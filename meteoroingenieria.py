import streamlit as st
import pandas as pd
import json

# Configuración de la página - Actualizada a Meteoro-ingeniería
st.set_page_config(
    page_title="Meteoro-ingeniería | Eficiencia Industrial",
    page_icon="☄️",
    layout="wide"
)

# --- FUNCIÓN DE VISITAS (Mantiene conexión con Firestore) ---
def gestionar_visitas():
    try:
        from google.cloud import firestore
        
        if "firestore" in st.secrets:
            # Autenticación con el JSON de los Secrets de Streamlit
            key_dict = json.loads(st.secrets["firestore"]["text_key"])
            db = firestore.Client.from_service_account_info(key_dict)
            
            # Referencia a la colección 'stats' y documento 'visitas_totales'
            doc_ref = db.collection('stats').document('visitas_totales')
            
            # Intento de actualización; si falla (por ser nueva app), crea el registro
            try:
                doc_ref.update({"contador": firestore.Increment(1)})
            except:
                doc_ref.set({"contador": 1})
            
            res = doc_ref.get().to_dict()
            return res.get("contador", 0)
    except Exception as e:
        # Retorna el error simplificado para diagnóstico en la barra lateral
        return f"Offline ({str(e)[:10]})"
    return "Configurando..."

# Estilos CSS de Meteoro-ingeniería (UI/UX Profesional)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMarkdown h1, h2, h3 { color: #00d4ff !important; }
    
    .nav-hint {
        color: #8892b0;
        font-size: 0.9rem;
        font-style: italic;
        margin-bottom: 20px;
    }

    .philosophy-box {
        background-color: #1e293b;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #00d4ff;
        margin-bottom: 30px;
    }
    .philosophy-text {
        color: #ffffff !important;
        font-size: 1.1rem;
        line-height: 1.6;
    }

    .method-card {
        background-color: #161b22;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #30363d;
        margin-bottom: 15px;
    }
    .method-title {
        color: #00d4ff;
        font-weight: bold;
        font-size: 1.2rem;
        margin-bottom: 10px;
    }
    
    .qr-container {
        background-color: white;
        padding: 10px;
        border-radius: 10px;
        display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="nav-hint">Navega en la barra de la izquierda, despliégala</p>', unsafe_allow_html=True)

# Lógica de Visitas (Se ejecuta una vez por sesión)
if 'conteo_ingenieria' not in st.session_state:
    st.session_state.conteo_ingenieria = gestionar_visitas()

# --- SIDEBAR (IDENTIDAD METEORO-INGENIERÍA) ---
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

# --- SECCIONES ACTUALIZADAS ---
if menu == "Inicio":
    col1, col2 = st.columns([1, 4])
    with col1: st.title("☄️") 
    with col2:
        st.title("Meteoro-ingeniería")
        st.subheader("Minería de Datos, Máquinas y Tecnología")
    st.write("---")
    st.write("Meteoro-ingeniería es una solución integral diseñada para transformar la complejidad operativa industrial en eficiencia financiera y técnica.")
    st.info("Especialistas en la salud de los datos y optimización de activos.")

elif menu == "Filosofía":
    st.title("Nuestra Filosofía")
    st.markdown("""
    <div class="philosophy-box">
        <h3 style="color: #ffffff !important;">Nuestra razón de ser</h3>
        <p class="philosophy-text">
        Cuidar la salud de los datos, su custodia y cumplir los propósitos de tu empresa, es nuestra razón de ser en <b>Meteoro-ingeniería</b>. 
        Buscamos la mejora de la eficiencia en todos los sentidos, apoyándonos en la inteligencia artificial para la simulación y 
        aproximación de la realidad de los datos operativos.
        </p>
    </div>
    """, unsafe_allow_html=True)

elif menu == "Metodología servicio de minería de datos":
    st.title("Metodología de Ingeniería de Datos")
    servicios = [
        {"id": 1, "t": "Estructura de Costos", "d": "Investigación técnica con administradores e ingenieros para definir costos críticos en maquinaria industrial."},
        {"id": 2, "t": "Clasificación de Costos", "d": "Categorización técnica y precisa de costos operativos para una minería de datos efectiva."},
        {"id": 3, "t": "Indicadores de Producción y Mantenimiento", "d": "Desarrollo de indicadores de costo de mantenimiento (depreciación, mano de obra, consumibles y repuestos)."},
        {"id": 4, "t": "Cálculo de Costo Aproximado Ideal", "d": "Modelado del costo ideal basado en las características específicas de la operación y el entorno industrial."},
        {"id": 5, "t": "Controles Económicos e Innovadores", "d": "Diseño e implementación de sistemas de control basados en innovación técnica."},
        {"id": 6, "t": "Entrega de Sistema de Gestión", "d": "Estudio técnico final con el análisis de los costos más relevantes para la toma de decisiones estratégicas."}
    ]
    for item in servicios:
        st.markdown(f"""<div class="method-card"><div class="method-title">{item['id']}. {item['t']}</div><p style="color: #ccd6f6;">{item['d']}</p></div>""", unsafe_allow_html=True)

elif menu == "Curso desarrollo software con IA Gemini":
    st.title("🚀 Curso de Ingeniería de Software con IA")
    puntos = [
        "1. Descarga y configuración de herramientas de desarrollo",
        "2. Ingeniería de prompts y comunicación con IA Gemini",
        "3. Primeros desarrollos y lógica de programación",
        "4. Gestión de dominios y arquitectura web",
        "5. Protocolos de pruebas y ensayos",
        "6. Despliegue y salida en vivo (Producción)",
        "7. Resultados y análisis de rendimiento",
        "8. Ciclo de mejora continua"
    ]
    for p in puntos: 
        st.markdown(f'<div class="method-card"><div style="color: #00d4ff; font-weight: bold;">{p}</div></div>', unsafe_allow_html=True)

elif menu == "Optimización de flota (Mantenimiento Preventivo)":
    st.title("🚛 Optimización de Flota")
    st.markdown("""
    <div class="philosophy-box">
        <p class="philosophy-text">
        En <b>Meteoro-ingeniería</b>, nuestra misión es optimizar el mantenimiento preventivo mediante paradas programadas. 
        Esto reduce la dependencia del mantenimiento correctivo, permitiendo operar con menos maquinaria. 
        El resultado: reducción directa en costos de impuestos, seguros y multas, logrando un mayor aprovechamiento de conductores y activos.
        </p>
    </div>
    """, unsafe_allow_html=True)

elif menu == "Casos Reales y Análisis":
    st.title("📂 Ingeniería Aplicada: Casos Reales")
    with st.expander("Control de Relleno de Aceite Hidráulico"): 
        st.info("Digitalización directa para eliminar riesgos de alteración de datos en campo y asegurar la integridad de la información.")
    with st.expander("Mangueras Hidráulicas In-house"): 
        st.write("Transición de compra externa a ensamblaje propio. Compra de rollos y acoples para fabricación a medida en minutos, optimizando tiempos de respuesta.")
        st.success("Impacto: Reducción drástica de tiempos de inactividad de máquina.")

elif menu == "Servicios y pagos":
    st.title("💳 Portafolio de Servicios Meteoro-ingeniería")
    col_info, col_qr = st.columns([2, 1])
    with col_info:
        st.markdown("""
        1. **Ingeniería de Minería de Datos**: Análisis de estructuras de costos.
        2. **Desarrollo de Software con IA**: Capacitación técnica especializada.
        3. **Gestión de Activos y Flotas**: Estrategias de mantenimiento preventivo.
        4. **Capacitación en Control y Riesgos Industriales**.
        """)
        st.write("---")
        st.write("Contacto Directo: **3122204688**")
        st.link_button("Contactar por WhatsApp 📱", "https://wa.me/573122204688?text=Hola%20Meteoro-ingenieria")
    with col_qr:
        st.markdown("### Acceso Directo")
        # El link del QR lo mantengo al actual, o puedes cambiarlo si la nueva app tiene otra URL
        qr_url = "https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://meteoroingenieria.streamlit.app/"
        st.markdown(f'<div class="qr-container"><img src="{qr_url}" alt="QR Code"></div>', unsafe_allow_html=True)

st.sidebar.caption("© 2026 Meteoro-ingeniería | Impulsando la eficiencia en el Universo.")