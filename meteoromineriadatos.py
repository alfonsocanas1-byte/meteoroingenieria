import streamlit as st

def mostrar_metodologia():
    """
    Renderiza la sección de Metodología de Ingeniería de Datos 
    con un diseño de flujo paso a paso para Meteoro-ingeniería.
    """
    st.title("Metodología de Ingeniería de Datos")
    
    # Enlace directo al WhatsApp de Alfonso
    ws_link = "https://wa.me/573122204688?text=Hola%20Meteoro-ingenieria,%20solicito%20información%20sobre%20este%20servicio"
    st.link_button("Solicitar este servicio: 3122204688 📱", ws_link)
    
    st.markdown("---")
    st.subheader("Fases de Implementación Estratégica")

    # Definición de los 8 pilares con indicadores de flujo
    servicios = [
        {"id": 1, "t": "Estructura de costos", "d": "Identificación rápida de posibles sobrecostos según intereses del cliente."},
        {"id": 2, "t": "Clasificación inteligente", "d": "Uso de IA para categorizar costos por monto y prioridad estratégica."},
        {"id": 3, "t": "Indicadores de mantenimiento", "d": "Diseño y evaluación de KPIs vinculados directamente a producción."},
        {"id": 4, "t": "Cálculo de costo ideal", "d": "Determinación del escenario óptimo mediante modelos de IA y entorno de mercado."},
        {"id": 5, "t": "Controles innovadores", "d": "Propuesta de proyectos económicos para potenciar producción y reducir gasto."},
        {"id": 6, "t": "Entrega de gestión", "d": "Documentación técnica (PDF) con hallazgos y oportunidades de mejora detectadas."},
        {"id": 7, "t": "Acompañamiento", "d": "Seguimiento e implementación real de los nuevos controles propuestos."},
        {"id": 8, "t": "Inteligencia de mercado", "d": "Visión global y actualizada de mercados y economía general aplicada al negocio."}
    ]
    
    # Renderizado con flechas de flujo paso a paso
    for i, item in enumerate(servicios):
        # Card del paso
        st.markdown(f"""
            <div style="background-color: #161b22; padding: 20px; border-radius: 10px; border: 2px solid #00d4ff; margin-bottom: 5px;">
                <div style="color: #00d4ff; font-weight: bold; font-size: 1.3rem; margin-bottom: 10px;">
                    PASO {item['id']}: {item['t']}
                </div>
                <p style="color: #ccd6f6; font-size: 1.05rem;">{item['d']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Dibujar flecha si no es el último elemento
        if i < len(servicios) - 1:
            st.markdown("""
                <div style="text-align: center; margin: 10px 0;">
                    <span style="color: #00d4ff; font-size: 2rem; font-weight: bold;">↓↓↓</span>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.info("Este flujo asegura que la salud de sus datos sea el faro de su rentabilidad operativa.")

if __name__ == "__main__":
    st.set_page_config(page_title="Minería de Datos | Meteoro", layout="wide")
    mostrar_metodologia()