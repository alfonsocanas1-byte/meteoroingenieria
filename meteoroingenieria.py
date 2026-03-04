import streamlit as st
import pandas as pd
import json

# Configuración de la página - Identidad Meteoro-ingeniería
st.set_page_config(
    page_title="Meteoro-ingeniería | Eficiencia Industrial",
    page_icon="☄️",
    layout="wide"
)

# --- FUNCIÓN DE VISITAS (Firestore) ---
def gestionar_visitas():
    try:
        from google.cloud import firestore
        if "firestore" in st.secrets:
            # Corrección de la lectura de la llave
            key_dict = json.loads(st.secrets["firestore"]["text_key"])
            db = firestore.Client.from_service_account_info(key_dict)
            doc_ref = db.collection('stats').document('visitas_totales')
            try:
                doc_ref.update({"contador": firestore.Increment(1)})
            except:
                doc_ref.set({"contador": 1})
            res = doc_ref.get().to_dict()
            return res.get("contador", 0)
    except Exception as e:
        return f"Offline ({str(e)[:10]})"
    return "Configurando..."

# Estilos CSS Profesionales
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMarkdown h1, h2, h3 { color: #00d4ff !important; }
    .nav-hint { color: #8892b0; font-size: 0.9rem; font-style: italic; margin-bottom: 20px; }
    .philosophy-box { background-color: #1e293b; padding: 25px; border-radius: 15px; border-left: 5px solid #00d4ff; margin-bottom: 30px; }
    .philosophy-text { color: #ffffff !important; font-size: 1.1rem; line-height: 1.6; }
    .method-card { background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 15px; }
    .method-title { color: #00d4ff; font-weight: bold; font-size: 1.2rem; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Visitas
if 'conteo_ingenieria' not in st.session_state:
    st.session_state.conteo_ingenieria = gestionar_visitas()

# --- SIDEBAR ---
st.sidebar.title("☄️ METEORO-INGENIERÍA")
st.sidebar.metric("Visitas totales", st.session_state.conteo_ingenieria)
st.sidebar.markdown("---")

menu = st.sidebar.radio("Navegación", [
    "Inicio", 
    "Filosofía", 
    "Metodología servicio de minería de datos", 
    "Curso desarrollo software con IA Gemini",
    "Optimización de flota (Mantenimiento Preventivo)",
    "Casos Reales y Análisis",
    "Servicios y pagos"
])

ws_link = "https://wa.me/573122204688?text=Hola%20Meteoro-ingenieria,%20solicito%20información%20sobre%20este%20servicio"

# --- SECCIONES ACTUALIZADAS ---
if menu == "Optimización de flota (Mantenimiento Preventivo)":
    st.title("🚛 Optimización de Flota")
    st.link_button("Solicitar este servicio: 3122204688 📱", ws_link)
    
    # Texto nuevo solicitado
    st.markdown(f"""
    <div class="philosophy-box">
        <p class="philosophy-text">
        En comunicación con ustedes, identificamos las principales razones de varadas o mantenimiento 
        no programado para diseñar una o varias estrategias para reducir el número de paradas 
        y permitir una producción más continua y no requerir maquinaria extra para cumplir 
        con responsabilidades. El mantenimiento preventivo exigente no puede permitir 
        varadas o mantenimientos no programados.
        </p>
    </div>
    """, unsafe_allow_html=True)

elif menu == "Metodología servicio de minería de datos":
    st.title("Metodología de Ingeniería de Datos")
    st.link_button("Solicitar este servicio: 3122204688 📱", ws_link)
    servicios = [
        {"id": 1, "t": "Estructura de costos", "d": "Según los intereses del cliente o por medio de revisión rápida identificar posibles sobre costos."},
        {"id": 2, "t": "Clasificación de costos", "d": "Con inteligencia artificial, clasificar los costos según su monto y prioridad."},
        {"id": 3, "t": "Indicadores de mantenimiento", "d": "Diseñar, estructurar y evaluar indicadores de mantenimiento con producción."},
        {"id": 4, "t": "Cálculo costo ideal", "d": "Con inteligencia artificial, determinar el costo ideal según las condiciones de la empresa, el mercado y el entorno."},
        {"id": 5, "t": "Controles innovadores", "d": "Se proponen controles y proyectos económicos para mejorar el costo y/o producción de la empresa."},
        {"id": 6, "t": "Entrega de la gestión", "d": "Entrega de PDF con todo lo realizado y oportunidades de mejora."},
        {"id": 7, "t": "Seguimiento e implementación", "d": "Acompañamiento en los nuevos controles y proyectos."},
        {"id": 8, "t": "Información del mercado", "d": "Conocimiento vario de los mercados y economía en general."}
    ]
    for item in servicios:
        st.markdown(f'<div class="method-card"><div class="method-title">{item["id"]}. {item["t"]}</div><p style="color: #ccd6f6;">{item["d"]}</p></div>', unsafe_allow_html=True)

elif menu == "Curso desarrollo software con IA Gemini":
    st.title("🚀 Curso de Ingeniería de Software con IA")
    st.link_button("Solicitar este servicio: 3122204688 📱", ws_link)
    puntos = [
        {"id": 1, "t": "Herramientas de desarrollo", "d": "Descargar e instalar el entorno técnico inicial."},
        {"id": 2, "t": "Arquitectura y diseño", "d": "Planificación estructural del software."},
        {"id": 3, "t": "Redacción para IA", "d": "Generación de código inicial mediante prompts avanzados."},
        {"id": 4, "t": "Repositorio web", "d": "Actualización y gestión de código en la nube."},
        {"id": 5, "t": "App en Streamlit", "d": "Creación de la interfaz interactiva."},
        {"id": 6, "t": "Ejecución", "d": "Pruebas y despliegue del software."},
        {"id": 7, "t": "Mejoramiento continuo", "d": "Comunicación con IA para optimizar el producto final."}
    ]
    for p in puntos:
        st.markdown(f'<div class="method-card"><div class="method-title">{p["id"]}. {p["t"]}</div><p style="color: #ccd6f6;">{p["d"]}</p></div>', unsafe_allow_html=True)

# ... (Las demás secciones como Inicio y Filosofía se mantienen según el código previo)