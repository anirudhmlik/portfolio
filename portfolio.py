import streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
import requests

# Page Config
st.set_page_config(page_title="Anirudh Malik Portfolio", layout="wide")

# Load Lottie Animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_animation = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_tfb3estd.json")

# Custom CSS for sticky sidebar and improved layout
st.markdown("""
<style>
/* Sticky Sidebar */
.sidebar-sticky {
    position: fixed;
    top: 20px;
    right: 20px;
    width: 300px;
    background-color: #0b0c10;
    color: white;
    padding: 20px;
    border-radius: 10px;
    font-family: Arial, sans-serif;
}

/* Main Scrollable Content */
.main-scroll {
    margin-right: 350px;
    padding: 30px;
}

/* Navbar */
#navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 320px;
    background-color: #0b0c10;
    color: white;
    z-index: 9999;
    display: flex;
    justify-content: space-around;
    align-items: center;
    padding: 10px 0;
    font-weight: bold;
}

#navbar a {
    color: white;
    text-decoration: none;
    padding: 8px 15px;
    border-radius: 5px;
    transition: background-color 0.3s ease;
}

#navbar a:hover {
    background-color: #1f2833;
}

#progress-container {
    width: 100%;
    background: #ddd;
    height: 5px;
    position: fixed;
    top: 50px;
    left: 0;
    z-index: 9999;
}

#progress-bar {
    height: 5px;
    background: #66fcf1;
    width: 0%;
}

</style>

<div id="navbar">
    <a href="#home">Home</a>
    <a href="#about">About</a>
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
    <a href="#experience">Experience</a>
    <a href="#education">Education</a>
    <a href="#contact">Contact</a>
</div>

<div id="progress-container">
    <div id="progress-bar"></div>
</div>

<script>
window.onscroll = function() {
    var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    var scrolled = (winScroll / height) * 100;
    document.getElementById("progress-bar").style.width = scrolled + "%";
};
</script>
""", unsafe_allow_html=True)

# Sidebar (Sticky Profile)
with st.container():
    components.html("""
    <div class='sidebar-sticky'>
        <img src="profile_picture.jpg" alt="Anirudh Malik" style="width:100%; border-radius:10px;">
        <h2>Anirudh Malik</h2>
        <p>📍 Delhi, India</p>
        <p><b>Email:</b> anirudhchoudhary308@gmail.com</p>
        <p><b>Phone:</b> +91 9058176356</p>
        <a href="https://linkedin.com/in/whoisaphysicist/" target="_blank">LinkedIn</a> | 
        <a href="https://github.com/anirudhmlik" target="_blank">GitHub</a>
        <br><br>
        <a href="anirudh_malik_cv.pdf" download style="color:#66fcf1;">📄 Download CV</a><br>
        <a href="anirudh_malik_cv.pdf" target="_blank" style="color:#66fcf1;">👁️ View CV Inline</a>
        <hr>
        <p><b>Languages:</b> English, Hindi</p>
        <p><b>Interests:</b> AI product design, ML research, teaching, scientific computing, astrophysics</p>
        <p><b>Freelance Gigs:</b> AI chatbot dev, real estate chatbot, data pipeline automation</p>
    </div>
    """, height=800)

# Main Content (Scrollable)
with st.container():
    st.markdown('<div class="main-scroll">', unsafe_allow_html=True)
    st_lottie(lottie_animation, height=200)
    st.title("Anirudh Malik")
    st.subheader("Scientific Software Engineer | Data Scientist | ML Engineer")

    st.markdown('<div id="about"></div>', unsafe_allow_html=True)
    st.header("👋 About Me")
    st.write("""
    I’m a Scientific Software Engineer and Machine Learning Specialist passionate about applying AI to scientific and business challenges.
    
    With experience in MLOps, NLP, particle physics applications, and full-stack AI systems, I specialize in building end-to-end machine learning pipelines, from data collection to deployment.

    Currently working on Generative AI projects and large-scale ML systems, I’m always eager to collaborate, innovate, and solve real-world problems.
    """)

    st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
    st.header("📊 Skills Overview")

    skills = {
        "Programming Languages": ["Python", "R", "SQL", "C++", "CUDA", "Bash"],
        "ML & DL Frameworks": ["TensorFlow", "PyTorch", "Scikit-learn", "Hugging Face Transformers"],
        "MLOps & Cloud Deployment": ["MLflow", "Apache Airflow", "Docker", "Kubernetes", "AWS EC2", "AWS Lambda"],
        "Data Tools": ["Pandas", "NumPy", "Matplotlib", "Seaborn", "REST APIs"],
        "Databases": ["MongoDB", "PostgreSQL", "MySQL", "Oracle"],
        "Scientific Tools": ["ROOT", "Geant4", "MadGraph", "Pythia8", "DDSCAT", "Optimal Transport"]
    }

    for category, skills_list in skills.items():
        st.subheader(f"🔸 {category}")
        st.markdown(f"<div style='font-size:17px; color:#66fcf1;'>{' • '.join(skills_list)}</div>", unsafe_allow_html=True)

    st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
    st.header("🚀 Key Projects")
    st.write("""
    - **RAG-based Alumni Chatbot:** Automated alumni query handling using Ollama, LangChain, ChromaDB.
    - **AI Property Chatbot:** NLP-powered property filter bot saving 15+ hours/week for real estate clients.
    - **Expense Tracker Bots:** Chat-based trackers deployed on WhatsApp and Telegram.
    - **Electron ID @ CERN (MSc Thesis):** ML-based electron classifier trained using ATLAS Monte Carlo datasets.
    - **3D Schrödinger Solver:** CUDA-accelerated 3D equation solver comparing CPU-GPU performance.
    """)

    st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
    st.header("💼 Professional Experience")
    st.write("""
    - **AI/ML Specialist – Imagenators, Noida (05/2025 – Present):**
        - Built scalable RAG-based chatbots.
        - Productionized AI microservices using Docker and AWS.

    - **Research Associate – IIT Delhi (04/2025 – Present):**
        - Simulated Higgs processes.
        - ML-based data analysis using ROOT and Python.

    - **Trainee Developer – Dev Group (02/2025 – 05/2025):**
        - Built REST APIs for ML models.
        - Created CO₂ emission estimator pipeline.

    - **Graduate Researcher – University of Sheffield (09/2023 – 09/2024):**
        - Thesis on ML-based particle classification.
        - Applied Optimal Transport and PICNN architectures.
    """)

    st.markdown('<div id="education"></div>', unsafe_allow_html=True)
    st.header("🎓 Education")
    st.write("""
    - **MSc Particle Physics – University of Sheffield (2023–2024)**  
      First Class with thesis focused on ATLAS detector and ML classifiers.

    - **BSc Physics, Math & Computer Science – University of Delhi (2020–2023)**  
      Graduated with Distinction.

    - **Schooling – Delhi Public School (DPS), India.**
    """)

    st.header("📬 Contact & Feedback")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        feedback = st.text_area("Your Feedback")
        submitted = st.form_submit_button("Submit")
        if submitted:
            with open("feedback_log.txt", "a") as f:
                f.write(f"Name: {name}\nFeedback: {feedback}\n---\n")
            st.success("Thank you for your feedback!")

    st.markdown("<p style='text-align:center;'>© 2025 Anirudh Malik | Built with Streamlit</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)