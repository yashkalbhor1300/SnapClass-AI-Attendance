import streamlit as st

from src.database.db import delete_subject


@st.dialog("Delete Subject")
def delete_subject_dialog(
    subject_id,
    subject_name,
    teacher_id
):

    st.warning(
        f'Are you sure you want to delete "{subject_name}"?'
    )

    st.write(
        "This will permanently delete the subject, "
        "its student enrollments, and its attendance records."
    )

    st.write("**This action cannot be undone.**")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "Cancel",
            width="stretch"
        ):

            st.rerun()

    with col2:

        if st.button(
            "Delete Subject",
            type="secondary",
            width="stretch",
            icon=":material/delete:"
        ):

            try:

                success = delete_subject(
                    subject_id,
                    teacher_id
                )

                if success:

                    st.success(
                        f'"{subject_name}" has been deleted successfully.'
                    )

                    st.session_state.current_teacher_tab = "manage_subjects"

                    import time
                    time.sleep(1)

                    st.rerun()

                else:

                    st.error(
                        "Unable to delete this subject. "
                        "The subject may not belong to your account."
                    )

            except Exception as e:

                st.error(
                    f"Delete failed: {e}"
                )