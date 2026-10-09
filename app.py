import streamlit as st

# ---------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA
# ---------------------------------------------------------
st.set_page_config(
    page_title="Abogadas Hermandad | Defensa Legal de la Mujer",
    page_icon="⚖", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# ESTADO DEL TEMA (CLARO CREMA / OSCURO ELEGANTE)
# ---------------------------------------------------------
if "theme_mode" not in st.session_state:
    st.session_state.theme_mode = "light"

def toggle_theme():
    if st.session_state.theme_mode == "light":
        st.session_state.theme_mode = "dark"
    else:
        st.session_state.theme_mode = "light"

is_dark = st.session_state.theme_mode == "dark"

# ---------------------------------------------------------
# VARIABLES DE COLOR (BLANCO AMARILLENTO Y DORADOS BRILLANTES)
# ---------------------------------------------------------
if is_dark:
    bg_app = "#121110"
    bg_nav = "#1A1816"
    bg_card = "#1E1C1A"
    bg_secondary = "#262320"
    border_color = "#3A352F"
    text_main = "#F4F1EA"
    text_muted = "#B8B0A1"
    gold_main = "#E5BE5E"
    gold_bright = "#FFD700"
else:
    bg_app = "#FDFBF7"        # Blanco amarillento muy sutil y elegante
    bg_nav = "#FFFFFF"
    bg_card = "#FFFFFF"
    bg_secondary = "#F5F0E6"
    border_color = "#E6DBC8"
    text_main = "#1C1A17"     # Letras oscuras para que se vean muy bien
    text_muted = "#5C554D"
    gold_main = "#D4AF37"     # Dorado clásico
    gold_bright = "#E5B80B"   # Dorado brillante

# ---------------------------------------------------------
# ESTILOS CSS DINÁMICOS Y ESTRUCTURA DE PÁGINA
# ---------------------------------------------------------
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600&display=swap');

    /* Reset global y forzado de tema */
    [data-testid="stAppViewContainer"], 
    .stApp, body, html {{
        background-color: {bg_app} !important;
        color: {text_main} !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }}

    /* Ocultar elementos nativos de Streamlit */
    #MainMenu, footer, header, [data-testid="stHeader"] {{
        visibility: hidden !important;
        height: 0px !important;
    }}

    .block-container {{
        padding-top: 6rem !important; /* Espacio para el navbar fijo */
        padding-bottom: 4rem !important;
        max-width: 1200px !important;
    }}

    /* NAVBAR FIJO (ESTILO ESTRUCTURADO) */
    .custom-navbar {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 70px;
        background-color: {bg_nav};
        border-bottom: 1px solid {border_color};
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 5%;
        z-index: 999999;
        box-shadow: 0 2px 15px rgba(0,0,0,0.03);
    }}

    .nav-brand {{
        display: flex;
        align-items: center;
        gap: 12px;
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        font-weight: 700;
        color: {text_main};
        letter-spacing: 1px;
    }}

    .nav-links {{
        display: flex;
        gap: 2rem;
        font-size: 0.85rem;
        font-weight: 600;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: {text_main};
    }}
    
    .nav-links span {{
        cursor: pointer;
        transition: color 0.3s;
    }}

    .nav-links span:hover {{
        color: {gold_bright};
    }}

    /* HERO BANNER */
    .hero-section {{
        text-align: center;
        padding: 4rem 1rem;
        background-color: {bg_app};
    }}

    .hero-title {{
        font-family: 'Playfair Display', serif;
        font-size: 3.8rem;
        font-weight: 700;
        color: {text_main};
        line-height: 1.1;
        margin-bottom: 1.5rem;
    }}

    .hero-subtitle {{
        font-size: 1.15rem;
        color: {text_muted};
        max-width: 800px;
        margin: 0 auto 2rem auto;
        line-height: 1.6;
    }}

    .gold-line {{
        width: 80px;
        height: 3px;
        background-color: {gold_bright};
        margin: 0 auto 2rem auto;
    }}

    /* CAJA DE URGENCIA */
    .alert-box {{
        background-color: {bg_secondary};
        border-left: 4px solid {gold_bright};
        padding: 1.5rem 2rem;
        margin: 2rem 0;
        border-radius: 4px;
        color: {text_main};
    }}
    
    .alert-title {{
        font-weight: 700;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 10px;
    }}

    /* TARJETAS DE SERVICIO */
    .service-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.5rem;
    }}

    .service-card {{
        background-color: {bg_card};
        border: 1px solid {border_color};
        padding: 2.5rem 2rem;
        border-radius: 4px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 100%;
    }}

    .service-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        border-color: {gold_main};
    }}

    .service-icon {{
        margin-bottom: 1.5rem;
    }}

    .service-title {{
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        font-weight: 600;
        color: {text_main};
        margin-bottom: 1rem;
    }}

    .service-desc {{
        font-size: 0.95rem;
        color: {text_muted};
        line-height: 1.6;
    }}

    /* BOTONES STREAMLIT */
    .stButton > button {{
        background-color: {bg_app} !important;
        color: {text_main} !important;
        border: 1px solid {border_color} !important;
        border-radius: 0px !important;
        padding: 0.6rem 1.5rem !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        transition: all 0.3s ease !important;
    }}

    .stButton > button:hover {{
        border-color: {gold_bright} !important;
        color: {gold_bright} !important;
    }}

    .btn-primary > button {{
        background-color: {gold_main} !important;
        color: #FFFFFF !important;
        border: none !important;
    }}
    
    .btn-primary > button:hover {{
        background-color: {gold_bright} !important;
        color: #FFFFFF !important;
    }}

    /* TIPOGRAFÍA GLOBAL DE CABECERAS */
    h1, h2, h3, h4 {{
        font-family: 'Playfair Display', serif !important;
        color: {text_main} !important;
    }}
    
    p, label, span {{
        color: {text_main} !important;
    }}
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# ÍCONOS SVG (HTML)
# ---------------------------------------------------------
icon_scale = f"""<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="{gold_bright}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v17M8 21h8M5 7h14M5 7l-3 6h6l-3-6zM19 7l-3 6h6l-3-6z"/></svg>"""
icon_alert = f"""<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="{gold_bright}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0zM12 9v4M12 17h.01"/></svg>"""
icon_shield = f"""<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="{gold_main}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>"""
icon_users = f"""<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="{gold_main}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2M9 7a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg>"""
icon_briefcase = f"""<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="{gold_main}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>"""
icon_check = f"""<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2E8B57" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>"""

# ---------------------------------------------------------
# NAVBAR SUPERIOR FIJO (HTML INYECTADO)
# ---------------------------------------------------------
st.markdown(f"""
    <div class="custom-navbar">
        <div class="nav-brand">
            {icon_scale}
            HERMANDAD
        </div>
        <div class="nav-links">
            <span>Inicio</span>
            <span>Áreas de Práctica</span>
            <span>Equipo</span>
            <span>Contacto</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Botón para cambiar de tema (integrado sutilmente debajo del navbar virtual)
col_spacer, col_theme = st.columns([8, 2])
with col_theme:
    btn_text = "Modo Claro" if is_dark else "Modo Oscuro"
    st.button(btn_text, on_click=toggle_theme, use_container_width=True)

# ---------------------------------------------------------
# SECCIÓN HERO
# ---------------------------------------------------------
st.markdown(f"""
    <div class="hero-section">
        <div class="gold-line"></div>
        <div class="hero-title">Defensa legal especializada, humana y libre de prejuicios.</div>
        <div class="hero-subtitle">
            Te acompañamos con rigor técnico y máxima confidencialidad ante situaciones complejas de violencia intrafamiliar, vulneración de derechos, acoso laboral y conflictos de familia en Chile. Tu tranquilidad jurídica es nuestro compromiso.
        </div>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# ALERTA DE URGENCIA
# ---------------------------------------------------------
st.markdown(f"""
    <div class="alert-box">
        <div class="alert-title">{icon_alert} ¿Enfrentas una situación de riesgo inminente?</div>
        <div style="font-size: 0.95rem; line-height: 1.6; margin-top: 8px;">
            En casos de Violencia Intrafamiliar (VIF) aguda, comunícate directamente al <b>Fono Familia de Carabineros (149)</b> o al <b>1455 (SernamEG)</b>. 
            Para representación legal express e interposición urgente de medidas de protección y alejamiento, cuenta con nuestro equipo.
        </div>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# ---------------------------------------------------------
# ÁREAS DE PRÁCTICA
# ---------------------------------------------------------
st.markdown("<h2 style='text-align: center; font-size: 2.5rem; margin: 3rem 0 2rem 0;'>Áreas de Especialización</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
        <div class="service-card">
            <div class="service-icon">{icon_shield}</div>
            <div class="service-title">Protección VIF y Agresiones</div>
            <div class="service-desc">
                Tramitación prioritaria de medidas cautelares de alejamiento, expulsión del agresor del hogar común, querellas criminales por agresiones físicas, psicológicas y amenazas.
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="service-card">
            <div class="service-icon">{icon_users}</div>
            <div class="service-title">Derecho de Familia</div>
            <div class="service-desc">
                Demandas de pensión de alimentos, retención de fondos (AFP y cuentas bancarias), cuidado personal (tuición), relación directa y regular (visitas) y divorcios.
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="service-card">
            <div class="service-icon">{icon_briefcase}</div>
            <div class="service-title">Acoso Laboral y Ley Karin</div>
            <div class="service-desc">
                Intervención legal estratégica ante acoso laboral, acoso sexual en el trabajo, tutela de derechos fundamentales y despidos injustificados por maternidad o género.
            </div>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# ---------------------------------------------------------
# EQUIPO DIRECTIVO
# ---------------------------------------------------------
st.markdown("<h2 style='text-align: center; font-size: 2.5rem; margin: 3rem 0 2rem 0;'>Nuestra Directora</h2>", unsafe_allow_html=True)

col_img, col_txt = st.columns([1, 2])

with col_img:
    st.markdown(f"""
        <div style="background-color: {bg_secondary}; border: 1px solid {border_color}; min-height: 250px; display: flex; align-items: center; justify-content: center; text-align: center; padding: 2rem;">
            <div>
                <div style="font-family: 'Playfair Display', serif; font-size: 1.8rem; font-weight: 700;">
                    María-Francisca Valentina
                </div>
                <div style="font-size: 0.8rem; color: {gold_bright}; text-transform: uppercase; letter-spacing: 2px; margin-top: 10px; font-weight: 600;">
                    Abogada Litigante
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_txt:
    st.markdown(f"""
        <div style="padding: 1rem 2rem;">
            <h3 style="font-size: 2rem; margin-bottom: 0.5rem; margin-top:0;">Experiencia Relevante</h3>
            <p style="font-size: 1.05rem; line-height: 1.8; color: {text_muted};">
                Especialista en litigación familiar y penal con enfoque de derechos humanos y perspectiva de género en Chile. 
                Fundó <b>Abogadas Hermandad</b> con la visión de ofrecer una defensa técnica de la más alta exigencia, combinada con contención real y transparencia absoluta para cada clienta.
            </p>
            <ul style="font-size: 0.95rem; line-height: 1.8; color: {text_muted}; margin-top: 1rem;">
                <li>Cobertura en la Región Metropolitana y tramitación electrónica en todo Chile.</li>
                <li>Atención presencial previa reserva y reuniones remotas por videollamada cifrada.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# ---------------------------------------------------------
# FORMULARIO DE CONSULTA
# ---------------------------------------------------------
st.markdown("<h2 style='text-align: center; font-size: 2.5rem; margin-bottom: 0.5rem;'>Agenda tu Consulta Confidencial</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1rem; margin-bottom: 3rem;'>Tus datos están protegidos bajo estricto secreto profesional.</p>", unsafe_allow_html=True)

with st.form("contact_form", clear_on_submit=True):
    fc1, fc2 = st.columns(2)
    
    with fc1:
        nombre = st.text_input("Nombre completo")
        telefono = st.text_input("Teléfono / WhatsApp (+56 9...)")
        region = st.selectbox("Región de residencia", [
            "Región Metropolitana", "Valparaíso", "Biobío", "Antofagasta", "Coquimbo", 
            "O'Higgins", "Maule", "La Araucanía", "Los Lagos", "Otra región de Chile"
        ])

    with fc2:
        correo = st.text_input("Correo electrónico")
        materia = st.selectbox("Materia de la consulta", [
            "Violencia Intrafamiliar (VIF) / Alejamiento",
            "Pensión de Alimentos / Retención de Fondos",
            "Cuidado Personal / Visitas",
            "Acoso Laboral / Ley Karin",
            "Derecho Penal / Querellas a Víctimas",
            "Otra consulta legal"
        ])
        horario = st.text_input("Horario preferente de contacto")

    mensaje = st.text_area("Cuéntanos brevemente tu caso (sin tecnicismos legales)")
    
    # Aplicar clase primaria al botón de submit
    st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
    submitted = st.form_submit_button("Enviar consulta confidencial")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if submitted:
        if nombre and (telefono or correo):
            st.markdown(f"""
                <div style="background-color: rgba(46, 139, 87, 0.1); border-left: 4px solid #2E8B57; padding: 1rem; color: #2E8B57; font-weight: 600; display: flex; align-items: center; gap: 10px; margin-top: 1rem;">
                    {icon_check} Tu consulta ha sido enviada con éxito. Te contactaremos a la brevedad.
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Por favor completa tu nombre y al menos un método de contacto (Teléfono o Correo).")

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown(f"""
    <div style="text-align: center; font-size: 0.9rem; color: {text_muted}; padding-top: 4rem; padding-bottom: 2rem;">
        <div class="gold-line" style="width: 40px; margin-bottom: 1.5rem;"></div>
        © 2026 <b>Abogadas Hermandad</b> • Estudio Jurídico de la Mujer en Chile<br>
        <span style="font-style: italic;">Compromiso, Integridad y Defensa Legal Efectiva.</span>
    </div>
""", unsafe_allow_html=True)
