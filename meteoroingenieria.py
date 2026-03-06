import streamlit as st
import pandas as pd

# Configuración de la página - Identidad Meteoro-ingeniería
st.set_page_config(
    page_title="Meteoro-ingeniería | Eficiencia Industrial",
    page_icon="☄️",
    layout="wide"
)

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

# --- SIDEBAR ---
st.sidebar.title("☄️ METEORO-INGENIERÍA")
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

elif menu == "Filosofía":
    st.title("Nuestra Filosofía")
    st.markdown("""<div class="philosophy-box"><p class="philosophy-text">Cuidar la salud de los datos y cumplir los propósitos de tu empresa es nuestra razón de ser.</p></div>""", unsafe_allow_html=True)

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
        {"id": 7, "t": "Seguimiento e implementación", "d": "Acompañamiento en los nuevos controles y proyectos."},
        {"id": 8, "t": "Información relevante del mercado", "d": "Conocimiento vario de los mercados y economía en general."}
    ]
    for item in servicios:
        st.markdown(f'<div class="method-card"><div class="method-title">{item["id"]}. {item["t"]}</div><p style="color: #ccd6f6;">{item["d"]}</p></div>', unsafe_allow_html=True)

elif menu == "Curso desarrollo software con IA Gemini":
    st.title("🚀 Curso de Ingeniería de Software con IA")
    st.link_button("Solicitar este servicio: 3122204688 📱", ws_link)
    puntos = [
        {"id": 1, "t": "Herramientas de desarrollo", "d": "Descargar las herramientas para desarrollar software."},
        {"id": 2, "t": "Arquitectura y diseño", "d": "Arquitectura y diseño de software."},
        {"id": 3, "t": "Redacción para IA", "d": "Redacción para IA para generación de código inicial."},
        {"id": 4, "t": "Repositorio", "d": "Actualización repositorio web."},
        {"id": 5, "t": "Streamlit", "d": "Creación app en Streamlit."},
        {"id": 6, "t": "Ejecución", "d": "Ejecución del software."},
        {"id": 7, "t": "Mejoramiento", "d": "Comunicación con IA para mejoramiento del software."}
    ]
    for p in puntos:
        st.markdown(f'<div class="method-card"><div class="method-title">{p["id"]}. {p["t"]}</div><p style="color: #ccd6f6;">{p["d"]}</p></div>', unsafe_allow_html=True)

elif menu == "Optimización de flota (Mantenimiento Preventivo)":
    st.title("🚛 Optimización de Flota")
    st.link_button("Solicitar este servicio: 3122204688 📱", ws_link)
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

elif menu == "Casos Reales y Análisis":
    st.title("📂 Casos Reales y Análisis")
    st.link_button("Solicitar asesoría: 3122204688 📱", ws_link)
    with st.expander("Control de Aceite Hidráulico"): 
        st.info("Digitalización directa para eliminar la pérdida de integridad en la información de campo.")
    with st.expander("Mangueras Hidráulicas In-house"): 
        st.success("Transición de compra externa a ensamblaje propio para reducir drásticamente los tiempos de inactividad.")

elif menu == "Servicios y pagos":
    st.title("💳 Portafolio Meteoro-ingeniería")
    col_info, col_qr = st.columns([2, 1])
    with col_info:
        st.markdown("""
        1. **Minería de Datos**: Estructuración y análisis de costos industriales.
        2. **Desarrollo IA**: Capacitación en creación de software con Gemini.
        3. **Gestión de Flotas**: Estrategias de mantenimiento preventivo exigente.
        4. **Control y Riesgos**: Proyectos económicos para mejora de producción.
        """)
        st.write("---")
        st.write("Contacto Directo: **3122204688**")
        st.link_button("Pagar / Contactar por WhatsApp 📱", ws_link)
    with col_qr:
        st.markdown("### Acceso Directo")
        qr_url = "https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://meteoroingenieria.streamlit.app/"
        st.markdown(f'<div class="qr-container"><img src="{qr_url}"></div>', unsafe_allow_html=True)

st.sidebar.caption("© 2026 Meteoro-ingeniería | Universo")