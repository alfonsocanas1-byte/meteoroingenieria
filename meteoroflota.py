import streamlit as st

def mostrar_optimizacion_flota():
    """
    Renderiza la sección de Optimización de Flota (Mantenimiento Preventivo)
    para el hub de Meteoro-ingeniería.
    """
    st.title("🚛 Optimización de Flota (Mantenimiento Preventivo)")
    
    # Enlace de contacto directo para asesoría técnica
    ws_link = "https://wa.me/573122204688?text=Hola%20Meteoro-ingenieria,%20solicito%20información%20sobre%20optimización%20de%20flota"
    st.link_button("Solicitar este servicio: 3122204688 📱", ws_link)
    
    # Declaración de principios del servicio
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

    # Pilares de la estrategia de flota
    pilares = [
        {"id": "A", "t": "Análisis de Falla", "d": "Identificación de patrones en mantenimientos no programados."},
        {"id": "B", "t": "Estrategia Preventiva", "d": "Diseño de rutinas de inspección para asegurar la continuidad."},
        {"id": "C", "t": "Eficiencia Operativa", "d": "Optimización del uso de activos para reducir costos de repuestos."},
        {"id": "D", "t": "Cero Varadas", "d": "Implementación de controles para que la maquinaria cumpla su responsabilidad al 100%."}
    ]
    
    # Renderizado de los pilares con estética Meteoro
    cols = st.columns(2)
    for i, p in enumerate(pilares):
        with cols[i % 2]:
            st.markdown(f"""
                <div style="background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 15px; height: 160px;">
                    <div style="color: #00d4ff; font-weight: bold; font-size: 1.1rem; margin-bottom: 8px;">
                        Pilar {p['id']}: {p['t']}
                    </div>
                    <p style="color: #ccd6f6; font-size: 0.95rem;">{p['d']}</p>
                </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    # Prueba independiente del módulo
    st.set_page_config(page_title="Gestión de Flota | Meteoro", layout="wide")
    mostrar_optimizacion_flota()