from pathlib import Path

p = Path("src/screens/teacher_screen.py")
s = p.read_text(encoding="utf-8")

old = """    subject_options = {
        f"{s['name']} - {s['subject_code']}": s['subject_id']
        for s in subjects
    }
"""

new = """    sections = sorted(list(set(
        str(s.get('section', '')).strip()
        for s in subjects
        if s.get('section')
    )))

    if not sections:
        st.warning('No sections found for your subjects.')
        return

    selected_section = st.selectbox(
        'Select Section',
        options=sections,
        key='attendance_section'
    )

    section_subjects = [
        s for s in subjects
        if str(s.get('section', '')).strip() == selected_section
    ]

    if not section_subjects:
        st.warning(
            f'No subjects found for Section {selected_section}.'
        )
        return

    subject_options = {
        f"{s['name']} - {s['subject_code']}": s['subject_id']
        for s in section_subjects
    }
"""

if old not in s:
    print("ERROR: Original code was not found.")
else:
    s = s.replace(old, new, 1)
    p.write_text(s, encoding="utf-8")
    print("SUCCESS: Section selection added.")