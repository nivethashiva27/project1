import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Student Dashboard",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #e0f2fe, #f5f3ff);
}

.main-title {
    text-align: center;
    color: #312e81;
    font-size: 38px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #475569;
    font-size: 18px;
}

.welcome-card {
    background: white;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🎓 Student Portal")
menu = st.sidebar.radio(
    "Navigation",
    ["Home", "My Profile", "Contact"]
)

# Home page
if menu == "Home":

    st.markdown(
        '<p class="main-title">Welcome to My Dashboard</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="subtitle">Your Learning Journey Starts Here!</p>',
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Courses", "5")
    col2.metric("Completed", "3")
    col3.metric("Progress", "60%")

    st.divider()

    st.subheader("✨ Student Registration")

    with st.form("student_form"):

        name = st.text_input("Enter Your Name")

        email = st.text_input("Enter Your Email")

        course = st.selectbox(
            "Select Your Course",
            ["Python", "Java", "React", "Data Science", "AI"]
        )

        submitted = st.form_submit_button(
            "Register Now",
            use_container_width=True
        )

        if submitted:
            if name.strip() and email.strip():
                st.success(f"Welcome {name}!")
                st.write("Email:", email)
                st.write("Selected Course:", course)
                st.balloons()
            else:
                st.warning("Please enter your name and email.")

    st.divider()

    st.subheader("📚 My Learning Progress")

    st.write("Python Programming")
    st.progress(80)

    st.write("Web Development")
    st.progress(60)

    st.write("Artificial Intelligence")
    st.progress(40)

# Profile page
elif menu == "My Profile":

    st.title("👩‍🎓 My Profile")

    st.info("Welcome to your student profile.")

    st.write("Name: Student")
    st.write("Course: Python Full Stack Development")
    st.write("Skills: Python, HTML, CSS, JavaScript")

# Contact page
elif menu == "Contact":

    st.title("📞 Contact Us")

    st.write("Email: student@example.com")

    st.write("Thank you for visiting!")