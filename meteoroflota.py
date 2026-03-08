import streamlit as st

def mostrar_optimizacion_flota():
    """
    Renderiza la sección de Optimización de Flota (Mantenimiento Preventivo)
    con diseño de flujo sincronizado para el hub de Meteoro-ingeniería.
    """
    st.title("🚛 Optimización de Flota (Mantenimiento Preventivo)")
    
    # Enlace de contacto directo para asesoría técnica
    ws_link = "https://wa.me/573122204688?text=Hola%20Meteoro-ingenieria,%20solicito%20información%20sobre%20optimización%20de%20flota"
    st.link_button("Solicitar este servicio: 3122204688 📱", ws_link)
    
    # Declaración de principios del servicio (Faro de la estrategia)
    st.markdown(f"""
    <div style="background-color: #1e293b; padding: 25px; border-radius: 15px; border-left: 5px solid #00d4ff; margin-bottom: 30px;">
        <p style="color: #ffffff; font-size: 1.1rem; line-height: 1.6; margin: 0;">
        En comunicación directa con su operación, identificamos las principales causas de varadas 
        o mantenimiento no programado. Diseñamos estrategias para reducir paradas, 
        permitiendo una producción continua y eliminando la necesidad de maquinaria extra. 
        <b>El mantenimiento preventivo exigente no permite varadas.</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Ruta Crítica de Optimización de Activos")

    # Definición del flujo de 7 pasos sincronizado
    pasos_flota = [
        {"id": 1, "t": "Análisis de Naturaleza", "d": "Entender y analizar la naturaleza de las varadas frecuentes, graves y accidentes."},
        {"id": 2, "t": "Impacto Económico", "d": "Analizar los costos de los efectos de las varadas y su impacto en la necesidad de flota adicional."},
        {"id": 3, "t": "Auditoría de Activos", "d": "Revisión de edad de equipos, modelos, proveedores, repuestos originales y homologados."},
        {"id": 4, "t": "Diseño de Soluciones", "d": "Realizar opciones de mejora técnica para la reducción drástica de varadas."},
        {"id": 5, "t": "Socialización Estratégica", "d": "Presentación de opciones de mejora, riesgos calculados y oportunidades detectadas."},
        {"id": 6, "t": "Entrega Técnica", "d": "Entrega en PDF de las mejoras estratégicas en máquinas y componentes."},
        {"id": 7, "t": "Ejecución de Campo", "d": "Seguimiento riguroso e implementación de las mejoras aprobadas."}
    ]
    
    # Renderizado con flechas de flujo sincronizadas (↓↓↓)
    for i, p in enumerate(pasos_flota):
        # Card del paso con diseño de ingeniería
        st.markdown(f"""
            <div style="background-color: #161b22; padding: 20px; border-radius: 10px; border: 2px solid #00d4ff; margin-bottom: 5px;">
                <div style="color: #00d4ff; font-weight: bold; font-size: 1.3rem; margin-bottom: 10px;">
                    PASO {p['id']}: {p['t']}
                </div>
                <p style="color: #ccd6f6; font-size: 1.05rem;">{p['d']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Indicador de flujo visual
        if i < len(pasos_flota) - 1:
            st.markdown("""
                <div style="text-align: center; margin: 10px 0;">
                    <span style="color: #00d4ff; font-size: 2rem; font-weight: bold;">↓↓↓</span>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.info("Lograr que su maquinaria cumpla su responsabilidad al 100% es nuestra prioridad absoluta.")

if __name__ == "__main__":
    st.set_page_config(page_title="Gestión de Flota | Meteoro", layout="wide")
    mostrar_optimizacion_flota()