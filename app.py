import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
import base64

# --- Custom CSS ---
st.markdown('''
    <style>
        .main {background-color: #f5f7fa;}
        .css-1d391kg {background: #fff; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);}
        .stButton>button {background-color: #4F8BF9; color: white; border-radius: 8px;}
        .st-bb {background: #4F8BF9; color: white; border-radius: 8px;}
        .stProgress > div > div > div > div {background-image: linear-gradient(90deg, #4F8BF9, #6DD5FA);}
        .stRadio > div {flex-direction: row;}
        .st-cq {border-radius: 50%;}
    </style>
''', unsafe_allow_html=True)

# --- Helper functions ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def get_base64_of_file(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def download_button(file_path, label):
    b64 = get_base64_of_file(file_path)
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_path}"><button>{label}</button></a>'
    st.markdown(href, unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", [
    "Home", "About", "Education", "Skills", "Projects & Research", "Achievements & Certifications", "Contact"
])

# --- Lottie Animation ---
lottie_url = "https://assets2.lottiefiles.com/packages/lf20_kyu7xb1v.json"  # fun developer animation
lottie_json = load_lottieurl(lottie_url)

# --- Profile Image ---
try:
    image = Image.open("profile.jpg")  # Place your profile image as 'profile.jpg' in the root
except:
    image = None

# --- Animated Header ---
if section == "Home":
    col1, col2 = st.columns([1,3])
    with col1:
        if image:
            st.image(image, width=120, caption="Patel Vatsal", output_format="auto")
        else:
            st_lottie(lottie_json, height=120)
    with col2:
        st.markdown("""
        <h1 style='font-size:2.8rem; font-weight:700; color:#4F8BF9;'>Patel Vatsal</h1>
        <h3 style='color:#222;'>AI/ML Researcher & Engineer</h3>
        <p style='font-size:1.1rem;'>Surat, Gujarat | <a href='mailto:[REDACTED]'>[REDACTED]</a></p>
        <a href='https://github.com/alphaboy017' target='_blank'><img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg' width='32' style='margin-right:10px;'/></a>
        <a href='https://www.linkedin.com/in/patelvatsal17/' target='_blank'><img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg' width='32'/></a>
        """, unsafe_allow_html=True)
    st.write("")
    st_lottie(lottie_json, height=180)
    st.write("")
    st.markdown("""
    <span style='font-size:1.2rem;'>Welcome to my interactive portfolio! Use the sidebar to explore my work, skills, and achievements.</span>
    """, unsafe_allow_html=True)
    st.write("")
    # Download CV button
    # Place your CV as 'Vatsal_CV.pdf' in the root directory
    try:
        download_button("Vatsal_CV.pdf", "Download My CV")
    except:
        st.info("CV download coming soon!")

# --- About ---
if section == "About":
    st.header("About Me")
    st.markdown("""
    - Bachelor of Engineering - Computer Engineering (Expected 2026)
    - C.K. Pithawala College of Engineering and Technology, Gujarat, India
    - Passionate about AI, Data Science, and building scalable ML systems.
    """)
    st_lottie(lottie_json, height=120)

# --- Education ---
if section == "Education":
    st.header("Education")
    st.markdown("""
    **C.K. Pithawala College of Engineering and Technology**  
    Bachelor of Engineering - Computer Engineering  
    Gujarat, India (Expected 2026)  
    **CGPA:** 7.4  
    **Courses:** Artificial Intelligence, Data Mining, Theory of Computation, Data Structures and Algorithms, OOP, DBMS
    """)

# --- Skills ---
if section == "Skills":
    st.header("Skills Summary")
    st.write("")
    skills = {
        "Python": 80,
        "Java": 65,
        "R": 60,
        "C": 60,
        "JavaScript": 70,
        "TensorFlow": 75,
        "pandas": 85,
        "NumPy": 85,
        "scikit-learn": 80,
        "Keras": 70,
        "matplotlib": 80,
        "seaborn": 70,
        "Google Cloud": 60,
        "Flutter": 50,
        "Figma": 60,
        "React": 50,
        "HTML/CSS": 70,
        "Node.js": 60,
        "Mongoose": 55,
        "REST API": 70,
        "Firebase": 55
    }
    for skill, percent in skills.items():
        st.write(f"{skill}")
        st.progress(percent)
    st.write("")
    st.markdown("**Soft Skills:** Problem solving, Communication, Management, Leadership")

# --- Projects & Research ---
if section == "Projects & Research":
    st.header("Projects & Research")
    with st.expander("Modular ML Pipeline with MLflow"):
        st.markdown("""
        - Engineered a modular ML pipeline with MLflow and a YAML-driven config/schema/params framework for reproducibility and streamlined hyperparameter tuning.
        - Automated CI/CD workflows via GitHub Actions: built Docker images, pushed to AWS-ECR, spun up self-hosted EC2 runners, and deployed models in under 10 minutes.
        - Centralized experiment tracking by integrating DagsHub as a remote MLflow server, managing credentials securely with environment variables.
        - Built a Flask microservice to serve trained models over RESTful endpoints, enabling real-time inference for downstream applications.
        """)
    with st.expander("Stock Price Prediction with LSTM & GRU"):
        st.markdown("""
        - Compared LSTM and GRU models for predicting prices of TCS, Reliance, and Infosys.
        - Enhanced model inputs with RSI, MACD, and Bollinger Bands to improve accuracy.
        - Achieved RMSE as low as 0.02 and MAE under 0.015 on normalized stock data.
        - Demonstrated performance improvements using visual RMSE/MAE comparisons.
        """)
    with st.expander("UAV-Based Mesh Networks for Emergency Communication"):
        st.markdown("""
        - Analyzed UAV-based mesh networks for emergency communication, proposing a hybrid deployment model using UAVs and ground-based relays to achieve up to 98.7% coverage reliability.
        - Utilized Ubiquiti Bullet M2 HP with 12 dBi directional mesh antennas and SDN for network management, estimating throughput ranging from 35-120 Mbps.
        - Covered challenges like UAV energy constraints, spectrum interference, and regulatory compliance.
        """)

# --- Achievements & Certifications ---
if section == "Achievements & Certifications":
    st.header("Achievements & Certifications")
    st.markdown("""
    - Scored 47/50 marks in Future of India's Space Exploration Course
    - Completed Course and earned 37 valuable badges
    - Volunteer, C.K. Pithawala College of Engineering and Technology
    - Successfully completed the START - Space Science and Technology Awareness Training by ISRO and IIRS
    - Gained deep insights into India's space missions, advanced propulsion, space biology, quantum communication, and planetary exploration
    - Gaseous air pollutants: Monitoring and modeling
    """)
    st_lottie(lottie_json, height=120)

# --- Contact ---
if section == "Contact":
    st.header("Contact Me")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success("Thank you for your message! (This is a demo form.)")
    st.write("")
    st.markdown("""
    <a href='https://github.com/alphaboy017' target='_blank'><img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg' width='32' style='margin-right:10px;'/></a>
    <a href='https://www.linkedin.com/in/patelvatsal17/' target='_blank'><img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg' width='32'/></a>
    """, unsafe_allow_html=True) 