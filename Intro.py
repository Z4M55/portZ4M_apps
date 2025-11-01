import streamlit as st

# 🎨 Colores personalizados
st.markdown("""
    <style>
    body {
        background-color: #B7E5CD;
        color: #305669;
    }
    .stApp {
        background-color: #B7E5CD;
    }
    .project-card {
        background-color: white;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        text-align: center;
        transition: transform 0.2s ease-in-out;
    }
    .project-card:hover {
        transform: scale(1.03);
        box-shadow: 0px 6px 16px rgba(0,0,0,0.15);
    }
    .project-title {
        font-size: 22px;
        font-weight: bold;
        margin-top: 10px;
        color: #305669;
    }
    .open-btn {
        color: #305669;
        font-weight: bold;
        text-decoration: none;
        margin-top: 10px;
        display: inline-block;
    }
    .open-btn:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# 📸 Datos de los proyectos
projects = [
    {"name": "Intro ✨", "image": "SAMURAI.jpg"},
    {"name": "Texto - Voz 🔊", "image": "thor.jpg"},
    {"name": "Voz - Texto 🎙️", "image": "DEADPOOL.jpg"},
    {"name": "Imagen - Texto 🖼️", "image": "IRONMANN.jpg"},
    {"name": "Análisis de Imagen 🔍", "image": "GRUU.jpg"},
    {"name": "Análisis de Sentimiento ❤️", "image": "LOKI.jpg"},
    {"name": "Análisis de texto (Inglés) 🇺🇸", "image": "blackpanter.jpg"},
    {"name": "Análisis de texto (Español) 🇪🇸", "image": "CAPAMERICA.jpg"},
    {"name": "Reconocimiento de Objeto 🧠", "image": "CAPAMERICA.jpg"},
    {"name": "Detección de gestos ✋", "image": "LOBEZNO.jpg"}
]

# 🧱 Mostrar las tarjetas en una cuadrícula
cols = st.columns(5)  # Ajusta el número de columnas según tu gusto
for i, project in enumerate(projects):
    with cols[i % 5]:
        st.markdown(f"""
        <div class="project-card">
            <img src="{project['image']}" alt="{project['name']}" width="100%" style="border-radius:15px;"/>
            <div class="project-title">{project['name']}</div>
            <a class="open-btn" href="#">Abrir proyecto ↗</a>
        </div>
        """, unsafe_allow_html=True)
