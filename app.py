import streamlit as st

st.set_page_config(page_title="Student Management", page_icon="🎓", layout="centered")

st.title("🎓 Student Management")
st.write("Add, view, and remove student records.")

if "students" not in st.session_state:
    st.session_state.students = []

with st.form("student_form", clear_on_submit=True):
    st.subheader("Add a student")
    name = st.text_input("Student name")
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    course = st.selectbox(
        "Course",
        ["Computer Science", "Information Technology", "Data Science", "Other"]
    )
    submitted = st.form_submit_button("Add student")

if submitted:
    if not name.strip():
        st.error("Please enter a student name.")
    else:
        st.session_state.students.append({
            "name": name.strip(),
            "age": int(age),
            "course": course
        })
        st.success(f"Added {name.strip()} successfully.")

st.divider()
st.subheader("Student records")

if not st.session_state.students:
    st.info("No students added yet.")
else:
    for index, student in enumerate(st.session_state.students):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(
                f"**{student['name']}**  \n"
                f"Age: {student['age']} · Course: {student['course']}"
            )
        with col2:
            if st.button("Delete", key=f"delete_{index}"):
                st.session_state.students.pop(index)
                st.rerun()
