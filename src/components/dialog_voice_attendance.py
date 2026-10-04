import streamlit as st
import pandas as pd
from datetime import datetime

try:
    from src.pipelines.voice_pipeline import process_bulk_audio
except Exception:
    process_bulk_audio = None

from src.database.config import supabase
from src.components.dialog_attendance_results import show_attendance_result


@st.dialog("Voice Attendance")
def voice_attendance_dialog(selected_subject_id):

    st.write(
        "Record audio of students saying 'I am present'. "
        "AI will recognize the enrolled students."
    )

    # Record classroom audio
    audio_data = st.audio_input("Record classroom audio")

    # Analyze audio
    if st.button(
        "Analyze Audio",
        width="stretch",
        type="primary"
    ):

        # Check audio
        if audio_data is None:
            st.warning("Please record classroom audio first.")
            return

        # Check voice pipeline
        if process_bulk_audio is None:
            st.error(
                "Voice attendance is unavailable because the voice pipeline "
                "could not be loaded."
            )
            return

        with st.spinner("Processing audio data..."):

            try:

                # Get enrolled students
                enrolled_res = (
                    supabase
                    .table("subject_students")
                    .select("*, students(*)")
                    .eq("subject_id", selected_subject_id)
                    .execute()
                )

                enrolled_students = enrolled_res.data or []

                if not enrolled_students:
                    st.warning(
                        "No students are enrolled in this subject."
                    )
                    return

                # Create voice candidate dictionary
                candidates_dict = {}

                for node in enrolled_students:

                    student = node.get("students")

                    if not student:
                        continue

                    student_id = student.get("student_id")
                    voice_embedding = student.get("voice_embedding")

                    if student_id and voice_embedding:
                        candidates_dict[student_id] = voice_embedding

                if not candidates_dict:
                    st.error(
                        "No enrolled students have registered voice profiles."
                    )
                    return

                # Read recorded audio
                audio_bytes = audio_data.read()

                if not audio_bytes:
                    st.warning(
                        "No audio was recorded. Please record again."
                    )
                    return

                # Run voice recognition
                detected_scores = process_bulk_audio(
                    audio_bytes,
                    candidates_dict
                )

                if detected_scores is None:
                    st.error(
                        "Voice recognition did not return any results."
                    )
                    return

                results = []
                attendance_to_log = []

                current_timestamp = datetime.now().strftime(
                    "%Y-%m-%dT%H:%M:%S"
                )

                # Prepare attendance results
                for node in enrolled_students:

                    student = node.get("students")

                    if not student:
                        continue

                    student_id = student.get("student_id")
                    student_name = student.get("name", "Unknown")

                    score = detected_scores.get(
                        student_id,
                        0.0
                    )

                    is_present = bool(score > 0)

                    results.append({
                        "Name": student_name,
                        "ID": student_id,
                        "Source": score if is_present else "-",
                        "Status": (
                            "✅ Present"
                            if is_present
                            else "❌ Absent"
                        )
                    })

                    attendance_to_log.append({
                        "student_id": student_id,
                        "subject_id": selected_subject_id,
                        "timestamp": current_timestamp,
                        "is_present": is_present
                    })

                # Save results
                st.session_state.voice_attendance_results = (
                    pd.DataFrame(results),
                    attendance_to_log
                )

                st.success("Voice attendance analysis completed.")

            except Exception as e:

                st.error(
                    f"Voice attendance failed: {str(e)}"
                )

    # Show attendance results
    if st.session_state.get("voice_attendance_results"):

        st.divider()

        df_results, logs = (
            st.session_state.voice_attendance_results
        )

        show_attendance_result(
            df_results,
            logs
        )