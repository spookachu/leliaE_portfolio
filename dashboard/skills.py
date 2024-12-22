import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Skills & Certificates Dashboard",
    page_icon="🎓",
    layout="wide",
)
MAIN_COLOR = "#4CAF50"
SECONDARY_COLOR = "#45a049"
TEXT_COLOR = "#333333"
BACKGROUND_COLOR = "#f9f9f9"
st.markdown(
    f"""
    <style>
    body {{
        background-color: {BACKGROUND_COLOR};
        color: {TEXT_COLOR};
    }}
    .stButton>button {{
        background-color: {MAIN_COLOR};
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
    }}
    .stButton>button:hover {{
        background-color: {SECONDARY_COLOR};
    }}
    </style>
    """,
    unsafe_allow_html=True,
)
st.title("🎓 Skills & Certificates Dashboard")
st.markdown("Explore my skills and certifications interactively!")
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to:", ["Skills", "Certificates"])

# Skills Data
skills = {
    "Programming": ["Python", "MATLAB", "Java", "R", "SQL", "C#"],
    "Tools": ["TensorFlow", "Pandas", "Scikit-learn"],
    "Languages": ["Romanian", "English", "French", "Japanese"],
}

# Certificates Data
certificates = [
    {"title": "Simulation Neuroscience", "issuer": "EPFLx", "date": "May 2024"},
    {"title": "ISO 14155 Clinical Investigation", "issuer": "TÜV SÜD", "date": "Feb 2024"},
]

PASSWORD = "yeet"
# Display Skills
if section == "Skills":
    st.header("🛠 Skills")

    for skill_category, skill_list in skills.items():
        st.markdown(f"### {skill_category}")
        cols = st.columns(len(skill_list))
        for col, skill in zip(cols, skill_list):
            with col:
                st.markdown(f"**{skill}**")

    password_input = st.sidebar.text_input("Enter password to edit ratings:", type="password")
    if password_input == PASSWORD:
        st.subheader("⭐ Rate Your Skills!")
        for skill_category, skill_list in skills.items():
            st.markdown(f"### {skill_category}")
            for skill in skill_list:
                st.slider(f"{skill}", 0, 10, 5, key=f"{skill}")
    else:
        st.sidebar.error("Unauthorized access. Enter the correct password to edit ratings.")

# Display Certificates
elif section == "Certificates":
    st.header("🏅 Certificates")
    for cert in certificates:
        st.markdown(
            f"""
            **{cert['title']}**  
            *Issued by*: {cert['issuer']}  
            *Issue Date*: {cert['date']}  
            ---
            """
        )
