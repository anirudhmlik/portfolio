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

# Custom CSS for navbar and progress bar
st.markdown("""
<style>
#navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background-color: #0b0c10;
    color: white;
    z-index: 9999;
    display: flex;
    justify-content: space-around;
    align-items: center;
    padding: 10px 0;
    font-family: Arial, sans-serif;
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
body {
    padding-top: 70px;
}
</style>

<div id="navbar">
    <a href="#home">Home</a>
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


# Sidebar
col_main, col_profile = st.columns([3, 1], gap="large")

with col_profile:
    st.image("profile_picture.jpg", caption="Anirudh Malik", width=220)
    st.markdown("**📍 Location:** Delhi, India")
    st.write("**📞 Contact:** +91 9058176356")
    st.write("**✉️ Email:** anirudhchoudhary308@gmail.com")
    st.markdown("[💼 LinkedIn](https://linkedin.com/in/whoisaphysicist/)")
    st.markdown("[🐙 GitHub](https://github.com/anirudhmlik)")

    try:
        with open("anirudh_malik_cv.pdf", "rb") as pdf_file:
            st.download_button("📄 Download CV", pdf_file, file_name="Anirudh_Malik_CV.pdf")
            if st.button("👁️ View CV Inline"):
                components.html(f"""
                    <embed src="anirudh_malik_cv.pdf" width="700" height="900" type="application/pdf">
                """, height=900)
    except FileNotFoundError:
        st.warning("CV file not found.")

    st.markdown("---")
    st.subheader("🌐 Languages")
    st.write("- English (Professional)\n- Hindi (Native)")

    st.subheader("💬 Interests")
    st.write("""
- Statistical modeling & data-driven decisions  
- Generative AI, LLMs, prompt engineering  
- MLOps pipelines & scalable ML systems  
- Data storytelling & visualization  
- Building AI tools for automation
""")
    st.markdown("**🏫 PG Education:**")
    st.write(""" MSc, University of Sheffield, UK
    """)
    
    st.subheader("🎖️ Certifications")
    st.write("""
- Data Science, ML, DL, NLP — Udemy  
- Mastering SQL & Analytics — Udemy  
- MLOps Bootcamp, DL Specialization — Udemy  
- Python for Data Analytics — Learntube.ai
""")


# ---- Main Content ----
with col_main:
    st.markdown('<div id="home"></div>', unsafe_allow_html=True)
    st_lottie(lottie_animation, height=250)
    st.title("Anirudh Malik")
    st.subheader("Scientific Software Engineer | Data Scientist | MLOps Engineer")
    st.write("""
I’m Anirudh Malik — a Scientific Software Engineer and Data Scientist passionate about bridging AI with real-world applications.  
I specialize in deploying scalable machine learning solutions, developing AI-powered chatbots, and optimizing ML pipelines for production environments.  
With a solid foundation in scientific research and practical engineering, I help transform ideas into automated, efficient systems.
""")
    st.markdown("---")


    # Skills
    st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
    st.header("📊 Skills Overview")

    skill_groups = {
        "Programming Languages": ["Python", "R", "SQL", "C++", "CUDA", "Bash"],
        "ML & Deep Learning Frameworks": ["TensorFlow", "PyTorch", "Scikit-learn", "Hugging Face Transformers"],
        "MLOps & Cloud Deployment": ["MLflow", "Apache Airflow", "Docker", "Kubernetes", "AWS EC2", "AWS Lambda"],
        "Data Tools": ["Pandas", "NumPy", "Matplotlib", "Seaborn", "REST APIs"],
        "Databases": ["MongoDB", "PostgreSQL", "MySQL", "Oracle"],
        "Scientific & Physics Tools": ["ROOT", "Geant4", "MadGraph", "Pythia8", "DDSCAT", "Optimal Transport"]
    }

    for category, skills in skill_groups.items():
        st.subheader(f"🔸 {category}")
        st.markdown(f"<div style='font-size:20px; color:#4CAF50;'>{' — '.join(skills)}</div>", unsafe_allow_html=True)
        st.markdown("---")

    # Experience
    st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
    st.header("💼 Professional Experience")

    experience = [
        {"role": "AI/ML Specialist", "company": "Imagenators, Noida", "duration": "05/2025 – Present",
         "details": [
             "Developed alumni chatbot using RAG pipelines (Ollama, LangChain, ChromaDB).",
             "Benchmarked GenAI vs traditional NLP pipelines for customer service solutions.",
             "Containerized ML pipelines using Docker for scalable deployments."
         ]},
        {"role": "Trainee Developer", "company": "Dev Group, New Delhi", "duration": "02/2025 – 05/2025",
         "details": [
             "Created CO₂ emission estimator and deployed it on AWS EC2 using Flask APIs and MLflow.",
             "Prototyped AI tools integrating REST APIs and LangChain."
         ]},
        {"role": "Research Associate", "company": "IIT Delhi", "duration": "04/2025 – Present",
         "details": [
             "Simulated Higgs boson production using MadGraph, Pythia8, and Delphes.",
             "Optimized physics analysis using ROOT and Python."
         ]},
        {"role": "Graduate Researcher", "company": "University of Sheffield", "duration": "09/2023 – 09/2024",
         "details": [
             "Developed ML models to improve electron identification for CERN ATLAS experiment.",
             "Worked on Optimal Transport techniques and statistical methods (sPlot, Tag-and-Probe)."
         ]}
    ]

    for job in experience:
        with st.expander(f"{job['role']} – {job['company']} ({job['duration']})"):
            details_html = "<br>".join([f"• {d}" for d in job["details"]])
            st.markdown(f"<div style='font-size:17px; color:white;'>{details_html}</div>", unsafe_allow_html=True)

    st.markdown("---")

    
    # Education
    st.markdown('<div id="education"></div>', unsafe_allow_html=True)
    st.header("🎓 Education")
    st.markdown("""
<div style='font-size:17px; color:white;'>
<ul>
<li><b>MSc in Particle Physics</b>, University of Sheffield, UK (2023–2024) — First Class</li>
<li><b>BSc in Physics, Math & Computer Science</b>, University of Delhi, India (2020–2023) — Distinction</li>
</ul>
</div>
""", unsafe_allow_html=True)

    st.header("📜 Certifications")
    st.markdown("""
<div style='font-size:17px; color:white;'>
<ul>
<li>Data Science, ML, DL, NLP – Krish AI Technologies (2025)</li>
<li>SQL & Analytics – Udemy (2025)</li>
<li>MLOps Bootcamp – Udemy (2024)</li>
<li>Python for Data Analytics – Learntube.ai (2024)</li>
</ul>
</div>
""", unsafe_allow_html=True)

    st.header("📝 MSc Dissertation Summary")
    st.markdown("""
<div style='font-size:17px; color:white;'>
<b>Electron Identification Using Machine Learning at CERN ATLAS Detector</b><br><br>
<ul>
<li>Applied ML to enhance electron identification efficiency using ATLAS Monte Carlo datasets.</li>
<li>Used Optimal Transport, PICNN, Tag-and-Probe, and sPlot techniques.</li>
<li>Technologies: TensorFlow, ROOT, Geant4, ATLFAST3, Python, C++.</li>
</ul>
</div>
""", unsafe_allow_html=True)

    st.markdown("---")



    # Projects
    st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
    st.header("🚀 Key Projects")

    projects = [
        {"title": "RAG-based Alumni Chatbot",
         "description": "Automated alumni interactions using Ollama, Mistral, LangChain, Django, ChromaDB (RAG + vector search).",
         "tech": "GenAI, Django, Docker, ChromaDB"},
        {"title": "Expense Tracker Bots",
         "description": "Conversational bots for managing expenses via WhatsApp and Telegram.",
         "tech": "Python, Flask, Telegram API"},
        {"title": "AI-Powered Property Chatbot",
         "description": "Real estate chatbot handling queries like '3BHK under ₹1.5Cr near Marina' using GPT-based NLP pipelines.",
         "tech": "GPT APIs, Flask, Docker, CSV/JSON backend"},
        {"title": "Electron ID at CERN",
         "description": "Improved electron ID using ML techniques (PICNN, Optimal Transport) on ATLAS Monte Carlo datasets.",
         "tech": "TensorFlow, ROOT, C++, Optimal Transport"},
        {"title": "3D Schrödinger Equation Solver",
         "description": "Numerical solver using CUDA acceleration, benchmarking GPU vs CPU performance.",
         "tech": "NumPy, SciPy, CUDA"}
    ]

    for project in projects:
        st.markdown(f"""
        <div style='margin-bottom: 20px;'>
        <h3 style='color:#007acc;'>{project['title']}</h3>
        <p style='font-size:16px; color:white;'>{project['description']}</p>
        <p style='font-size:15px; font-style:italic; color:#888;'>Tech Used: {project['tech']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")



    # Contact Form
    st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
    st.header("📬 Contact & Feedback")
    with st.form("feedback_form"):
        name = st.text_input("Your Name")
        feedback = st.text_area("Your Feedback")
        submitted = st.form_submit_button("Submit")
        if submitted:
            with open("feedback_log.txt", "a") as f:
                f.write(f"Name: {name}\nFeedback: {feedback}\n---\n")
            st.success("Thank you for your feedback!")

    st.markdown("<p style='text-align:center;'>© 2025 Anirudh Malik | Built with Streamlit</p>", unsafe_allow_html=True)
