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
    .philosophy-box { 
        background-color: #161b22; 
        padding: 25px; 
        border-radius: 15px; 
        border-left: 5px solid #00d4ff; 
        margin-top: 30px;
    }
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

# Instrucción superior
st.markdown('<div class="nav-instruction">⬅️ Despliega el panel de la izquierda para navegar en la aplicación</div>', unsafe_allow_html=True)

if menu == "Inicio":
    # Encabezado Principal
    st.title("Meteoro-ingeniería")
    
    # Subtítulos de servicios core
    st.markdown("""
    ### • Minería de Datos
    ### • Aprendizaje Desarrollo Software con IA
    ### • Optimización de Flota
    ### • Casos de Análisis
    """)
    
    st.write("---")
    
    # Redacción de Visión y Compromiso
    st.markdown("""
    <div class="philosophy-box">
        <p style="font-size: 1.2rem; line-height: 1.6; color: #ccd6f6;">
        Meteoro ingeniería, ingenieros dedicados a mejorar los procesos con máquinas para reducir costos 
        y optimizar las entregas o producción, necesitamos un mundo más eficiente, con menos desperdicio 
        y menos máquinas extras para hacer lo mismo. 
        <br><br>
        Llegó el momento de que tengas menos máquinas y produzcas más, recibe nuestros análisis 
        y retroalimentación con confidencialidad y exclusividad al que contrate, será nuestro faro 
        en el estudio y recomendaciones.
        </p>
    </div>
    """, unsafe_allow_html=True)

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
        qr_url = "https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://meteoroingenieria.com"
        st.markdown(f'<div style="background-color: white; padding: 10px; border-radius: 10px; display: inline-block;"><img src="{qr_url}"></div>', unsafe_allow_html=True)