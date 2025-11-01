# app.py
# Portafolio · Tema: Dioses + Tecnología (tonos oscuros, dorado y azul)
# - Coloca imágenes .jpg en ./images/ con los nombres de superhéroes indicados.
# - Si faltan imágenes, se usan placeholders automáticos.
# - El orden de asignación de imágenes a proyectos es aleatorio cada vez que se ejecuta.

import streamlit as st
import random
import os
import urllib.parse
from datetime import datetime

# ------------------------
# Configuración página
# ------------------------
st.set_page_config(page_title="⌬ Portafolio — Dioses & Tech ⌬", page_icon="⚡", layout="wide")
st.markdown("""
<style>
/* Theme: dark + dorado + azul (dioses + tecnología) */
:root{
  --bg: #071022;        /* very dark navy */
  --panel: #0f2236;     /* dark blue panel */
  --gold: #C9A84A;      /* soft gold */
  --accent: #2F7BD8;    /* tech blue */
  --muted: #9fb3c8;
  --card-bg: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(0,0,0,0.06));
}
html, body, .stApp {
  background: radial-gradient(900px 500px at 10% 0%, #07142a 0%, var(--bg) 70%);
  color: #e9f1fb;
  font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
}
h1,h2,h3 {
  color: var(--gold) !important;
  text-align: left;
  letter-spacing: 1px;
  font-weight: 700;
}
.header-box{
  border-left: 6px solid var(--gold);
  padding: 18px;
  border-radius: 10px;
  background: linear-gradient(90deg, rgba(47,123,216,0.03), rgba(201,168,74,0.02));
  margin-bottom: 12px;
}
.card {
  background: var(--card-bg);
  border: 1px solid rgba(47,123,216,0.12);
  border-radius: 14px;
  padding: 12px;
  transition: transform .18s ease, box-shadow .18s ease;
  box-shadow: 0 6px 18px rgba(0,0,0,0.5);
}
.card:hover {
  transform: translateY(-6px) scale(1.01);
  box-shadow: 0 12px 32px rgba(47,123,216,0.12);
}
.card img {
  width: 100%;
  height: 180px;
  object-fit: cover;
  border-radius: 10px;
  border: 2px solid rgba(201,168,74,0.12);
}
.card h4 {
  margin: 10px 0 6px 0;
  color: #eaf6ff;
}
.card p { color: var(--muted); margin: 0; font-size: 14px; }
.card a {
  display:inline-block;
  margin-top:8px;
  color: var(--gold);
  text-decoration:none;
  font-weight:700;
}
.card a:hover { color: #fff; text-decoration:underline; }
.row {
  margin-bottom: 18px;
}
.meta {
  font-size:12px; color: var(--muted);
}
.grid {
  gap: 18px;
}
.footer {
  color: var(--muted);
  margin-top: 18px;
}
.badge {
  display:inline-block;
  padding:6px 10px;
  border-radius:999px;
  background: rgba(201,168,74,0.12);
  border:1px solid rgba(201,168,74,0.16);
  color: var(--gold);
  font-weight:700;
  font-size:12px;
}
</style>
""", unsafe_allow_html=True)

# ------------------------
# Datos del portafolio (proyectos y links)
# ------------------------
projects = [
    ("Intro", "https://intro2-2bbeuqnqeswgfoyswmhcpr.streamlit.app/"),
    ("Texto - Voz", "https://imm1porfe-6ccneorn74eegcazqt3vev.streamlit.app/"),
    ("Voz - texto", "https://traductor-mqlkxigyt53vvahwgpnvvz.streamlit.app/"),
    ("Imagen-texto", "https://ocr040925imagetotext.streamlit.app/"),
    ("Análisis de Imagen", "https://visionapp-25-09-25-interpretacion-de-imagenes.streamlit.app/"),
    ("Análisis de Sentimiento", "https://txa-11-09-25.streamlit.app/"),
    ("Análisis de texto (Inglés)", "https://tf-txa11-09-25.streamlit.app/"),
    ("Análisis de texto (Español)", "https://ocr-audio-04-09-25-wk.streamlit.app/"),
    ("Reconocimiento de Objeto en Imagen", "https://yolov5-18-09-25-9.streamlit.app/"),
    ("Detección de gestos", "https://tm-18-09-25-deteccion-de-gestos-en-aplicacion.streamlit.app/"),
    ("Reconocimiento de escritura manual", "https://jmmkjajakhandw-6e65smhjjbwbbpcnzktx59.streamlit.app/"),
    ("bocetos", "https://bocetosdrawrecog-hedij5ffxtqnqolquyfuyy.streamlit.app/"),
    ("Lector de sensor", "https://recepmqtt161025-e7jafwey8ayhjzcazgd7yn.streamlit.app/"),
    ("MQTT Control", "https://sendcmqttbotones-elwaife6rhrsewvqkrenaq.streamlit.app/"),
    ("Control por Voz + MQTT", "https://ctrlvoice16-10-25voz--iot-y-sistemas-ciberfisicos.streamlit.app/"),
]

# Lista de nombres de imagenes proporcionados por el usuario
hero_names = [
    "BLACKPANTERR", "LOKI", "SAMURAI", "SPIDERMAAN", "CAPIAMERICA",
    "CAPAMERICA", "IRONMANN", "GRUU", "HULKK", "DRSTRANGER",
    "DEADPOOLL", "LOBEZNOO", "FLASHH", "blackpanter", "thor"
]

# Path local esperado para imágenes
images_folder = "images"  # crea esta carpeta y sube ahí los .jpg con los nombres indicados

# Mezclar los nombres de imagen para asignación aleatoria
random.seed()  # semilla por tiempo
shuffled_heroes = hero_names.copy()
random.shuffle(shuffled_heroes)

# Construir lista de image URLs (si existe local -> usar file:, si no -> placeholder)
image_urls = []
for hero in shuffled_heroes:
    filename = f"{hero}.jpg"
    local_path = os.path.join(images_folder, filename)
    if os.path.exists(local_path):
        # usar ruta relativa (funciona si despliegas el repo con archivos estáticos)
        # Streamlit en many deploys no sirve file://, pero al poner path relativo Streamlit lo servirá si está en repo.
        url = local_path
    else:
        # placeholder con texto (codificado)
        text = urllib.parse.quote_plus(f"{hero}")
        url = f"https://via.placeholder.com/600x400/0f2236/ffffff?text={text}"
    image_urls.append((hero, url))

# Asignar aleatoriamente imágenes a proyectos (orden aleatorio ya obtenido)
project_cards = []
for (title, link), (hero, url) in zip(projects, image_urls):
    project_cards.append({
        "title": title,
        "link": link,
        "hero": hero,
        "image": url
    })

# ------------------------
# Header UI
# ------------------------
st.markdown(f"""
<div class="header-box">
  <h1>⌬ Portafolio · Dioses & Tecnología</h1>
  <div style="display:flex; gap:12px; align-items:center; margin-top:6px;">
    <div class="badge">TONOS: Oscuro · Dorado · Azul</div>
    <div style="margin-left:8px;" class="meta">Estética: mitos, dioses, y sistemas — proyectos multimodales · {len(project_cards)} items</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ------------------------
# Mostrar tarjetas en grid 5 columnas
# ------------------------
cols_per_row = 5
rows = (len(project_cards) + cols_per_row - 1) // cols_per_row
idx = 0
for r in range(rows):
    cols = st.columns(cols_per_row, gap="large")
    for c in cols:
        if idx >= len(project_cards):
            break
        card = project_cards[idx]
        title = card["title"]
        link = card["link"]
        hero = card["hero"]
        img = card["image"]

        # Si la url es local path, mostrar con st.image; de lo contrario usar markdown img.
        if img.startswith(images_folder):
            # streamlit image
            with c:
                st.markdown(
                    f"""
                    <div class="card">
                        <img src="{img}" alt="{hero}">
                        <h4>{title}</h4>
                        <p class="meta">Imagen: <strong>{hero}.jpg</strong></p>
                        <a href="{link}" target="_blank">Abrir proyecto ↗</a>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            # placeholder remote
            with c:
                st.markdown(
                    f"""
                    <div class="card">
                        <img src="{img}" alt="{hero}">
                        <h4>{title}</h4>
                        <p class="meta">Imagen placeholder: <strong>{hero}.jpg</strong></p>
                        <a href="{link}" target="_blank">Abrir proyecto ↗</a>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        idx += 1

# ------------------------
# Mapeo actual (información al final)
# ------------------------
st.markdown("---")
st.subheader("📜 Mapeo de imágenes asignadas (aleatorio)")
mapping_md = ""
for i, card in enumerate(project_cards, start=1):
    mapping_md += f"{i}. **{card['title']}** — imagen: **{card['hero']}.jpg** — link: {card['link']}  \n"

st.markdown(mapping_md)

st.markdown("---")
st.markdown(f"<div class='meta'>Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} · Diseñado con tonos dorado y azul · Tema: Dioses & Tecnología</div>", unsafe_allow_html=True)
