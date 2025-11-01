# -*- coding: utf-8 -*-
"""
Portafolio — tema oscuro / dorado / azul (dioses + tecnología)
Asigna aleatoriamente imágenes .jpg (nombres basados en superhéroes)
a cada proyecto. NO muestra el nombre del archivo de la imagen.
"""

import streamlit as st
import random
import os

# ===========================
# CONFIG
# ===========================
st.set_page_config(page_title="⚡ Portafolio · Samuel Serna Giraldo", page_icon="🛡️", layout="wide")

# Carpeta donde colocas las imágenes .jpg (puede ser "." o "images")
IMAGE_FOLDER = "images"  # cambia si las imágenes están otra carpeta
# Asegúrate de tener archivos: BLACKPANTERR.jpg, LOKI.jpg, ..., thor.jpg (según la lista que diste)

# ===========================
# ESTILOS (oscuro, dorado, azul)
# ===========================
st.markdown(
    """
    <style>
    :root{
      --bg: #070812;         /* muy oscuro */
      --panel: #0f1724;      /* panel oscuro */
      --gold: #C9A84E;       /* dorado suave */
      --blue: #0E3B66;       /* azul profundo */
      --muted: #98AFC7;      /* gris azulado */
      --accent: linear-gradient(90deg, #0E3B66, #C9A84E);
    }
    html, body, .stApp {
      background: radial-gradient(900px 600px at 10% 0%, #071022 0%, var(--bg) 60%);
      color: var(--muted) !important;
      font-family: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }
    .header {
      border: 2px solid rgba(201,168,78,0.12);
      background: linear-gradient(180deg, rgba(14,59,102,0.06), rgba(201,168,78,0.02));
      padding: 20px;
      border-radius: 12px;
      text-align: center;
      box-shadow: 0 6px 30px rgba(2,6,23,0.6);
      margin-bottom: 18px;
    }
    .title {
      color: #E6EEF8;
      font-size: 34px;
      font-weight: 800;
      letter-spacing: 0.6px;
    }
    .subtitle {
      color: var(--gold);
      margin-top: 6px;
      font-size: 14px;
    }
    .card {
      background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
      border: 1px solid rgba(201,168,78,0.06);
      border-radius: 14px;
      padding: 12px;
      transition: transform .18s ease, box-shadow .18s ease;
      box-shadow: 0 6px 18px rgba(2,6,23,0.6);
    }
    .card:hover {
      transform: translateY(-6px);
      box-shadow: 0 12px 30px rgba(2,6,23,0.8);
    }
    .proj-title {
      color: #F6F9FC;
      font-weight: 700;
      margin: 8px 0 6px 0;
      font-size: 16px;
    }
    .proj-link {
      color: var(--gold);
      font-weight: 700;
      text-decoration: none;
    }
    .proj-link:hover { text-decoration: underline; }
    .thumb {
      width: 100%;
      height: 220px;
      object-fit: cover;
      border-radius: 8px;
      border: 1px solid rgba(201,168,78,0.06);
    }
    .grid { gap: 20px; }
    @media (max-width: 900px) {
      .thumb { height: 160px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ===========================
# Cabecera
# ===========================
st.markdown(
    """
    <div class="header">
      <div class="title">⚡ Portafolio — Interfaces Multimodales </div>
      <div class="subtitle">Proyectos multimodales — Samuel Serna Giraldo</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ===========================
# Datos (el usuario los proveyó)
# ===========================
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
    ("Control por Voz + MQTT", "https://ctrlvoice16-10-25voz--iot-y-sistemas-ciberfisicos.streamlit.app/")
]

# ===========================
# Lista de nombres de imagenes (proporcionados)
# Se agregarán .jpg y se asignarán aleatoriamente
# ===========================
hero_names = [
    "BLACKPANTERR","LOKI","SAMURAI","SPIDERMAAN","CAPIAMERICA","CAPAMERICA","IRONMANN",
    "GRUU","HULKK","DRSTRANGER","DEADPOOLL","LOBEZNOO","FLASHH","blackpanter","thor"
]

# Construir rutas de imagen (sin mostrar el nombre en la UI).
# Intentaremos usar IMAGE_FOLDER/<NAME>.jpg; si no existe, intentaremos NAME.jpg en la raíz.
available_images = []
for name in hero_names:
    p1 = os.path.join(IMAGE_FOLDER, f"{name}.jpg")
    p2 = f"{name}.jpg"
    if os.path.exists(p1):
        available_images.append(p1)
    elif os.path.exists(p2):
        available_images.append(p2)
# Si no se encuentran archivos locales, el código seguirá, pero mostrará un placeholder (color).
# Para evitar error, si la carpeta está vacía, crear una lista con None placeholders.
if len(available_images) == 0:
    # No hay imágenes locales detectadas — usaremos placeholders generados (data URLs o colores).
    # Aquí creamos placeholders simples con gradientes CSS (no se muestran nombres)
    use_placeholders = True
else:
    use_placeholders = False

# Asegurar que haya al menos tantas imágenes como proyectos: si fewer, permitimos repetición.
# Mezclar aleatoriamente la lista de imágenes para asignación
if not use_placeholders:
    random.shuffle(available_images)
    # Si hay menos imágenes que proyectos, repetir hasta cubrir
    while len(available_images) < len(projects):
        available_images = available_images + available_images
    assigned_images = available_images[: len(projects)]
else:
    # placeholders: asignar None for each project
    assigned_images = [None] * len(projects)

# ===========================
# Renderizar tarjetas en grid (3 filas x 5 columnas)
# ===========================
cols_per_row = 5
rows = (len(projects) + cols_per_row - 1) // cols_per_row
idx = 0

for r in range(rows):
    cols = st.columns(cols_per_row, gap="large")
    for c in cols:
        if idx >= len(projects):
            break
        title, link = projects[idx]
        image_path = assigned_images[idx]  # path or None
        with c:
            # tarjeta HTML + streamlit elements
            if image_path:
                # usar st.image para que no muestre nombre de archivo
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.image(image_path, use_column_width=True, clamp=True)
                st.markdown(f'<div style="padding-top:8px;"><div class="proj-title">{title}</div>'
                            f'<a class="proj-link" href="{link}" target="_blank">Abrir proyecto</a></div>',
                            unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                # Placeholder: caja con gradiente dorado/azul y título + enlace
                placeholder_html = f"""
                <div class="card" style="display:flex; flex-direction:column; align-items:center; justify-content:flex-start;">
                  <div style="width:100%; height:220px; border-radius:8px;
                              background: linear-gradient(135deg, rgba(14,59,102,0.6), rgba(201,168,78,0.45));
                              display:flex; align-items:center; justify-content:center;">
                    <div style="color: rgba(255,255,255,0.12); font-size:46px; font-weight:800;">⚡</div>
                  </div>
                  <div style="padding-top:10px;">
                    <div class="proj-title">{title}</div>
                    <a class="proj-link" href="{link}" target="_blank">Abrir proyecto</a>
                  </div>
                </div>
                """
                st.markdown(placeholder_html, unsafe_allow_html=True)
        idx += 1

# ===========================
# Footer / créditos
# ===========================
st.markdown("---")
st.markdown(
    """
    <div style="display:flex; justify-content:space-between; align-items:center;">
      <div style="color: #98AFC7;">Tema: Interfaces · Samuel Serna Giralfo</div>
      <div style="color: #C9A84E; font-weight:700;">Portafolio Interfaces Multimodales</div>
    </div>
    """,
    unsafe_allow_html=True,
)
