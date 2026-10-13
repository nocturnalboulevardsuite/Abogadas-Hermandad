import streamlit as st
import streamlit.components.v1 as components

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
# ESTADO DEL TEMA
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
# PALETA DE COLORES (CREMA CÁLIDO Y DORADO)
# ---------------------------------------------------------
if is_dark:
    bg_app = "#12110E"
    bg_nav = "#181714"
    bg_card = "#1C1A17"
    bg_secondary = "#26231E"
    border_color = "#3A342C"
    text_main = "#F7F4ED"
    text_muted = "#B8B0A1"
    gold_main = "#E5C06A"
    gold_bright = "#FFD700"
    btn_text = "CAMBIAR A TEMA CLARO"
    beam_transform = "rotate(14deg)" # Inclinación suave en modo oscuro
else:
    bg_app = "#FAF6E8"        # Blanco amarillento / crema cálido elegante
    bg_nav = "#FFFFFF"
    bg_card = "#FFFFFF"
    bg_secondary = "#F3EDDF"
    border_color = "#E6DCB8"
    text_main = "#1E1A15"     
    text_muted = "#6B6255"
    gold_main = "#D4AF37"     
    gold_bright = "#E5B80B"   
    btn_text = "CAMBIAR A TEMA OSCURO"
    beam_transform = "rotate(0deg)"  # Balanza recta equilibrada en modo claro

# ---------------------------------------------------------
# ESTILOS CSS DINÁMICOS Y ANIMACIONES DE CARRUSEL
# ---------------------------------------------------------
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600&display=swap');

    [data-testid="stAppViewContainer"], 
    .stApp, body, html {{
        background-color: {bg_app} !important;
        color: {text_main} !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        transition: background-color 0.4s ease, color 0.4s ease;
    }}

    #MainMenu, footer, header, [data-testid="stHeader"] {{
        visibility: hidden !important;
        height: 0px !important;
    }}

    .block-container {{
        padding-top: 5.5rem !important;
        padding-bottom: 4rem !important;
        max-width: 1100px !important;
    }}

    /* NAVBAR FIJO DE LUJO */
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
        transition: background-color 0.4s ease;
    }}

    .nav-brand {{
        display: flex;
        align-items: center;
        gap: 14px;
        font-family: 'Playfair Display', serif;
        font-size: 1.35rem;
        font-weight: 700;
        color: {text_main};
        letter-spacing: 1.5px;
    }}

    .nav-links {{
        display: flex;
        gap: 2.2rem;
        font-size: 0.82rem;
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

    /* CONTENEDOR DE LA BALANZA ANIMADA (SIN CORTES) */
    .theme-wrapper {{
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 1.5rem auto 1rem auto;
        text-align: center;
        overflow: visible !important;
    }}

    /* CENTRADO ABSOLUTO DEL BOTÓN Y SU CONTENEDOR STREAMLIT */
    div[data-testid="stElementContainer"]:has(div[data-testid="stButton"]),
    div[data-testid="stButton"] {{
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        margin: 0 auto !important;
    }}

    div[data-testid="stButton"] > button {{
        background-color: {bg_card} !important;
        color: {text_main} !important;
        border: 1px solid {border_color} !important;
        border-radius: 6px !important;
        padding: 0.75rem 1.8rem !important;
        font-size: 0.82rem !important;
        font-weight: 700 !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        white-space: nowrap !important;
        width: 100% !important;
        max-width: 280px !important;
        cursor: pointer !important;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
        margin: 0 auto !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.02) !important;
        text-align: center !important;
    }}

    div[data-testid="stButton"] > button:hover {{
        border-color: {gold_bright} !important;
        color: {gold_bright} !important;
        transform: scale(1.04) !important;
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.22) !important;
    }}

    .btn-primary > button {{
        background-color: {gold_main} !important;
        color: #FFFFFF !important;
        border: none !important;
        font-size: 0.9rem !important;
        padding: 0.85rem 2.5rem !important;
    }}
    
    .btn-primary > button:hover {{
        background-color: {gold_bright} !important;
        color: #FFFFFF !important;
        transform: scale(1.05) !important;
        box-shadow: 0 8px 25px rgba(212, 175, 55, 0.35) !important;
    }}

    /* HERO BANNER */
    .hero-section {{
        text-align: center;
        padding: 2.5rem 1rem 1rem 1rem;
    }}

    .hero-title {{
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        font-weight: 700;
        color: {text_main};
        line-height: 1.15;
        margin-bottom: 1.5rem;
    }}

    .hero-subtitle {{
        font-size: 1.1rem;
        color: {text_muted};
        max-width: 800px;
        margin: 0 auto 2rem auto;
        line-height: 1.6;
    }}

    .gold-line {{
        width: 60px;
        height: 2px;
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
        transition: background-color 0.4s ease;
    }}
    
    .alert-title {{
        font-weight: 700;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 10px;
    }}

    /* REGLA DE SIMETRÍA 100% RIGUROSA EN CONTENEDORES DE COLUMNA */
    div[data-testid="stHorizontalBlock"] {{
        display: flex !important;
        align-items: stretch !important;
        gap: 1.5rem !important;
    }}

    div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {{
        flex: 1 1 0px !important;
        min-width: 0 !important;
        display: flex !important;
        flex-direction: column !important;
    }}

    div[data-testid="stHorizontalBlock"] > div[data-testid="column"] > div {{
        height: 100% !important;
        display: flex !important;
        flex-direction: column !important;
    }}

    div[data-testid="stHorizontalBlock"] > div[data-testid="column"] .stMarkdown {{
        height: 100% !important;
        display: flex !important;
        flex-direction: column !important;
    }}

    div[data-testid="stHorizontalBlock"] > div[data-testid="column"] .stMarkdown > div {{
        height: 100% !important;
        display: flex !important;
        flex-direction: column !important;
    }}

    /* TARJETAS DENTRO DE COLUMNAS */
    .service-card {{
        background-color: {bg_card};
        border: 1px solid {border_color};
        padding: 2.5rem 1.8rem;
        border-radius: 8px;
        transition: transform 0.4s ease, box-shadow 0.4s ease, border-color 0.4s ease;
        height: 100% !important;
        box-sizing: border-box !important;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        flex: 1 1 auto !important;
    }}

    .service-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.06);
        border-color: {gold_bright};
    }}

    .service-icon {{
        margin-bottom: 1.2rem;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 48px;
        width: 100%;
    }}

    /* TÍTULOS Y DESCRIPCIONES DE TARJETAS */
    .service-title {{
        font-family: 'Playfair Display', serif;
        font-size: 1.35rem;
        font-weight: 600;
        color: {text_main};
        margin-bottom: 1.2rem;
        min-height: 3.6rem;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        line-height: 1.25;
        width: 100%;
    }}

    .service-desc {{
        font-size: 0.92rem;
        color: {text_muted};
        line-height: 1.6;
        margin: 0;
        flex: 1;
        display: flex;
        align-items: center;
        text-align: center;
        width: 100%;
    }}

    /* TARJETA DE EQUIPO / ABOGADA FUNDADORA */
    .team-card {{
        background-color: {bg_card};
        border: 1px solid {border_color};
        padding: 2.5rem;
        border-radius: 8px;
        transition: border-color 0.4s ease, box-shadow 0.4s ease;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }}

    .team-card:hover {{
        border-color: {gold_bright};
        box-shadow: 0 10px 30px rgba(0,0,0,0.06);
    }}

    /* CARRUSEL INFINITO DE CASOS DE ÉXITO (MARQUEE CSS) */
    .marquee-container {{
        overflow: hidden;
        white-space: nowrap;
        width: 100%;
        position: relative;
        padding: 1rem 0;
        mask-image: linear-gradient(to right, transparent, black 8%, black 92%, transparent);
        -webkit-mask-image: linear-gradient(to right, transparent, black 8%, black 92%, transparent);
    }}

    .marquee-track {{
        display: flex;
        gap: 1.8rem;
        width: max-content;
        animation: marqueeScroll 32s linear infinite;
    }}

    .marquee-track:hover {{
        animation-play-state: paused;
    }}

    @keyframes marqueeScroll {{
        0% {{ transform: translateX(0); }}
        100% {{ transform: translateX(-50%); }}
    }}

    .case-card {{
        background-color: {bg_card};
        border: 1px solid {border_color};
        border-top: 3px solid {gold_bright};
        border-radius: 8px;
        padding: 1.8rem;
        width: 340px;
        white-space: normal;
        flex-shrink: 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.02);
        transition: transform 0.3s ease, border-color 0.3s ease;
    }}

    .case-card:hover {{
        transform: translateY(-4px);
        border-color: {gold_bright};
    }}

    .case-badge {{
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        color: {gold_bright};
        background-color: rgba(212, 175, 55, 0.12);
        padding: 4px 10px;
        border-radius: 20px;
        display: inline-block;
        margin-bottom: 0.8rem;
    }}

    .case-title {{
        font-family: 'Playfair Display', serif;
        font-size: 1.15rem;
        font-weight: 700;
        color: {text_main};
        margin-bottom: 0.6rem;
    }}

    .case-detail {{
        font-size: 0.88rem;
        color: {text_muted};
        line-height: 1.5;
    }}

    /* SECCIÓN DE DIPLOMAS Y CERTIFICACIONES */
    .diploma-card {{
        background-color: {bg_card};
        border: 1px solid {border_color};
        border-radius: 8px;
        padding: 1.5rem;
        text-align: center;
        transition: transform 0.4s ease, border-color 0.4s ease;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
    }}

    .diploma-card:hover {{
        transform: scale(1.02);
        border-color: {gold_bright};
    }}

    .diploma-img {{
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 6px;
        border: 1px solid {border_color};
        margin-bottom: 1rem;
    }}

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
# ÍCONOS VECTORIALES PROFESIONALES DE ALTA PRECISIÓN
# ---------------------------------------------------------
nav_logo_svg = f"""<svg width="34" height="34" viewBox="0 0 36 36" fill="none" stroke="{gold_bright}" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="18" r="16" stroke-width="1.5"/><path d="M18 9v18M12 27h12M11 14h14M11 14l-3 8h6l-3-8zM25 14l-3 8h6l-3-8z" stroke-width="1.5"/></svg>"""

# BALANZA PRINCIPAL CON MARGEN AMPLIO Y OVERFLOW LIBRE
main_scale_svg = f"""<svg width="78" height="74" viewBox="-10 -6 84 76" style="overflow: visible !important;" fill="none" stroke="{gold_main}" stroke-linecap="round" stroke-linejoin="round"><path d="M32 10v42M18 52h28M25 52l7-5 7 5" stroke-width="2.5"/><circle cx="32" cy="10" r="3" fill="{gold_main}"/><g style="transform: {beam_transform}; transform-origin: 32px 16px; transition: transform 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);"><path d="M10 16h44" stroke-width="3"/><path d="M32 11v5" stroke-width="2"/><path d="M10 16l-7 18h14l-7-18z" stroke-width="1.5"/><path d="M3 34c0 3.5 3.1 6 7 6s7-2.5 7-6H3z" fill="{gold_main}" fill-opacity="0.25" stroke-width="1.5"/><path d="M54 16l-7 18h14l-7-18z" stroke-width="1.5"/><path d="M47 34c0 3.5 3.1 6 7 6s7-2.5 7-6H47z" fill="{gold_main}" fill-opacity="0.25" stroke-width="1.5"/></g></svg>"""

icon_alert = f"""<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="{gold_bright}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0zM12 9v4M12 17h.01"/></svg>"""

# 1. Escudo de Protección Legal y VIF
icon_shield_pro = f"""<svg width="42" height="42" viewBox="0 0 24 24" fill="none" stroke="{gold_main}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M12 8v7"/><path d="M9 11h6"/><path d="M9 11l-1.5 3h3L9 11z"/><path d="M15 11l-1.5 3h3L15 11z"/></svg>"""

# 2. Sello de Familia e Integridad de Derechos
icon_family_pro = f"""<svg width="42" height="42" viewBox="0 0 24 24" fill="none" stroke="{gold_main}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18z"/><path d="M9 10a2 2 0 1 0 0-4 2 2 0 0 0 0 4z"/><path d="M15 10a2 2 0 1 0 0-4 2 2 0 0 0 0 4z"/><path d="M6.5 16.5v-.5a2.5 2.5 0 0 1 5 0v.5"/><path d="M12.5 16.5v-.5a2.5 2.5 0 0 1 5 0v.5"/></svg>"""

# 3. Maletín Ejecutivo y Tutela Laboral (Ley Karin)
icon_work_pro = f"""<svg width="42" height="42" viewBox="0 0 24 24" fill="none" stroke="{gold_main}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M16 7V4a1 1 0 0 0-1-1h-6a1 1 0 0 0-1 1v3"/><circle cx="12" cy="13.5" r="2.5"/><path d="M12 11v5"/></svg>"""

icon_check = f"""<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#2E8B57" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>"""

icon_mail = f"""<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="{gold_bright}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>"""

icon_phone = f"""<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="{gold_bright}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>"""

# ---------------------------------------------------------
# NAVBAR SUPERIOR
# ---------------------------------------------------------
st.markdown(f"""
    <div class="custom-navbar">
        <div class="nav-brand">
            {nav_logo_svg}
            ABOGADAS HERMANDAD
        </div>
        <div class="nav-links">
            <span>Inicio</span>
            <span>Áreas de Práctica</span>
            <span>Equipo</span>
            <span>Contacto</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# BALANZA Y BOTÓN DE CAMBIO DE TEMA (CENTRADO TOTAL)
# ---------------------------------------------------------
_, col_center, _ = st.columns([1, 1.2, 1])
with col_center:
    st.markdown(f'<div class="theme-wrapper">{main_scale_svg}</div>', unsafe_allow_html=True)
    st.button(btn_text, on_click=toggle_theme, use_container_width=True)

# ---------------------------------------------------------
# HERO PRINCIPAL
# ---------------------------------------------------------
st.markdown(f"""
    <div class="hero-section">
        <div class="gold-line"></div>
        <div class="hero-title">Defensa legal especializada,<br>humana y libre de prejuicios.</div>
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
st.markdown("<h2 style='text-align: center; font-size: 2.5rem; margin: 3rem 0 2.5rem 0;'>Áreas de Especialización</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
        <div class="service-card">
            <div class="service-icon">{icon_shield_pro}</div>
            <div class="service-title">Protección y VIF</div>
            <div class="service-desc">
                Tramitación prioritaria de medidas cautelares de alejamiento, expulsión del agresor del hogar común y querellas criminales por agresiones.
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="service-card">
            <div class="service-icon">{icon_family_pro}</div>
            <div class="service-title">Derecho de Familia</div>
            <div class="service-desc">
                Demandas de pensión de alimentos, retención de fondos (AFP y bancos), cuidado personal, relación directa y regular (visitas) y divorcios.
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="service-card">
            <div class="service-icon">{icon_work_pro}</div>
            <div class="service-title">Acoso Laboral (Ley Karin)</div>
            <div class="service-desc">
                Intervención legal estratégica ante acoso laboral o sexual en el trabajo, tutela de derechos fundamentales y despidos por maternidad.
            </div>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# ---------------------------------------------------------
# ABOGADAS ESPECIALISTAS (SECCIÓN DE EQUIPO)
# ---------------------------------------------------------
st.markdown("<h2 style='text-align: center; font-size: 2.5rem; margin: 3rem 0 2.5rem 0;'>Abogadas Especialistas</h2>", unsafe_allow_html=True)

team_col1, team_col2 = st.columns([1, 2])

with team_col1:
    st.image(
        "fran.jpg", 
        caption="María-Francisca Valentina", 
        use_container_width=True
    )

with team_col2:
    st.markdown(f"""
        <div class="team-card">
            <h3 style="font-size: 2rem; margin-bottom: 0.2rem;">María-Francisca Valentina</h3>
            <p style="color: {gold_bright}; font-weight: 700; font-size: 1.05rem; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 1.2rem;">
                Abogada Fundadora
            </p>
            <p style="color: {text_muted}; line-height: 1.7; font-size: 1.02rem; margin-bottom: 2rem;">
                Abogada especialista en violencia de género, familia, penal y laboral. Compromiso técnico y acompañamiento estratégico para la protección integral de tus derechos.
            </p>
            <div style="border-top: 1px solid {border_color}; padding-top: 1.5rem; display: flex; flex-direction: column; gap: 12px;">
                <div style="display: flex; align-items: center; gap: 12px; font-size: 0.98rem;">
                    {icon_mail} <span style="font-weight: 500;">Lex.Mfrancisca@gmail.com</span>
                </div>
                <div style="display: flex; align-items: center; gap: 12px; font-size: 0.98rem;">
                    {icon_phone} <span style="font-weight: 500;">+56 9 5492 2730</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# ---------------------------------------------------------
# CARRUSEL CONTINUO: CASOS DE ÉXITO Y SENTENCIAS FAVORABLES
# ---------------------------------------------------------
st.markdown("<h2 style='text-align: center; font-size: 2.5rem; margin-top: 3rem; margin-bottom: 0.5rem;'>Casos Destacados & Resoluciones</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1rem; color: #B8B0A1; margin-bottom: 2rem;'>Pasa el cursor sobre una resolución para pausar el carrusel</p>", unsafe_allow_html=True)

cases_html = f"""
    <div class="marquee-container">
        <div class="marquee-track">
            <!-- BLOQUE 1 -->
            <div class="case-card">
                <span class="case-badge">Protección & VIF</span>
                <div class="case-title">Medida Cautelar Urgente 24h</div>
                <div class="case-detail">Otorgamiento inmediato de prohibición de acercamiento y expulsión del agresor del hogar común en el Juzgado de Familia de Santiago.</div>
            </div>
            <div class="case-card">
                <span class="case-badge">Pensión de Alimentos</span>
                <div class="case-title">Retención 100% Fondos AFP</div>
                <div class="case-detail">Cobro efectivo de adeudamiento histórico superior a $14.000.000 mediante retención judicial de fondos de capitalización individual.</div>
            </div>
            <div class="case-card">
                <span class="case-badge">Tutela Laboral</span>
                <div class="case-title">Acoso Laboral (Ley Karin)</div>
                <div class="case-detail">Sentencia favorable con indemnización por vulneración de derechos fundamentales y despido indirecto en sector corporativo.</div>
            </div>
            <div class="case-card">
                <span class="case-badge">Derecho de Familia</span>
                <div class="case-title">Cuidado Personal Definitivo</div>
                <div class="case-detail">Resolución favorable garantizando el interés superior del niño y régimen de visitas estructurado con evaluación psicológica.</div>
            </div>
            <div class="case-card">
                <span class="case-badge">Derecho Penal</span>
                <div class="case-title">Querella por Lesiones VIF</div>
                <div class="case-detail">Condena firme dictada por el Tribunal de Juicio Oral en lo Penal con prohibición absoluta de contacto y resguardo policial.</div>
            </div>
            <!-- BLOQUE DUPLICADO PARA EFECTO INFINITO CONTINUO -->
            <div class="case-card">
                <span class="case-badge">Protección & VIF</span>
                <div class="case-title">Medida Cautelar Urgente 24h</div>
                <div class="case-detail">Otorgamiento inmediato de prohibición de acercamiento y expulsión del agresor del hogar común en el Juzgado de Familia de Santiago.</div>
            </div>
            <div class="case-card">
                <span class="case-badge">Pensión de Alimentos</span>
                <div class="case-title">Retención 100% Fondos AFP</div>
                <div class="case-detail">Cobro efectivo de adeudamiento histórico superior a $14.000.000 mediante retención judicial de fondos de capitalización individual.</div>
            </div>
            <div class="case-card">
                <span class="case-badge">Tutela Laboral</span>
                <div class="case-title">Acoso Laboral (Ley Karin)</div>
                <div class="case-detail">Sentencia favorable con indemnización por vulneración de derechos fundamentales y despido indirecto en sector corporativo.</div>
            </div>
            <div class="case-card">
                <span class="case-badge">Derecho de Familia</span>
                <div class="case-title">Cuidado Personal Definitivo</div>
                <div class="case-detail">Resolución favorable garantizando el interés superior del niño y régimen de visitas estructurado con evaluación psicológica.</div>
            </div>
            <div class="case-card">
                <span class="case-badge">Derecho Penal</span>
                <div class="case-title">Querella por Lesiones VIF</div>
                <div class="case-detail">Condena firme dictada por el Tribunal de Juicio Oral en lo Penal con prohibición absoluta de contacto y resguardo policial.</div>
            </div>
        </div>
    </div>
"""
st.markdown(cases_html, unsafe_allow_html=True)

st.write("---")

# ---------------------------------------------------------
# DIPLOMAS Y CERTIFICACIONES
# ---------------------------------------------------------
st.markdown("<h2 style='text-align: center; font-size: 2.5rem; margin: 3rem 0 2.5rem 0;'>Diplomas & Certificaciones Academicas</h2>", unsafe_allow_html=True)

dip_col1, dip_col2, dip_col3 = st.columns(3)

with dip_col1:
    st.markdown(f"""
        <div class="diploma-card">
            <img src="https://images.unsplash.com/photo-1589829545856-d10d557cf95f?q=80&w=800&auto=format&fit=crop" class="diploma-img" alt="Diploma 1" />
            <h4 style="font-size: 1.1rem; margin-bottom: 0.4rem;">Diplomado en Derecho de Familia</h4>
            <p style="font-size: 0.85rem; color: {gold_bright}; font-weight: 600; margin-bottom: 0.5rem;">UNIVERSIDAD DE CHILE</p>
            <p style="font-size: 0.85rem; color: {text_muted};">Especialización avanzada en litigación oral y medidas cautelares en tribunales de familia.</p>
        </div>
    """, unsafe_allow_html=True)

with dip_col2:
    st.markdown(f"""
        <div class="diploma-card">
            <img src="https://images.unsplash.com/photo-1521791136064-7986c2920216?q=80&w=800&auto=format&fit=crop" class="diploma-img" alt="Diploma 2" />
            <h4 style="font-size: 1.1rem; margin-bottom: 0.4rem;">Certificación Ley Karin y Género</h4>
            <p style="font-size: 0.85rem; color: {gold_bright}; font-weight: 600; margin-bottom: 0.5rem;">PONTIFICIA UNIV. CATÓLICA</p>
            <p style="font-size: 0.85rem; color: {text_muted};">Especialista en prevención, tutela de derechos fundamentales y acoso laboral en Chile.</p>
        </div>
    """, unsafe_allow_html=True)

with dip_col3:
    st.markdown(f"""
        <div class="diploma-card">
            <img src="https://images.unsplash.com/photo-1450133064473-71024230f91b?q=80&w=800&auto=format&fit=crop" class="diploma-img" alt="Diploma 3" />
            <h4 style="font-size: 1.1rem; margin-bottom: 0.4rem;">Postítulo en Derecho Penal & VIF</h4>
            <p style="font-size: 0.85rem; color: {gold_bright}; font-weight: 600; margin-bottom: 0.5rem;">ACADEMIA JUDICIAL / UDP</p>
            <p style="font-size: 0.85rem; color: {text_muted};">Estrategia penal defensiva e interposición de querellas criminales por agresiones graves.</p>
        </div>
    """, unsafe_allow_html=True)

st.write("---")

# ---------------------------------------------------------
# FORMULARIO DE CONSULTA CONFIDENCIAL
# ---------------------------------------------------------
st.markdown("<h2 style='text-align: center; font-size: 2.5rem; margin-top: 3rem; margin-bottom: 0.5rem;'>Agenda tu Consulta Confidencial</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1rem; margin-bottom: 3rem;'>Tus datos están protegidos bajo estricto secreto profesional.</p>", unsafe_allow_html=True)

with st.form("contact_form", clear_on_submit=True):
    fc1, fc2 = st.columns(2)
    
    with fc1:
        nombre = st.text_input("Nombre completo")
        telefono = st.text_input("Teléfono / WhatsApp (+56 9...)")

    with fc2:
        correo = st.text_input("Correo electrónico")
        materia = st.selectbox("Materia de la consulta", [
            "Violencia Intrafamiliar (VIF) / Alejamiento",
            "Pensión de Alimentos / Retención de Fondos",
            "Cuidado Personal / Visitas",
            "Acoso Laboral / Ley Karin",
            "Otra consulta legal"
        ])

    mensaje = st.text_area("Cuéntanos brevemente tu caso (sin tecnicismos legales)")
    
    st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
    submitted = st.form_submit_button("Enviar consulta confidencial")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if submitted:
        if nombre and (telefono or correo):
            st.markdown(f"""
                <div style="background-color: rgba(46, 139, 87, 0.1); border-left: 4px solid #2E8B57; padding: 1rem; color: #2E8B57; font-weight: 600; display: flex; align-items: center; gap: 10px; margin-top: 1rem; border-radius: 4px;">
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

# ---------------------------------------------------------
# SCRIPT DE AUDIO: SINTETIZADOR DE IMPACTO DE MADERA NATURAL
# ---------------------------------------------------------
components.html("""
<script>
    const doc = window.parent.document;
    
    function playWoodClick() {
        const AudioContext = window.parent.AudioContext || window.parent.webkitAudioContext;
        if (!AudioContext) return;
        const ctx = new AudioContext();
        const t = ctx.currentTime;
        
        // 1. Tono principal de la madera
        const osc1 = ctx.createOscillator();
        const gain1 = ctx.createGain();
        osc1.type = 'sine';
        osc1.frequency.setValueAtTime(1050, t);
        osc1.frequency.exponentialRampToValueAtTime(400, t + 0.035);
        
        gain1.gain.setValueAtTime(0.85, t);
        gain1.gain.exponentialRampToValueAtTime(0.001, t + 0.04);
        
        osc1.connect(gain1);
        gain1.connect(ctx.destination);
        
        // 2. Resonancia secundaria del bloque de madera
        const osc2 = ctx.createOscillator();
        const gain2 = ctx.createGain();
        osc2.type = 'sine';
        osc2.frequency.setValueAtTime(1600, t);
        osc2.frequency.exponentialRampToValueAtTime(800, t + 0.02);
        
        gain2.gain.setValueAtTime(0.35, t);
        gain2.gain.exponentialRampToValueAtTime(0.001, t + 0.025);
        
        osc2.connect(gain2);
        gain2.connect(ctx.destination);
        
        // 3. Transitorio percusivo
        const bufferSize = Math.floor(ctx.sampleRate * 0.008);
        const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) {
            data[i] = (Math.random() * 2 - 1) * Math.exp(-i / (bufferSize * 0.25));
        }
        
        const noise = ctx.createBufferSource();
        noise.buffer = buffer;
        
        const filter = ctx.createBiquadFilter();
        filter.type = 'bandpass';
        filter.frequency.setValueAtTime(1300, t);
        filter.Q.setValueAtTime(2.5, t);
        
        const gainNoise = ctx.createGain();
        gainNoise.gain.setValueAtTime(0.5, t);
        gainNoise.gain.exponentialRampToValueAtTime(0.001, t + 0.012);
        
        noise.connect(filter);
        filter.connect(gainNoise);
        gainNoise.connect(ctx.destination);
        
        osc1.start(t);
        osc1.stop(t + 0.045);
        osc2.start(t);
        osc2.stop(t + 0.03);
        noise.start(t);
    }

    if (!doc.bambooListenerAdded) {
        doc.addEventListener('mousedown', function(e) {
            if (e.target.closest('.stButton > button') || e.target.closest('.btn-primary > button')) {
                playWoodClick();
            }
        });
        doc.bambooListenerAdded = true;
    }
</script>
""", height=0, width=0)
