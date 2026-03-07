import streamlit as st

# Importación de submódulos independientes
from meteoromineriadatos import mostrar_metodologia
from meteorodesarrollosoftware import mostrar_curso_ia
from meteoroflota import mostrar_optimizacion_flota
from meteorocasos import mostrar_casos_reales

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
    .nav-instruction { 
        background-color: #1e293b; 
        padding: 10px; 
        border-radius: 8px; 
        border: 1px solid #00d4ff; 
        color: #00d4ff; 
        font-weight: bold; 
        text-align: center;
        margin-bottom: 25px;
    }
    .qr-container { background-color: white; padding: 10px; border-radius: 10px; display: inline-block; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (PANEL DE NAVEGACIÓN) ---
st.sidebar.title("☄️ METEORO-INGENIERÍA")
st.sidebar.markdown("---")

menu = st.sidebar.radio("Navegación", [
    "Inicio", 
    "Metodología servicio de minería de datos", 
    "Curso desarrollo software con IA Gemini",
    "Optimización de flota (Mantenimiento Preventivo)",
    "Casos Reales y Análisis",
    "Servicios y pagos"
])

st.sidebar.markdown("---")
st.sidebar.caption("© 2026 Meteoro-ingeniería | Universo")

# --- LÓGICA DEL HUB ---

# Instrucción superior presente en todas las secciones
st.markdown('<div class="nav-instruction">⬅️ Despliega el panel de la izquierda para navegar en la aplicación</div>', unsafe_allow_html=True)

if menu == "Inicio":
    col1, col2 = st.columns([1, 4])
    with col1: st.title("☄️") 
    with col2:
        st.title("Meteoro-ingeniería")
        st.subheader("Minería de Datos, Máquinas y Tecnología")
    st.write("---")
    st.write("Meteoro-ingeniería transforma la complejidad operativa industrial en eficiencia financiera.")
    st.info("Especialistas en salud de datos y optimización de activos.")
    
    st.markdown("""
    ### Bienvenid@ al Hub Tecnológico
    Aquí encontrarás soluciones diseñadas para la optimización de procesos industriales 
    y capacitación avanzada en IA. Selecciona un módulo en el menú lateral para comenzar.
    """)

elif menu == "Metodología servicio de minería de datos":
    mostrar_metodologia()

elif menu == "Curso desarrollo software con IA Gemini":
    mostrar_curso_ia()

elif menu == "Optimización de flota (Mantenimiento Preventivo)":
    mostrar_optimizacion_flota()

elif menu == "Casos Reales y Análisis":
    mostrar_casos_reales()

elif menu == "Servicios y pagos":
    st.title("💳 Portafolio y Contacto")
    col_info, col_qr = st.columns([2, 1])
    
    with col_info:
        st.markdown("""
        1. **Minería de Datos**: Estructuración y análisis de costos industriales.
        2. **Desarrollo IA**: Capacitación en creación de software con Gemini.
        3. **Gestión de Flotas**: Estrategias de mantenimiento preventivo exigente.
        4. **Casos de Éxito**: Consultoría basada en resultados reales.
        """)
        st.write("---")
        st.write("Contacto Directo Alfonso: **3122204688**")
        ws_link = "https://wa.me/573122204688?text=Hola%20Meteoro-ingenieria,%20solicito%20información%20comercial"
        st.link_button("Contactar por WhatsApp 📱", ws_link)
        
    with col_qr:
        st.markdown("### Acceso Directo")
        # Generación de QR dinámico hacia el dominio oficial
        qr_url = "https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://meteoroingenieria.com"
        st.markdown(f'<div class="qr-container"><img src="{qr_url}"></div>', unsafe_allow_html=True)