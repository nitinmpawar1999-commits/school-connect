import streamlit as st

st.title("SchoolConnect 🏫")
st.write("Welcome to your School Management App!")

# Simple Menu
menu = ["Student Admission", "Attendance", "Homework"]
choice = st.sidebar.selectbox("Select Feature", menu)

if choice == "Student Admission":
    st.header("Student Registration")
    name = st.text_input("Name")
    if st.button("Register"):
        st.success(f"{name} registered!")

elif choice == "Attendance":
    st.header("Daily Attendance")
    st.checkbox("Is Student Present?")

elif choice == "Homework":
    st.header("Daily Homework")
    st.text_area("Write homework details here...")
