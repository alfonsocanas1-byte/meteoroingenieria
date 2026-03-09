import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Meteoro-ingeniería | Hub", layout="wide")

# 2. ESTILOS CSS (Cian brillante sobre Negro para legibilidad en Celular y PC)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMarkdown h1, h2, h3 { color: #00d4ff !important; }
    
    .modulo-inicio { 
        color: #00d4ff !important; 
        font-weight: bold; 
        margin-bottom: 12px;
        font-size: 1.4rem;
    }
    
    .nav-instruction { 
        background-color: #1e293b; 
        padding: 15px; 
        border-radius: 10px; 
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
    
    .card-paso {
        background-color: #161b22; 
        padding: 20px; 
        border-radius: 10px; 
        border: 2px solid #00d4ff; 
        margin-bottom: 5px;
    }
    
    .flecha {
        text-align: center; 
        margin: 10px 0;
        color: #00d4ff; 
        font-size: 2rem; 
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA LATERAL (Navegación del Imperio)
with st.sidebar:
    st.title("🚀 Navegación")
    menu = st.radio(
        "Seleccione un módulo estratégico:",
        ["Inicio", "Minería de Datos", "Software e IA", "Optimización de Flota", "Casos Reales"]
    )
    st.write("---")
    st.info("Meteoro-ingeniería: Transformando datos en activos estratégicos.")

# 4. LÓGICA DE CONTENIDO
if menu == "Inicio":
    st.title("Meteoro-ingeniería")
    st.markdown('<p class="nav-instruction">Bienvenido. Utilice el menú lateral para explorar nuestra capacidad operativa.</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin-top: 20px;">
        <p class="modulo-inicio">🔹 Minería de Datos</p>
        <p class="modulo-inicio">🔹 Desarrollo de Software con IA</p>
        <p class="modulo-inicio">🔹 Optimización de Flota</p>
        <p class="modulo-inicio">🔹 Casos de Análisis Reales</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("""
    <div class="philosophy-box">
        <h3 style="margin-top:0;">Nuestra Misión</h3>
        <p>No solo vemos máquinas; vemos flujos de capital. Utilizamos Minería de Datos e Inteligencia Artificial para que su empresa sea una estructura eficiente, rentable e indestructible.</p>
    </div>
    """, unsafe_allow_html=True)

elif menu == "Minería de Datos":
    st.title("📊 Metodología de Ingeniería de Datos")
    st.link_button("Solicitar este servicio: 3122204688 📱", "https://wa.me/573122204688?text=Información_Minería")
    
    pasos = [
        {"t": "Estructura de costos", "d": "Identificación de sobrecostos según intereses del cliente."},
        {"t": "Clasificación inteligente", "d": "Uso de IA para categorizar costos por prioridad estratégica."},
        {"t": "Indicadores de mantenimiento", "d": "Diseño de KPIs vinculados directamente a producción."},
        {"t": "Cálculo de costo ideal", "d": "Determinación del escenario óptimo mediante modelos de IA."},
        {"t": "Controles innovadores", "d": "Proyectos económicos para potenciar producción."},
        {"t": "Entrega de gestión", "d": "Documentación técnica (PDF) con hallazgos."},
        {"t": "Acompañamiento", "d": "Seguimiento real de los nuevos controles propuestos."},
        {"t": "Inteligencia de mercado", "d": "Visión global aplicada al negocio."}
    ]
    for i, p in enumerate(pasos):
        st.markdown(f'<div class="card-paso"><div style="color:#00d4ff; font-weight:bold;">PASO {i+1}: {p["t"]}</div><p>{p["d"]}</p></div>', unsafe_allow_html=True)
        if i < len(pasos)-1: st.markdown('<div class="flecha">↓↓↓</div>', unsafe_allow_html=True)

elif menu == "Software e IA":
    st.title("🚀 Ingeniería de Software con IA")
    st.link_button("Solicitar este servicio: 3122204688 📱", "https://wa.me/573122204688?text=Información_IA")
    
    puntos = [
        {"t": "Herramientas de desarrollo", "d": "Instalación y configuración técnica inicial."},
        {"t": "Arquitectura y diseño", "d": "Estructuración de software escalable e indestructible."},
        {"t": "Prompt Engineering", "d": "Dominio de Gemini para código eficiente."},
        {"t": "Gestión de Repositorios", "d": "Control de versiones en GitHub y despliegue seguro."},
        {"t": "Ecosistema Streamlit", "d": "Interfaces interactivas para toma de decisiones."},
        {"t": "Ejecución y Pruebas", "d": "Puesta en marcha en entornos reales."},
        {"t": "Mejoramiento Continuo", "d": "Auditoría y potenciación mediante IA."}
    ]
    for i, p in enumerate(puntos):
        st.markdown(f'<div class="card-paso"><div style="color:#00d4ff; font-weight:bold;">PASO {i+1}: {p["t"]}</div><p>{p["d"]}</p></div>', unsafe_allow_html=True)
        if i < len(puntos)-1: st.markdown('<div class="flecha">↓↓↓</div>', unsafe_allow_html=True)

elif menu == "Optimización de Flota":
    st.title("🚛 Optimización de Flota (Preventivo)")
    st.link_button("Solicitar este servicio: 3122204688 📱", "https://wa.me/573122204688?text=Información_Flota")
    
    st.markdown('<div class="philosophy-box">El mantenimiento preventivo exigente no permite varadas.</div>', unsafe_allow_html=True)
    
    flota = [
        {"t": "Análisis de Naturaleza", "d": "Análisis de varadas frecuentes, graves y accidentes."},
        {"t": "Impacto Económico", "d": "Costos de efectos de varadas y necesidad de flota extra."},
        {"t": "Auditoría de Activos", "d": "Revisión de edad, modelos y repuestos originales."},
        {"t": "Diseño de Soluciones", "d": "Mejora técnica para reducción drástica de varadas."},
        {"t": "Socialización", "d": "Presentación de riesgos calculados y oportunidades."},
        {"t": "Entrega Técnica", "d": "Mejoras estratégicas en máquinas en formato PDF."},
        {"t": "Ejecución de Campo", "d": "Seguimiento riguroso de las mejoras aprobadas."}
    ]
    for i, p in enumerate(flota):
        st.markdown(f'<div class="card-paso"><div style="color:#00d4ff; font-weight:bold;">PASO {i+1}: {p["t"]}</div><p>{p["d"]}</p></div>', unsafe_allow_html=True)
        if i < len(flota)-1: st.markdown('<div class="flecha">↓↓↓</div>', unsafe_allow_html=True)

elif menu == "Casos Reales":
    st.title("📂 Casos Reales y Análisis")
    st.link_button("Solicitar asesoría técnica: 3122204688 📱", "https://wa.me/573122204688?text=Información_Casos")
    
    casos = [
        {
            "t": "Control de Aceite Hidráulico", 
            "p": "Pérdida de integridad en información de campo.",
            "s": "Digitalización directa para eliminar error humano.",
            "r": "Decisiones basadas en datos reales e impecables."
        },
        {
            "t": "Gestión de Mangueras In-house", 
            "p": "Altos tiempos de Downtime por proveedores externos.",
            "s": "Transición a ensamblaje propio y rediseño logístico.",
            "r": "Reducción drástica de espera y ahorro inmediato."
        }
    ]
    for i, c in enumerate(casos):
        st.markdown(f"""
            <div class="card-paso">
                <div style="color:#00d4ff; font-weight:bold; font-size:1.2rem;">CASO {i+1}: {c['t']}</div>
                <p style="color:#ff4b4b; font-weight:bold; margin:0;">⚠️ Problema:</p><p>{c['p']}</p>
                <p style="color:#00d4ff; font-weight:bold; margin:0;">🛠️ Solución:</p><p>{c['s']}</p>
                <p style="color:#00ff7f; font-weight:bold; margin:0;">📈 Resultado:</p><p>{c['r']}</p>
            </div>
        """, unsafe_allow_html=True)
        if i < len(casos)-1: st.markdown('<div class="flecha">↓↓↓</div>', unsafe_allow_html=True)