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


# Main Content
with col_main:
    st.markdown('<div id="home"></div>', unsafe_allow_html=True)
    st_lottie(lottie_animation, height=250)
    st.title("Anirudh Malik")
    st.subheader("ML Engineer — Data Scientist — Scientific Software Engineer")
    st.write("""
I am a Scientific Software Engineer and Data Scientist with experience across AI product development, MLOps, and cloud deployment.  
My expertise includes Python, SQL, C++, TensorFlow, and PyTorch.  
I focus on scalable ML pipelines and solving complex problems in science and computation.
""")
    st.markdown("---")

    st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
    st.header("📊 Skills")
    st.write("""
**Languages:** Python, C++, SQL, Bash  
**Frameworks:** TensorFlow, PyTorch, Scikit-learn, Transformers  
**MLOps:** MLFlow, Airflow, Docker, Kubernetes, AWS EC2, Lambda  
**Databases:** PostgreSQL, MongoDB, Oracle  
**Tools:** Pandas, NumPy, Matplotlib, Seaborn, REST APIs  
**Scientific:** ROOT, Geant4, MadGraph, DDSCAT, Optimal Transport
""")
    st.markdown("---")

    st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
    st.header("🚀 Projects")
    st.write("""
**RAG-based Alumni Chatbot:** Ollama, Mistral, LangChain, Django, ChromaDB  
**Expense Tracker Bots:** WhatsApp/Telegram bots using Flask, Python, JSON  
**AI-Powered Property Chatbot:** GPT APIs, property search backend  
**Electron ID at CERN:** PICNN, Optimal Transport with ATLAS datasets  
**3D Schrödinger Solver:** CUDA-accelerated solver comparing CPU vs GPU  
**Retail Sales Forecasting:** ML pipeline with Flask, MLflow on AWS  
**Fraud Detection System:** Spark-based fraud detection with AWS Lambda  
**YouTube Comment Analysis:** Transformer-based sentiment analysis
""")
    st.markdown("---")

    st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
    st.header("💼 Professional Experience")
    st.write("""
**AI/ML Specialist — Imagenators (Noida) [05/2025 – Present]**  
- Developed alumni chatbot using RAG pipelines  
- Benchmarked GenAI vs classical NLP retrieval  
- Containerized pipelines with Docker  

**Trainee Developer — Dev Group (New Delhi) [02/2025 – 05/2025]**  
- Prototyped AI tools with REST APIs, LangChain  
- Built CO₂ emission estimator using Flask, MLFlow on AWS  

**Research Associate — IIT Delhi [04/2025 – Present]**  
- Simulated gg → H → τ+τ− with MadGraph5, Pythia8, Delphes  
- Used ROOT and Python for event optimization  

**Graduate Researcher — University of Sheffield (UK) [09/2023 – 09/2024]**  
- Built PICNN classifiers for electron ID at CERN  
- Applied Optimal Transport to simulation alignment  

**Undergraduate Researcher — University of Delhi [09/2022 – 05/2023]**  
- Simulated SPR via DDSCAT  
- Studied AgNO3 nanomaterials' optical properties
""")
    st.markdown("---")

    st.markdown('<div id="education"></div>', unsafe_allow_html=True)
    st.header("🎓 Education")
    st.write("""
**MSc in Particle Physics — University of Sheffield, UK (2023 – 2024)**  
First Division  

**BSc in Physical Science — University of Delhi, India (2020 – 2023)**  
Distinction  

**Senior Secondary, ISC — Mount Carmel School (2018 – 2020)**  
94%
""")
    st.markdown("---")

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
