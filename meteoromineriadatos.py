import streamlit as st

def mostrar_metodologia():
    """
    Renderiza la sección de Metodología de Ingeniería de Datos 
    para el hub de Meteoro-ingeniería.
    """
    st.title("Metodología de Ingeniería de Datos")
    
    # Enlace directo al WhatsApp de Alfonso
    ws_link = "https://wa.me/573122204688?text=Hola%20Meteoro-ingenieria,%20solicito%20información%20sobre%20este%20servicio"
    st.link_button("Solicitar este servicio: 3122204688 📱", ws_link)
    
    # Definición de los 8 pilares del servicio
    servicios = [
        {"id": 1, "t": "Estructura de costos", "d": "Según los intereses del cliente o por medio de revisión rápida identificar posibles sobrecostos."},
        {"id": 2, "t": "Clasificación de costos", "d": "Con inteligencia artificial, clasificar los costos según su monto y prioridad."},
        {"id": 3, "t": "Indicadores de mantenimiento", "d": "Diseñar, estructurar y evaluar indicadores de mantenimiento con producción."},
        {"id": 4, "t": "Cálculo costo ideal", "d": "Con inteligencia artificial, determinar el costo ideal según las condiciones de la empresa, el mercado y el entorno."},
        {"id": 5, "t": "Controles innovadores", "d": "Se proponen controles y proyectos económicos para mejorar el costo y/o producción de la empresa."},
        {"id": 6, "t": "Entrega de la gestión", "d": "Entrega de PDF con todo lo realizado y oportunidades de mejora."},
        {"id": 7, "t": "Seguimiento e implementación", "d": "Acompañamiento en los nuevos controles y proyectos."},
        {"id": 8, "t": "Información relevante del mercado", "d": "Conocimiento vario de los mercados y economía en general."}
    ]
    
    # Renderizado de tarjetas con el estilo visual de Meteoro-ingeniería
    for item in servicios:
        st.markdown(f"""
            <div style="background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 15px;">
                <div style="color: #00d4ff; font-weight: bold; font-size: 1.2rem; margin-bottom: 10px;">
                    {item['id']}. {item['t']}
                </div>
                <p style="color: #ccd6f6;">{item['d']}</p>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    # Permite probar el módulo de forma independiente
    st.set_page_config(page_title="Minería de Datos | Meteoro", layout="wide")
    mostrar_metodologia()