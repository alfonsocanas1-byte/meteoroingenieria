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
    .qr-container { background-color: white; padding: 10px; border-radius: 10px; display: inline-block; }
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

# --- SECCIONES ---
if menu == "Inicio":
    col1, col2 = st.columns([1, 4])
    with col1: st.title("☄️") 
    with col2:
        st.title("Meteoro-ingeniería")
        st.subheader("Minería de Datos, Máquinas y Tecnología")
    st.write("---")
    st.write("Meteoro-ingeniería transforma la complejidad operativa industrial en eficiencia financiera.")
    st.info("Especialistas en salud de datos y optimización de activos.")

elif menu == "Metodología servicio de minería de datos":
    st.title("Metodología de Ingeniería de Datos")
    st.link_button("Solicitar este servicio: 3122204688 📱", ws_link)
    servicios = [
        {"id": 1, "t": "Estructura de costos", "d": "Según los intereses del cliente o por medio de revisión rápida identificar posibles sobre costos."},
        {"id": 2, "t": "Clasificación de costos", "d": "Con inteligencia artificial, clasificar los costos según su monto y prioridad."},
        {"id": 3, "t": "Indicadores de mantenimiento", "d": "Diseñar, estructurar y evaluar indicadores de mantenimiento con producción."},
        {"id": 4, "t": "Cálculo costo ideal", "d": "Con inteligencia artificial, determinar el costo ideal según las condiciones de la empresa, el mercado y el entorno."},
        {"id": 5, "t": "Controles innovadores", "d": "Se propone controles y proyectos económicos para mejorar el costo y/o producción de la empresa."},
        {"id": 6, "t": "Entrega de la gestión", "d": "Entrega de PDF con todo lo realizado y oportunidades de mejora."},
        {"id": 7, "t": "Posible contratación para seguimiento e implementación de mejoras", "d": "Acompañamiento en los nuevos controles y proyectos."},
        {"id": 8, "t": "Información relevante del mercado", "d": "Conocimiento vario de los mercados y economía en general."}
    ]
    for item in servicios:
        st.markdown(f'<div class="method-card"><div class="method-title">{item["id"]}. {item["t"]}</div><p style="color: #ccd6f6;">{item["d"]}</p></div>', unsafe_allow_html=True)

elif menu == "Curso desarrollo software con IA Gemini":
    st.title("🚀 Curso de Ingeniería de Software con IA")
    st.link_button("Solicitar este servicio: 3122204688 📱", ws_link)
    
    # Nuevos puntos del curso actualizados
    puntos_curso = [
        {"id": 1, "t": "Descargar las herramientas para desarrollar software", "d": "Instalación y configuración del entorno técnico inicial."},
        {"id": 2, "t": "Arquitectura y diseño de software", "d": "Planificación estructural de la aplicación."},
        {"id": 3, "t": "Redacción para IA para generación de código inicial", "d": "Ingeniería de prompts avanzada para obtener código funcional."},
        {"id": 4, "t": "Actualización repositorio web", "d": "Gestión de versiones y control de código en la nube."},
        {"id": 5, "t": "Creación app en Streamlit", "d": "Desarrollo de la interfaz de usuario interactiva."},
        {"id": 6, "t": "Ejecución del software", "d": "Pruebas de rendimiento y puesta en marcha."},
        {"id": 7, "t": "Comunicación con IA para mejoramiento del software", "d": "Ciclo de retroalimentación para optimización continua."}
    ]
    for p in puntos_curso:
        st.markdown(f'<div class="method-card"><div class="method-title">{p["id"]}. {p["t"]}</div><p style="color: #ccd6f6;">{p["d"]}</p></div>', unsafe_allow_html=True)

elif menu == "Optimización de flota (Mantenimiento Preventivo)":
    st.title("🚛 Optimización de Flota")
    st.link_button("Solicitar este servicio: 3122204688 📱", ws_link)
    st.markdown("""<div class="philosophy-box"><p class="philosophy-text">Optimizamos el mantenimiento preventivo para operar con menos maquinaria, reduciendo costos de seguros y multas.</p></div>""", unsafe_allow_html=True)

# ... (Resto de secciones se mantienen igual)