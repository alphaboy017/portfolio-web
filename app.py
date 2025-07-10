import streamlit as st
from PIL import Image

# --- Sidebar ---
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", [
    "Home", "About", "Education", "Skills", "Projects & Research", "Achievements & Certifications", "Links"
])

# --- Header ---
if section == "Home":
    st.title("Patel Vatsal")
    st.write("t Researcher")
    st.write("Surat, Gujarat | Mobile: 9327187353 | Email: [REDACTED]")
    st.write("[GitHub](https://github.com/alphaboy017) | [LinkedIn](https://www.linkedin.com/in/patelvatsal17/)")
    # Uncomment and add your photo if desired
    # image = Image.open('path_to_photo.jpg')
    # st.image(image, width=150)

# --- About ---
if section == "About":
    st.header("About Me")
    st.markdown("""
    - Bachelor of Engineering - Computer Engineering (Expected 2026)
    - C.K. Pithawala College of Engineering and Technology, Gujarat, India
    - Passionate about AI, Data Science, and building scalable ML systems.
    """)

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
    st.markdown("""
    - **Languages:** Python (Intermediate), Java, R, C, JavaScript
    - **Data Science:** TensorFlow, pandas, NumPy, scikit-learn, Keras, matplotlib, seaborn
    - **Cloud:** Google Cloud
    - **Frontend:** Flutter, Figma, React (basic), HTML, CSS
    - **Backend:** Node.js, Mongoose, REST API, Firebase
    - **Soft Skills:** Problem solving, Communication, Management, Leadership
    """)

# --- Projects & Research ---
if section == "Projects & Research":
    st.header("Projects & Research")
    st.subheader("Modular ML Pipeline with MLflow")
    st.markdown("""
    - Engineered a modular ML pipeline with MLflow and a YAML-driven config/schema/params framework for reproducibility and streamlined hyperparameter tuning.
    - Automated CI/CD workflows via GitHub Actions: built Docker images, pushed to AWS-ECR, spun up self-hosted EC2 runners, and deployed models in under 10 minutes.
    - Centralized experiment tracking by integrating DagsHub as a remote MLflow server, managing credentials securely with environment variables.
    - Built a Flask microservice to serve trained models over RESTful endpoints, enabling real-time inference for downstream applications.
    """)
    st.subheader("Stock Price Prediction with LSTM & GRU")
    st.markdown("""
    - Compared LSTM and GRU models for predicting prices of TCS, Reliance, and Infosys.
    - Enhanced model inputs with RSI, MACD, and Bollinger Bands to improve accuracy.
    - Achieved RMSE as low as 0.02 and MAE under 0.015 on normalized stock data.
    - Demonstrated performance improvements using visual RMSE/MAE comparisons.
    """)
    st.subheader("UAV-Based Mesh Networks for Emergency Communication")
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

# --- Links ---
if section == "Links":
    st.header("Links")
    st.markdown("""
    - [GitHub](https://github.com/alphaboy017)
    - [LinkedIn](https://www.linkedin.com/in/patelvatsal17/)
    """) 