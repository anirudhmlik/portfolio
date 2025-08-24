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
    st.image("photo.png", caption="Anirudh Malik", width=220)
    st.markdown("**📍 Location:** Delhi, India")
    st.write("**📞 Contact:** +91 9058176356")
    st.write("**✉️ Email:** anirudhforjobs@gmail.com")
    st.markdown("[💼 LinkedIn](https://linkedin.com/in/whoisaphysicist/)")
    st.markdown("[🐙 GitHub](https://github.com/anirudhmlik)")

    try:
        with open("AnirudhMalik.pdf", "rb") as pdf_file:
            st.download_button("📄 Download CV", pdf_file, file_name="Anirudh_Malik_CV.pdf")
    except FileNotFoundError:
        st.warning("CV file not found.")

    st.markdown("---")
    st.subheader("🌐 Languages")
    st.write("- English (Professional)\n- Hindi (Native)")

    st.subheader("💬 Interests")
    st.write("""
- Statistical modeling & AI-driven insights  
- Generative AI & Large Language Models (LLMs)  
- Predictive modeling & Recommender systems  
- Scalable ML pipelines & MLOps  
- Quantum Computing & Quantum ML
""")

    st.subheader("🎖️ Hobbies")
    st.write("""
- Basketball 🏀
- Physics research as a passion project
""")

# ---- Main Content ----
with col_main:
    st.markdown('<div id="home"></div>', unsafe_allow_html=True)

    col_lottie, col_intro = st.columns([2, 3])

    with col_lottie:
        if lottie_animation:
            st_lottie(lottie_animation, height=250)

    with col_intro:
        st.title("Anirudh Malik")
        st.subheader("Data Scientist | AI/ML Engineer | Scientific Software Engineer")
    st.write("""
I’m **Anirudh Malik** — a Data Scientist and AI/ML Software Engineer passionate about **bridging research with real-world AI applications**.  
I specialize in **predictive modeling, generative AI, anomaly detection, and scalable ML pipelines**, with proven experience across research and industry.  
With a strong background in **particle physics research** and **AI engineering**, I deliver intelligent, production-ready solutions.
""")
    st.markdown("---")

    # Skills
    st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
    st.header("📊 Skills Overview")

    skill_groups = {
        "Programming Languages": ["Python", "C++", "SQL", "Bash", "Java"],
        "Machine Learning & AI": ["Predictive Modeling", "Recommender Systems", "Generative AI (VAEs, GANs, Transformers)", "Deep Learning", "NLP", "Text Mining"],
        "Big Data & MLOps": ["Apache Spark", "Hadoop", "Docker", "Kubernetes", "Airflow", "MLflow"],
        "Frameworks & APIs": ["FastAPI", "Flask", "Django", "LangChain", "Ollama", "Mistral"],
        "Cloud Platforms": ["AWS", "Azure"],
        "Databases": ["PostgreSQL", "MongoDB", "MySQL"],
        "Visualization": ["Matplotlib", "Seaborn"],
        "Physics & Simulation Tools": ["ROOT", "Geant4", "MadGraph5", "DDSCAT", "Optimal Transport"]
    }

    for section, items in skill_groups.items():
        st.subheader(f"🔹 {section}")
        st.markdown(f"<div style='font-size:18px; color:#4CAF50;'>" + " — ".join(items) + "</div>", unsafe_allow_html=True)

    st.markdown("---")

    # Experience
    st.markdown("<div id='experience'></div>", unsafe_allow_html=True)
    st.header("💼 Professional Experience")

    experience = [
        {
            "title": "AI - Software Engineer – Dextra Labs (Aug 2025 – Present)",
            "description": """Working on **Instavaluate**, an AI-powered valuation platform for auditors & customers.
- Automated Excel-to-template parsing with NLP.
- Built AI-powered chatbot for onboarding & valuation support.
- Developed narrative generation tools for financial reports.
- Implemented AI-driven forecasting models using market data.
"""
        },
        {
            "title": "Research Associate – IIT Delhi (Apr 2025 – Present)",
            "description": """Developing **hybrid anomaly detection (VAE + FROCC)** for unsupervised jet tagging.  
Simulated **gg → H → τ+τ−** using MadGraph5 + Pythia8 + Delphes.  
Conducted EDA on CMS MiniAOD datasets for tau leptons.  
Designed latent-space anomaly scores for model-independent new physics searches.
"""
        },
        {
            "title": "AI/ML Specialist – Imagenators (May 2025 – Jul 2025)",
            "description": """Built and deployed containerized **RAG systems** using FastAPI, LangChain, FAISS, Gemini.  
Benchmarked GenAI vs traditional NLP.  
Optimized Revolt Motors’ **voice assistant** with Gemini's audio-dialog model.
"""
        },
        {
            "title": "Trainee Developer – Dev Group (Feb 2025 – May 2025)",
            "description": """Developed **CO₂ emissions prediction models** using Flask + MLflow.  
Created dashboards and Python REST APIs for analytics tools.
"""
        },
        {
            "title": "Graduate Researcher – Univ. of Sheffield (Sep 2023 – Sep 2024)",
            "description": """Built **PICNN classifiers** for Z → e+e− using ATLAS MC data.  
Applied **Optimal Transport** to match AF3 & Geant4 simulations.
"""
        },
        {
            "title": "Undergraduate Researcher – Univ. of Delhi (Sep 2022 – May 2023)",
            "description": """Simulated **surface plasmon resonance** via DDSCAT.  
Analyzed dielectric properties of AgNO₃ nanomaterials.
"""
        }
    ]

    for exp in experience:
        desc_html = exp["description"].replace("\n", "<br>")
        st.markdown(
        f"""
        <div style='margin-bottom: 25px;'>
            <h3 style='color:#007acc;'>{exp['title']}</h3>
            <p style='font-size:16px; color:white;'>{desc_html}</p>
        </div>
        """,
        unsafe_allow_html=True
        )

    st.markdown("---")

    # Education
    st.markdown('<div id="education"></div>', unsafe_allow_html=True)
    st.header("🎓 Education")
    st.markdown("""
<div style='font-size:17px; color:white;'>
<ul>
<li><b>MSc in Particle Physics</b>, University of Sheffield, UK (2023–2024) — First Class</li>
<li><b>BSc in Physical Science</b>, University of Delhi, India (2020–2023) — Distinction</li>
<li><b>Senior Secondary (ISC)</b>, Mount Carmel School (2018–2020) — 94%</li>
</ul>
</div>
""", unsafe_allow_html=True)

    st.header("📜 Certifications")
    st.markdown("""
<div style='font-size:17px; color:white;'>
<ul>
<li>Data Science, ML, DL, NLP – Krish AI Technologies (2025)</li>
<li>Mastering SQL & Analytics – Udemy (2025)</li>
</ul>
</div>
""", unsafe_allow_html=True)

    st.markdown("---")

# Contact
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.header("📬 Contact & Feedback")
st.write("**📞 Contact:** +91 9058176356")
st.write("**✉️ Email:** anirudhforjobs@gmail.com")
st.markdown("[💼 LinkedIn](https://linkedin.com/in/whoisaphysicist/)")
st.markdown("[🐙 GitHub](https://github.com/anirudhmlik)")

st.markdown(" MSc | AI/ML Engineer | Anirudh Malik | Data Scientist | Immediately Available ", unsafe_allow_html=True)
