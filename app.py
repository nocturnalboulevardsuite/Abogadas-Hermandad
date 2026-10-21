import base64
import os

import streamlit as st
import streamlit.components.v1 as componentsimport streamlit as st
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


# =========================================================
# CONFIGURACIÓN
# =========================================================
BRAND = "Hermanas Hermandad"
PHONE_DISPLAY = "+56 9 5492 2730"
PHONE_TEL = "+56954922730"
EMAIL = "Lex.Mfrancisca@gmail.com"
WA_LINK = "https://wa.me/56954922730?text=Hola%2C%20quisiera%20agendar%20una%20consulta%20confidencial."

st.set_page_config(
    page_title=f"{BRAND} | Estudio Jurídico de la Mujer",
    page_icon="⚖",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# UTILIDADES
# =========================================================
def html(markup: str) -> None:
    """Renderiza HTML sin sangrías (evita que Markdown lo convierta en bloque de código)."""
    clean = "\n".join(line.strip() for line in markup.splitlines() if line.strip())
    st.markdown(clean, unsafe_allow_html=True)


def image_to_data_uri(path: str):
    if not os.path.exists(path):
        return None
    ext = os.path.splitext(path)[1].lower().lstrip(".") or "jpeg"
    ext = "jpeg" if ext == "jpg" else ext
    with open(path, "rb") as f:
        return f"data:image/{ext};base64,{base64.b64encode(f.read()).decode()}"


# =========================================================
# ESTILOS
# Paleta mate: beige, blanco, dorado envejecido y texto negro.
# Tema oscuro: azul noche mate, dorado y texto blanco.
# Movimiento reservado para la balanza y el interruptor de tema.
# =========================================================
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Inter:wght@400;500;600&display=swap');

:root {
  --bg: #F5F1E8;
  --band: #ECE5D6;
  --surface: #FFFFFF;
  --line: #DDD3C0;
  --line-2: #C8BBA2;
  --ink: #161514;
  --muted: #57524A;
  --gold: #A8843F;
  --gold-d: #85672F;
  --btn: #161514;
  --btn-ink: #FFFFFF;
  --deep: #1E1C19;
  --deep-ink: #F5F1E8;
  --r: 4px;
  --ease: cubic-bezier(.45,0,.2,1);
  --serif: 'Cormorant Garamond', Georgia, 'Times New Roman', serif;
  --sans: 'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --alert-h: 44px;
}
:root[data-theme="dark"] {
  --bg: #12161F;
  --band: #171C27;
  --surface: #1B212D;
  --line: #2B3242;
  --line-2: #3A4356;
  --ink: #FFFFFF;
  --muted: #D2CDC3;
  --gold: #C9A45A;
  --gold-d: #D8B670;
  --btn: #C9A45A;
  --btn-ink: #12161F;
  --deep: #0D1017;
  --deep-ink: #F4F1EA;
}
:root.alert-closed { --alert-h: 0px; }

html, body, .stApp { background: var(--bg) !important; color: var(--ink) !important; font-family: var(--sans) !important;
  -webkit-font-smoothing: antialiased; transition: background-color .8s var(--ease), color .8s var(--ease); }
[data-testid="stAppViewContainer"], [data-testid="stMain"] { background: transparent !important; }
html, [data-testid="stMain"], [data-testid="stAppViewContainer"] { scroll-behavior: smooth; }
#MainMenu, footer, header, [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"] { display: none !important; }
.block-container { padding: calc(var(--alert-h) + 76px) 0 0 !important; max-width: 100% !important; }
[data-testid="stVerticalBlock"] { gap: 0 !important; }
::selection { background: var(--gold); color: #FFFFFF; }
/* Streamlit agrega un ícono de enlace junto a los títulos: se oculta */
[data-testid="stHeaderActionElements"], .stMarkdown h1 > a, .stMarkdown h2 > a, .stMarkdown h3 > a, .stMarkdown h4 > a,
[data-testid="stMarkdownContainer"] h1 a[href^="#"], [data-testid="stMarkdownContainer"] h2 a[href^="#"] { display: none !important; }
[data-testid="stMarkdownContainer"], .stMarkdown, [data-testid="stElementContainer"] { width: 100% !important; max-width: 100% !important; }
[data-testid="stMarkdownContainer"] h1, [data-testid="stMarkdownContainer"] h2, [data-testid="stMarkdownContainer"] h3, [data-testid="stMarkdownContainer"] h4 {
  padding: 0 !important; scroll-margin-top: 0; }
body { text-rendering: optimizeLegibility; }
h1, h2, h3, h4 { font-family: var(--serif) !important; color: var(--ink) !important; font-weight: 600 !important; letter-spacing: -0.005em; margin: 0; }
p { margin: 0; }
a { text-decoration: none !important; color: inherit; }
a:focus-visible, button:focus-visible { outline: 2px solid var(--gold) !important; outline-offset: 3px; }
::view-transition-old(root), ::view-transition-new(root) { animation-duration: .8s; animation-timing-function: var(--ease); }

.wrap { max-width: 1120px; margin: 0 auto; padding: 0 32px; }
.t { transition: background-color .8s var(--ease), border-color .8s var(--ease), color .8s var(--ease); }

/* ---------- Alerta de peligro inminente ---------- */
.alert-bar { position: fixed; top: 0; left: 0; right: 0; height: 44px; z-index: 1000002; isolation: isolate;
  display: flex; align-items: center; justify-content: center; gap: 12px; padding: 0 56px;
  background: #9E1422; color: #FFFFFF; font-size: .86rem; font-weight: 500; }
.alert-bar::before { content: ""; position: absolute; inset: 0; background: #C41E30; z-index: -1; animation: blink 1.2s steps(1, end) infinite; }
@keyframes blink { 50% { opacity: 0; } }
:root.alert-closed .alert-bar { display: none; }
.alert-bar strong { font-weight: 600; color: #FFFFFF; }
.alert-bar span { color: #FFFFFF; }
.alert-bar a { color: #FFFFFF !important; font-weight: 600; border-bottom: 1px solid rgba(255,255,255,.7); padding-bottom: 1px; white-space: nowrap; }
.alert-bar .sep { opacity: .5; }
.alert-close { position: absolute; right: 16px; top: 50%; transform: translateY(-50%); width: 28px; height: 28px; border: 1px solid rgba(255,255,255,.6);
  border-radius: 2px; background: transparent; color: #FFFFFF; font-size: 16px; line-height: 1; cursor: pointer; display: grid; place-items: center; }
.alert-close:hover { background: rgba(255,255,255,.15); }

/* ---------- Encabezado ---------- */
.site-header { position: fixed; top: var(--alert-h); left: 0; right: 0; height: 76px; z-index: 1000001;
  background: var(--surface); border-bottom: 1px solid var(--line); }
.site-header .wrap { height: 100%; display: flex; align-items: center; justify-content: space-between; }
.brand { display: flex; align-items: center; gap: 14px; }
.brand svg { width: 42px; height: 42px; flex-shrink: 0; }
.brand-name { display: block; font-family: var(--serif); font-size: 1.45rem; font-weight: 700; color: var(--ink); line-height: 1; letter-spacing: .02em; }
.brand-sub { display: block; font-size: .7rem; color: var(--muted); margin-top: 5px; letter-spacing: .08em; }
.nav { display: flex; align-items: center; gap: 28px; }
.nav a.nl { font-size: .86rem; font-weight: 500; color: var(--ink); padding: 6px 0; border-bottom: 1px solid transparent; transition: border-color .3s, color .3s; }
.nav a.nl:hover { border-color: var(--gold); color: var(--gold-d); }
.btn { display: inline-flex; align-items: center; gap: 10px; padding: 13px 22px; border-radius: var(--r); font-size: .88rem; font-weight: 600;
  border: 1px solid var(--btn); background: var(--btn); color: var(--btn-ink) !important; transition: background-color .3s, color .3s, border-color .3s; }
.btn:hover { background: var(--gold); border-color: var(--gold); color: #FFFFFF !important; }
.btn.ghost { background: transparent; color: var(--ink) !important; border-color: var(--line-2); }
.btn.ghost:hover { border-color: var(--ink); background: transparent; color: var(--ink) !important; }
.btn svg { stroke: currentColor; }

/* ---------- Portada ---------- */
.hero { background: var(--band); border-bottom: 1px solid var(--line); padding: 64px 0 0; text-align: center; }
.hero .wrap { display: flex; flex-direction: column; align-items: center; text-align: center; }
.hero h1, .hero .lead { text-align: center !important; margin-left: auto !important; margin-right: auto !important; width: 100%; opacity: 1 !important; filter: none !important; }
.scale-wrap { width: 340px; max-width: 80vw; margin: 0 auto; }
.scale-wrap svg { width: 100%; height: auto; display: block; overflow: visible; }
.hero .rule { width: 48px; height: 1px; background: var(--gold); margin: 36px auto 28px; }
.hero h1 { font-size: clamp(2.5rem, 5vw, 4rem) !important; line-height: 1.1 !important; max-width: 20ch; margin: 0 auto 22px !important; color: var(--ink) !important; font-weight: 600 !important; }
.hero h1 em { font-style: italic; font-weight: 500; color: var(--gold-d); }
.hero .lead { font-size: 1.08rem; line-height: 1.75; color: var(--muted); max-width: 40rem; margin: 0 auto 32px !important; }
.hero .actions { display: flex; justify-content: center; flex-wrap: wrap; gap: 12px; margin-bottom: 56px; }
.facts { display: grid; grid-template-columns: repeat(3, 1fr); background: var(--surface); border-top: 1px solid var(--line); }
.facts div { padding: 26px 24px; text-align: center; font-size: .86rem; color: var(--muted); }
.facts div + div { border-left: 1px solid var(--line); }
.facts b { display: block; font-family: var(--serif); font-size: 1.25rem; font-weight: 600; color: var(--ink); margin-bottom: 4px; }

/* Balanza: movimiento al cambiar de tema */
.beam, .pan-l, .pan-r, .fab-beam, .fab-pan-l, .fab-pan-r { transition: transform 1.6s var(--ease); }
.beam { transform-origin: 160px 70px; }
.pan-l { transform-origin: 44px 78px; }
.pan-r { transform-origin: 276px 78px; }
:root[data-theme="dark"] .beam { transform: rotate(-10deg); }
:root[data-theme="dark"] .pan-l, :root[data-theme="dark"] .pan-r { transform: rotate(10deg); }

/* ---------- Secciones ---------- */
.section { padding: 96px 0; border-bottom: 1px solid var(--line); scroll-margin-top: 130px; }
.section.alt { background: var(--surface); }
.split { display: grid; grid-template-columns: 320px 1fr; gap: 64px; }
.sec-title .eyebrow { display: block; font-size: .78rem; font-weight: 600; color: var(--gold-d); letter-spacing: .06em; margin-bottom: 14px; }
.sec-title h2 { font-size: clamp(2rem, 3.4vw, 2.7rem) !important; line-height: 1.1; margin-bottom: 18px; }
.sec-title p { font-size: .98rem; line-height: 1.75; color: var(--muted); }
.sec-title.center { text-align: center; max-width: 40rem; margin: 0 auto 56px; }
.sec-title.center h2, .sec-title.center p { text-align: center !important; }

/* Áreas: filas */
.rows { border-top: 1px solid var(--ink); }
.row { display: grid; grid-template-columns: 48px 1fr; gap: 24px; padding: 30px 0; border-bottom: 1px solid var(--line); }
.row svg { stroke: var(--gold); }
.row h3 { font-size: 1.6rem !important; margin-bottom: 8px; }
.row p { color: var(--muted); line-height: 1.7; font-size: .95rem; margin-bottom: 12px; }
.row .items { font-size: .86rem; color: var(--ink); line-height: 1.7; }
.row .items span + span::before { content: "  /  "; color: var(--line-2); white-space: pre; }

/* Proceso */
.steps { display: grid; grid-template-columns: repeat(3, 1fr); border-top: 1px solid var(--ink); }
.step { padding: 32px 32px 0 0; }
.step + .step { padding-left: 32px; border-left: 1px solid var(--line); }
.step .n { font-family: var(--serif); font-size: 2.4rem; color: var(--gold); line-height: 1; margin-bottom: 18px; }
.step h4 { font-size: 1.4rem !important; margin-bottom: 10px; }
.step p { color: var(--muted); font-size: .94rem; line-height: 1.7; }

/* Equipo */
.team { display: grid; grid-template-columns: 380px 1fr; gap: 64px; align-items: start; }
.portrait { aspect-ratio: 4/5; background: var(--band); border: 1px solid var(--line); padding: 10px; }
.portrait img { width: 100%; height: 100%; object-fit: cover; display: block; filter: saturate(.85); }
.monogram { width: 100%; height: 100%; display: grid; place-items: center; font-family: var(--serif); font-size: 5.5rem; color: var(--gold); background: var(--surface); }
.team .role { font-size: .78rem; font-weight: 600; color: var(--gold-d); letter-spacing: .06em; }
.team h3 { font-size: clamp(2.1rem, 3.6vw, 2.8rem) !important; margin: 10px 0 20px; line-height: 1.08; }
.team .bio { color: var(--muted); line-height: 1.8; font-size: 1rem; margin-bottom: 28px; }
.quote { border-left: 2px solid var(--gold); padding-left: 22px; font-family: var(--serif); font-style: italic; font-size: 1.35rem; line-height: 1.5; color: var(--ink); margin: 0 0 32px; }
.areas-list { display: grid; grid-template-columns: 1fr 1fr; border-top: 1px solid var(--line); margin-bottom: 28px; }
.areas-list div { padding: 12px 0; border-bottom: 1px solid var(--line); font-size: .9rem; }
.contact-line { display: flex; flex-wrap: wrap; gap: 28px; font-size: .92rem; }
.contact-line a { display: inline-flex; align-items: center; gap: 10px; color: var(--ink); border-bottom: 1px solid var(--line-2); padding-bottom: 3px; transition: border-color .3s; }
.contact-line a:hover { border-color: var(--gold); }
.contact-line svg { stroke: var(--gold); }

/* Casos: tabla */
.cases { border-top: 1px solid var(--ink); }
.case { display: grid; grid-template-columns: 200px 1fr 1.4fr; gap: 32px; padding: 26px 0; border-bottom: 1px solid var(--line); align-items: baseline; }
.case .cat { font-size: .8rem; font-weight: 600; color: var(--gold-d); }
.case h4 { font-size: 1.35rem !important; line-height: 1.25; }
.case p { color: var(--muted); font-size: .92rem; line-height: 1.7; }
.note { font-size: .8rem; color: var(--muted); margin-top: 20px; }

/* Formación */
.creds { display: grid; grid-template-columns: repeat(3, 1fr); border: 1px solid var(--line); background: var(--surface); }
.cred { padding: 32px 28px; }
.cred + .cred { border-left: 1px solid var(--line); }
.cred svg { stroke: var(--gold); margin-bottom: 20px; }
.cred small { display: block; font-size: .78rem; font-weight: 600; color: var(--gold-d); margin-bottom: 8px; }
.cred h4 { font-size: 1.35rem !important; line-height: 1.2; margin-bottom: 10px; }
.cred p { color: var(--muted); font-size: .9rem; line-height: 1.7; }

/* Contacto */
.contact-section { padding: 96px 0 72px; }
.contact-panel { background: var(--deep); color: var(--deep-ink); padding: 40px; height: 100%; border-radius: var(--r); }
.contact-panel h3 { color: var(--deep-ink) !important; font-size: 2rem !important; margin-bottom: 14px; }
.contact-panel p { color: rgba(245,241,232,.75); line-height: 1.7; font-size: .95rem; margin-bottom: 28px; }
.c-item { display: block; padding: 16px 0; border-top: 1px solid rgba(245,241,232,.15); color: var(--deep-ink) !important; }
.c-item small { display: block; font-size: .74rem; color: rgba(245,241,232,.6); margin-bottom: 4px; }
.c-item b { font-weight: 500; font-size: 1rem; color: var(--deep-ink); }
.c-item:hover b { color: #C9A45A; }
.c-note { font-size: .8rem; line-height: 1.6; color: rgba(245,241,232,.65); border-top: 1px solid rgba(245,241,232,.15); padding-top: 18px; margin-top: 8px; }

[data-testid="stHorizontalBlock"]:has(.contact-panel) { max-width: 1120px; margin: 0 auto !important; padding: 0 32px; gap: 24px !important; }
[data-testid="stForm"] { background: var(--surface) !important; border: 1px solid var(--line) !important; border-radius: var(--r) !important; padding: 36px !important; }
[data-testid="stForm"] [data-testid="stVerticalBlock"] { gap: 1rem !important; }
[data-testid="stForm"] label p { font-weight: 500 !important; font-size: .84rem !important; color: var(--ink) !important; }
[data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea, [data-baseweb="select"] > div {
  background: var(--bg) !important; color: var(--ink) !important; border-radius: var(--r) !important; border: 1px solid var(--line) !important; font-family: var(--sans) !important; }
[data-testid="stTextInput"] input::placeholder, [data-testid="stTextArea"] textarea::placeholder { color: var(--muted) !important; opacity: .7; }
[data-testid="stTextInput"] input:focus, [data-testid="stTextArea"] textarea:focus { border-color: var(--gold) !important; box-shadow: none !important; }
[data-testid="stTextInput"] > div > div, [data-testid="stTextArea"] > div > div { border: none !important; background: transparent !important; }
[data-baseweb="select"] span, [data-baseweb="select"] div { color: var(--ink) !important; }
[data-baseweb="popover"] ul { background: var(--surface) !important; }
[data-baseweb="popover"] li { color: var(--ink) !important; }
[data-testid="stFormSubmitButton"] > button { width: 100%; border-radius: var(--r) !important; padding: .9rem 2rem !important;
  background: var(--btn) !important; border: 1px solid var(--btn) !important; transition: background-color .3s, border-color .3s !important; }
[data-testid="stFormSubmitButton"] > button p { color: var(--btn-ink) !important; font-weight: 600 !important; }
[data-testid="stFormSubmitButton"] > button:hover { background: var(--gold) !important; border-color: var(--gold) !important; }
[data-testid="stFormSubmitButton"] > button:hover p { color: #FFFFFF !important; }
.success { padding: 14px 16px; border: 1px solid #3F7D58; border-left-width: 3px; color: #3F7D58; font-size: .9rem; font-weight: 500; }

/* Pie */
.site-footer { background: var(--deep); color: rgba(245,241,232,.7); padding: 56px 0 40px; font-size: .86rem; }
.site-footer .wrap { display: grid; grid-template-columns: 1.5fr 1fr 1fr; gap: 40px; }
.site-footer b { display: block; font-family: var(--serif); font-size: 1.5rem; font-weight: 700; color: #F5F1E8; margin-bottom: 8px; }
.site-footer a { color: #F5F1E8; }
.site-footer a:hover { color: #C9A45A; }
.site-footer .wrap > div > div { margin-bottom: 8px; }
.site-footer .legal { max-width: 1120px; margin: 40px auto 0; padding: 20px 32px 0; border-top: 1px solid rgba(245,241,232,.12); font-size: .78rem; }

/* ---------- Interruptor de tema (balanza) ---------- */
.theme-fab { position: fixed; left: 24px; bottom: 24px; z-index: 1000001; width: 62px; height: 62px; border-radius: 50%; padding: 0;
  background: var(--surface); border: 1px solid var(--line-2); cursor: pointer; display: grid; place-items: center;
  box-shadow: 0 6px 18px rgba(0,0,0,.12); transition: background-color .8s var(--ease), border-color .8s var(--ease); }
.theme-fab:hover { border-color: var(--gold); }
.theme-fab svg { width: 40px; height: 40px; overflow: visible; }
.fab-beam { transform-origin: 24px 12px; }
.fab-pan-l { transform-origin: 6px 13px; }
.fab-pan-r { transform-origin: 42px 13px; }
:root[data-theme="dark"] .fab-beam { transform: rotate(-14deg); }
:root[data-theme="dark"] .fab-pan-l, :root[data-theme="dark"] .fab-pan-r { transform: rotate(14deg); }
.theme-fab .tip { position: absolute; left: 74px; white-space: nowrap; background: var(--surface); color: var(--ink); border: 1px solid var(--line);
  font-size: .78rem; font-weight: 500; padding: 7px 12px; border-radius: var(--r); opacity: 0; transition: opacity .3s; pointer-events: none; }
.theme-fab:hover .tip, .theme-fab:focus-visible .tip { opacity: 1; }
.tip-dark, :root[data-theme="dark"] .tip-light { display: none; }
:root[data-theme="dark"] .tip-dark { display: inline; }

.wa { position: fixed; right: 24px; bottom: 24px; z-index: 1000001; width: 56px; height: 56px; border-radius: 50%; background: #25D366;
  display: grid; place-items: center; box-shadow: 0 6px 18px rgba(0,0,0,.18); }

/* Aparición sutil al hacer scroll */
.js .reveal { opacity: 0; transition: opacity .9s var(--ease); }
.js .reveal.in { opacity: 1; }

/* Responsive */
@media (max-width: 960px) {
  .wrap { padding: 0 20px; }
  .nav a.nl { display: none; }
  .brand-sub { display: none; }
  .split, .team { grid-template-columns: 1fr; gap: 36px; }
  .team .portrait { max-width: 360px; }
  .steps, .creds, .facts { grid-template-columns: 1fr; }
  .step, .step + .step { padding: 28px 0; border-left: none; border-bottom: 1px solid var(--line); }
  .cred + .cred, .facts div + div { border-left: none; border-top: 1px solid var(--line); }
  .case { grid-template-columns: 1fr; gap: 8px; }
  .site-footer .wrap { grid-template-columns: 1fr; }
  .section { padding: 72px 0; }
  .alert-bar { font-size: .76rem; justify-content: flex-start; padding: 0 48px 0 14px; }
  .alert-bar .hide-sm { display: none; }
  .theme-fab { width: 54px; height: 54px; left: 16px; bottom: 16px; }
  .theme-fab .tip { display: none; }
  .wa { right: 16px; bottom: 16px; }
  [data-testid="stHorizontalBlock"]:has(.contact-panel) { padding: 0 20px; }
}
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { transition-duration: .01ms !important; animation: none !important; }
  .js .reveal { opacity: 1; }
}
"""
st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)


# =========================================================
# ÍCONOS
# =========================================================
def icon(paths: str, size: int = 26) -> str:
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke-width="1.4" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>')


icon_shield = icon('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>')
icon_family = icon('<circle cx="9" cy="7" r="3"/><circle cx="17" cy="9" r="2.2"/><path d="M3 20v-1a5 5 0 0 1 10 0v1"/><path d="M14 20v-.5a3.5 3.5 0 0 1 7 0v.5"/>')
icon_work = icon('<rect x="3" y="7" width="18" height="13" rx="1.5"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/><path d="M3 13h18"/>')
icon_cap = icon('<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/><path d="M22 9v6"/>', 28)
icon_mail = icon('<rect x="2" y="4" width="20" height="16" rx="1.5"/><polyline points="22,6 12,13 2,6"/>', 17)
icon_phone = icon('<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.79 19.79 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>', 17)
icon_wa = '<svg width="28" height="28" viewBox="0 0 24 24" fill="#FFFFFF" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.25-.46-2.38-1.47-.88-.78-1.47-1.75-1.65-2.05-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.06 2.88 1.21 3.08c.15.2 2.1 3.2 5.08 4.48.71.31 1.26.49 1.69.63.71.23 1.36.2 1.87.12.57-.09 1.75-.72 2-1.41.25-.69.25-1.29.17-1.41-.07-.12-.27-.2-.57-.35zM12.04 21.5a9.45 9.45 0 0 1-4.82-1.32l-.35-.21-3.58.94.96-3.49-.23-.36a9.43 9.43 0 0 1-1.45-5.03c0-5.22 4.25-9.47 9.48-9.47a9.4 9.4 0 0 1 6.7 2.78 9.4 9.4 0 0 1 2.77 6.7c0 5.22-4.25 9.46-9.47 9.46zm8.06-17.53A11.32 11.32 0 0 0 12.04.64C5.76.64.65 5.75.65 12.03c0 2.01.52 3.97 1.52 5.7L.55 23.6l6.02-1.58a11.36 11.36 0 0 0 5.47 1.39c6.28 0 11.39-5.11 11.39-11.39 0-3.04-1.18-5.9-3.34-8.05z"/></svg>'

logo = """<svg viewBox="0 0 48 48" fill="none" aria-hidden="true">
<circle cx="24" cy="24" r="23" style="stroke:var(--gold)" stroke-width="1"/>
<circle cx="24" cy="24" r="19.5" style="stroke:var(--gold)" stroke-width=".5"/>
<g style="stroke:var(--ink)" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round">
<path d="M24 13.5v19.5M19 33.5h10M20.5 33.5l3.5-2.4 3.5 2.4"/><path d="M13 18Q24 16.4 35 18"/>
<path d="M14 18.4l-3 7.2M14 18.4l3 7.2M10 25.6h8c-.4 2-2 3.1-4 3.1s-3.6-1.1-4-3.1z"/>
<path d="M34 18.4l-3 7.2M34 18.4l3 7.2M30 25.6h8c-.4 2-2 3.1-4 3.1s-3.6-1.1-4-3.1z"/></g>
<circle cx="24" cy="12" r="1.4" style="fill:var(--gold)"/></svg>"""

# =========================================================
# BALANZA REALISTA (latón con volumen y sombras)
# =========================================================
BRASS_DEFS = """
<defs>
  <linearGradient id="hhV" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#EBD6A0"/><stop offset=".45" stop-color="#C19A52"/><stop offset="1" stop-color="#7E5F2A"/>
  </linearGradient>
  <linearGradient id="hhH" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#7A5B27"/><stop offset=".32" stop-color="#E4CB8C"/><stop offset=".55" stop-color="#BD9549"/><stop offset="1" stop-color="#6E5122"/>
  </linearGradient>
  <radialGradient id="hhBall" cx=".35" cy=".3" r=".75">
    <stop offset="0" stop-color="#F7E7BA"/><stop offset=".45" stop-color="#C9A257"/><stop offset="1" stop-color="#6E5122"/>
  </radialGradient>
  <radialGradient id="hhBowl" cx=".38" cy=".05" r="1">
    <stop offset="0" stop-color="#EAD39A"/><stop offset=".5" stop-color="#B68D45"/><stop offset="1" stop-color="#5F451C"/>
  </radialGradient>
  <linearGradient id="hhRim" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#F3E2B0"/><stop offset="1" stop-color="#9C7735"/>
  </linearGradient>
  <linearGradient id="hhInner" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#6E5122"/><stop offset="1" stop-color="#A98443"/>
  </linearGradient>
  <radialGradient id="hhShadow" cx=".5" cy=".5" r=".5">
    <stop offset="0" stop-color="#000" stop-opacity=".28"/><stop offset="1" stop-color="#000" stop-opacity="0"/>
  </radialGradient>
</defs>"""


def pan(cx: int, cls: str) -> str:
    return f"""
  <g class="{cls}">
    <circle cx="{cx}" cy="78" r="3.2" fill="none" stroke="#7E5F2A" stroke-width="1.6"/>
    <g stroke="#7A5B27" stroke-width="1.7" stroke-linecap="round" stroke-dasharray="3.2 1.8">
      <path d="M{cx} 81 L{cx - 34} 176"/><path d="M{cx} 81 L{cx} 172"/><path d="M{cx} 81 L{cx + 34} 176"/>
    </g>
    <path d="M{cx - 38} 178 Q{cx - 36} 207 {cx} 209 Q{cx + 36} 207 {cx + 38} 178 Z" fill="url(#hhBowl)"/>
    <path d="M{cx - 26} 186 Q{cx - 22} 200 {cx - 8} 203" fill="none" stroke="#F3E2B0" stroke-opacity=".45" stroke-width="2" stroke-linecap="round"/>
    <ellipse cx="{cx}" cy="178" rx="38" ry="6.5" fill="url(#hhRim)"/>
    <ellipse cx="{cx}" cy="178.6" rx="33" ry="4.4" fill="url(#hhInner)"/>
  </g>"""


main_scale = f"""
<svg viewBox="0 0 320 300" role="img" aria-label="Balanza de la justicia">
  {BRASS_DEFS}
  <ellipse cx="160" cy="286" rx="110" ry="9" fill="url(#hhShadow)"/>
  <rect x="78" y="264" width="164" height="16" rx="2" fill="url(#hhV)"/>
  <rect x="78" y="264" width="164" height="2" fill="#F3E2B0" opacity=".6"/>
  <path d="M100 264 L112 247 H208 L220 264 Z" fill="url(#hhV)"/>
  <rect x="136" y="238" width="48" height="10" rx="2" fill="url(#hhH)"/>
  <path d="M150 238 L153.5 92 H166.5 L170 238 Z" fill="url(#hhH)"/>
  <rect x="145" y="196" width="30" height="7" rx="2" fill="url(#hhH)"/>
  <rect x="147" y="130" width="26" height="6" rx="2" fill="url(#hhH)"/>
  <rect x="143" y="84" width="34" height="9" rx="2" fill="url(#hhH)"/>
  <rect x="156.5" y="50" width="7" height="34" fill="url(#hhH)"/>
  <circle cx="160" cy="44" r="9" fill="url(#hhBall)"/>
  <path d="M160 35 L157.5 24 L160 18 L162.5 24 Z" fill="url(#hhH)"/>
  <g class="beam">
    <path d="M38 66 Q160 57 282 66 L282 75 Q160 67 38 75 Z" fill="url(#hhV)"/>
    <path d="M42 67 Q160 59 278 67" fill="none" stroke="#F6E6B8" stroke-opacity=".55" stroke-width="1.2"/>
    <circle cx="34" cy="70.5" r="6.5" fill="url(#hhBall)"/>
    <circle cx="286" cy="70.5" r="6.5" fill="url(#hhBall)"/>
    <circle cx="160" cy="70" r="11" fill="url(#hhBall)"/>
    <circle cx="160" cy="70" r="3.4" fill="#5F451C"/>
    {pan(44, "pan-l")}
    {pan(276, "pan-r")}
  </g>
</svg>"""

fab_scale = """
<svg viewBox="0 0 48 48" aria-hidden="true">
  <defs>
    <linearGradient id="fbV" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E8D19A"/><stop offset="1" stop-color="#8A6A2E"/></linearGradient>
    <linearGradient id="fbH" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7A5B27"/><stop offset=".4" stop-color="#E4CB8C"/><stop offset="1" stop-color="#6E5122"/></linearGradient>
  </defs>
  <rect x="15" y="42" width="18" height="3" rx="1" fill="url(#fbV)"/>
  <path d="M22.6 42 L23.2 11 H24.8 L25.4 42 Z" fill="url(#fbH)"/>
  <circle cx="24" cy="8.5" r="2.2" fill="url(#fbV)"/>
  <g class="fab-beam">
    <path d="M4 11.2 Q24 9 44 11.2 L44 13 Q24 11 4 13 Z" fill="url(#fbV)"/>
    <circle cx="24" cy="12" r="2.4" fill="url(#fbV)"/>
    <g class="fab-pan-l"><path d="M6 13 L1 26 M6 13 L11 26" stroke="#7A5B27" stroke-width=".9"/>
      <path d="M0 26 Q.6 31 6 31.4 Q11.4 31 12 26 Z" fill="url(#fbV)"/><ellipse cx="6" cy="26" rx="6" ry="1.2" fill="#E8D19A"/></g>
    <g class="fab-pan-r"><path d="M42 13 L37 26 M42 13 L47 26" stroke="#7A5B27" stroke-width=".9"/>
      <path d="M36 26 Q36.6 31 42 31.4 Q47.4 31 48 26 Z" fill="url(#fbV)"/><ellipse cx="42" cy="26" rx="6" ry="1.2" fill="#E8D19A"/></g>
  </g>
</svg>"""

# =========================================================
# ALERTA, ENCABEZADO Y BOTONES FIJOS
# =========================================================
html(f"""
<div class="alert-bar" role="alert">
  <span><strong>¿Estás en peligro inminente?</strong> <span class="hide-sm">Llama de inmediato al</span></span>
  <a href="tel:149">149 Fono Familia Carabineros</a>
  <span class="sep hide-sm">·</span><a class="hide-sm" href="tel:133">133 Carabineros</a>
  <span class="sep hide-sm">·</span><a class="hide-sm" href="tel:1455">1455 SernamEG</a>
  <button class="alert-close" type="button" data-close-alert aria-label="Cerrar aviso">×</button>
</div>
<header class="site-header t">
  <div class="wrap">
    <a class="brand" href="#inicio" data-scroll="inicio" aria-label="{BRAND}, ir al inicio">{logo}
      <span><span class="brand-name">{BRAND}</span><span class="brand-sub">Estudio jurídico de la mujer</span></span></a>
    <nav class="nav" aria-label="Navegación principal">
      <a class="nl" href="#areas" data-scroll="areas">Áreas de práctica</a>
      <a class="nl" href="#equipo" data-scroll="equipo">Equipo</a>
      <a class="nl" href="#casos" data-scroll="casos">Casos</a>
      <a class="btn" href="#contacto" data-scroll="contacto">Agendar consulta</a>
    </nav>
  </div>
</header>
<button class="theme-fab" type="button" data-theme-toggle aria-label="Cambiar entre tema claro y oscuro" aria-pressed="false">
  {fab_scale}<span class="tip"><span class="tip-light">Tema oscuro</span><span class="tip-dark">Tema claro</span></span>
</button>
<a class="wa" href="{WA_LINK}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp">{icon_wa}</a>
""")

# =========================================================
# PORTADA
# =========================================================
html(f"""
<section class="hero t" id="inicio">
  <div class="wrap">
    <div class="scale-wrap">{main_scale}</div>
    <div class="rule"></div>
    <h1>Defensa legal especializada, <em>humana y sin prejuicios.</em></h1>
    <p class="lead">Representamos a mujeres en violencia intrafamiliar, derecho de familia y acoso laboral, con rigor técnico, absoluta confidencialidad y explicaciones claras en cada etapa del proceso.</p>
    <div class="actions">
      <a class="btn" href="#contacto" data-scroll="contacto">Agendar consulta confidencial</a>
      <a class="btn ghost" href="tel:{PHONE_TEL}">{icon_phone}<span>{PHONE_DISPLAY}</span></a>
    </div>
  </div>
  <div class="facts t">
    <div><b>Confidencialidad</b>Protegida por secreto profesional</div>
    <div><b>Medidas urgentes</b>Tramitación prioritaria en casos VIF</div>
    <div><b>Atención</b>Online y presencial en todo Chile</div>
  </div>
</section>
""")

# =========================================================
# ÁREAS DE PRÁCTICA
# =========================================================
areas = [
    (icon_shield, "Protección y violencia intrafamiliar",
     "Tramitación prioritaria de medidas cautelares y acciones penales para resguardar tu integridad y la de tu familia.",
     ["Prohibición de acercamiento", "Salida del agresor del hogar", "Querellas por lesiones"]),
    (icon_family, "Derecho de familia",
     "Representación en los procesos que definen el bienestar de tus hijos y la estabilidad de tu hogar.",
     ["Pensión de alimentos", "Retención de fondos AFP", "Cuidado personal y visitas", "Divorcio"]),
    (icon_work, "Acoso laboral y Ley Karin",
     "Intervención estratégica ante acoso laboral o sexual y vulneración de derechos fundamentales en el trabajo.",
     ["Tutela de derechos", "Despido indirecto", "Despido por maternidad"]),
]
rows = "".join(
    f"""<div class="row">{ic}<div><h3>{t}</h3><p>{d}</p><div class="items">{''.join(f'<span>{x}</span>' for x in items)}</div></div></div>"""
    for ic, t, d, items in areas
)
steps = [
    ("Primera reunión", "Nos cuentas tu situación con total reserva. Evaluamos riesgos, plazos y alternativas reales."),
    ("Estrategia", "Te proponemos un plan de acción concreto, con etapas y honorarios explicados con claridad."),
    ("Representación", "Llevamos tu causa ante tribunales y te informamos de cada avance relevante."),
]
steps_html = "".join(
    f'<div class="step"><div class="n">{i + 1:02d}</div><h4>{t}</h4><p>{d}</p></div>' for i, (t, d) in enumerate(steps)
)
html(f"""
<section class="section t" id="areas">
  <div class="wrap split">
    <div class="sec-title reveal">
      <span class="eyebrow">Áreas de práctica</span>
      <h2>Especialización en los derechos de la mujer</h2>
      <p>Tres áreas de ejercicio con un mismo método: estrategia jurídica precisa y acompañamiento cercano durante todo el proceso.</p>
    </div>
    <div class="rows reveal">{rows}</div>
  </div>
</section>
<section class="section alt t" id="proceso">
  <div class="wrap">
    <div class="sec-title center reveal">
      <span class="eyebrow">Cómo trabajamos</span>
      <h2>Un proceso claro desde el primer día</h2>
      <p>Sabrás en todo momento en qué etapa está tu causa y cuál es el siguiente paso.</p>
    </div>
    <div class="steps reveal">{steps_html}</div>
  </div>
</section>
""")

# =========================================================
# EQUIPO
# =========================================================
photo = image_to_data_uri("fran.jpg")
portrait = (f'<img src="{photo}" alt="Retrato de María-Francisca Valentina" />'
            if photo else '<div class="monogram">MF</div>')
html(f"""
<section class="section t" id="equipo">
  <div class="wrap team">
    <div class="portrait t reveal">{portrait}</div>
    <div class="reveal">
      <span class="role">Abogada fundadora</span>
      <h3>María-Francisca Valentina</h3>
      <p class="bio">Especialista en violencia de género, derecho de familia, penal y laboral. Combina litigación técnica con un acompañamiento humano para la protección integral de los derechos de sus clientas.</p>
      <blockquote class="quote">Ninguna mujer debería enfrentar sola un proceso judicial. Mi trabajo es que tengas claridad y respaldo en cada decisión.</blockquote>
      <div class="areas-list"><div>Violencia de género</div><div>Derecho de familia</div><div>Derecho penal</div><div>Derecho laboral</div></div>
      <div class="contact-line">
        <a href="mailto:{EMAIL}">{icon_mail}<span>{EMAIL}</span></a>
        <a href="tel:{PHONE_TEL}">{icon_phone}<span>{PHONE_DISPLAY}</span></a>
      </div>
    </div>
  </div>
</section>
""")

# =========================================================
# CASOS Y FORMACIÓN
# =========================================================
cases = [
    ("Protección y VIF", "Medida cautelar en 24 horas",
     "Prohibición de acercamiento y salida del agresor del hogar común, otorgadas por el Juzgado de Familia de Santiago."),
    ("Pensión de alimentos", "Retención de fondos AFP",
     "Cobro de una deuda histórica superior a $14.000.000 mediante retención judicial de fondos previsionales."),
    ("Tutela laboral", "Acoso laboral, Ley Karin",
     "Sentencia favorable con indemnización por vulneración de derechos fundamentales y despido indirecto."),
    ("Derecho de familia", "Cuidado personal definitivo",
     "Resolución que resguarda el interés superior del niño, con régimen de visitas y evaluación psicológica."),
    ("Derecho penal", "Querella por lesiones VIF",
     "Condena firme del Tribunal de Juicio Oral en lo Penal con prohibición absoluta de contacto."),
]
cases_html = "".join(
    f'<div class="case"><span class="cat">{c}</span><h4>{t}</h4><p>{d}</p></div>' for c, t, d in cases
)
creds = [
    ("Universidad de Chile", "Diplomado en Derecho de Familia", "Litigación oral y medidas cautelares en tribunales de familia."),
    ("Pontificia Universidad Católica", "Certificación en Ley Karin y género", "Prevención, tutela de derechos fundamentales y acoso laboral."),
    ("Academia Judicial / UDP", "Postítulo en Derecho Penal y VIF", "Estrategia penal y querellas por agresiones graves."),
]
creds_html = "".join(
    f'<div class="cred">{icon_cap}<small>{inst}</small><h4>{t}</h4><p>{d}</p></div>' for inst, t, d in creds
)
html(f"""
<section class="section alt t" id="casos">
  <div class="wrap split">
    <div class="sec-title reveal">
      <span class="eyebrow">Resultados</span>
      <h2>Casos destacados</h2>
      <p>Algunas resoluciones obtenidas para nuestras clientas, presentadas de forma anónima.</p>
    </div>
    <div class="reveal">
      <div class="cases">{cases_html}</div>
      <p class="note">Los resultados anteriores no garantizan resultados futuros. Cada caso se evalúa de forma individual.</p>
    </div>
  </div>
</section>
<section class="section t" id="formacion">
  <div class="wrap">
    <div class="sec-title center reveal">
      <span class="eyebrow">Formación académica</span>
      <h2>Preparación que respalda tu defensa</h2>
      <p>Especialización continua en las materias que defendemos ante tribunales.</p>
    </div>
    <div class="creds t reveal">{creds_html}</div>
  </div>
</section>
<section class="contact-section" id="contacto">
  <div class="wrap">
    <div class="sec-title center reveal">
      <span class="eyebrow">Contacto</span>
      <h2>Agenda tu consulta confidencial</h2>
      <p>Cuéntanos lo esencial. Te respondemos personalmente por el medio que prefieras.</p>
    </div>
  </div>
</section>
""")

# =========================================================
# CONTACTO
# =========================================================
col_info, col_form = st.columns([1, 1.5])

with col_info:
    html(f"""
    <div class="contact-panel t">
      <h3>Hablemos con reserva</h3>
      <p>La primera conversación sirve para entender tu situación y explicarte tus opciones, sin compromiso.</p>
      <a class="c-item" href="tel:{PHONE_TEL}"><small>Teléfono y WhatsApp</small><b>{PHONE_DISPLAY}</b></a>
      <a class="c-item" href="mailto:{EMAIL}"><small>Correo electrónico</small><b>{EMAIL}</b></a>
      <a class="c-item" href="tel:149"><small>Emergencias VIF</small><b>149 Fono Familia · 1455 SernamEG</b></a>
      <p class="c-note">Todo lo que compartas está protegido por secreto profesional y no se comparte con terceros.</p>
    </div>
    """)

with col_form:
    with st.form("contact_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            nombre = st.text_input("Nombre completo", placeholder="Tu nombre")
            telefono = st.text_input("Teléfono o WhatsApp", placeholder="+56 9 ...")
        with c2:
            correo = st.text_input("Correo electrónico", placeholder="nombre@correo.cl")
            materia = st.selectbox("Materia", [
                "Violencia intrafamiliar / Medidas de protección",
                "Pensión de alimentos / Retención de fondos",
                "Cuidado personal / Visitas",
                "Acoso laboral / Ley Karin",
                "Otra consulta legal",
            ])
        mensaje = st.text_area("Describe brevemente tu caso", placeholder="No necesitas usar términos legales.", height=140)
        submitted = st.form_submit_button("Enviar consulta confidencial")

        if submitted:
            if nombre and (telefono or correo):
                html('<div class="success">Consulta enviada. Te contactaremos a la brevedad.</div>')
            else:
                st.error("Indica tu nombre y al menos un medio de contacto (teléfono o correo) para poder responderte.")

# =========================================================
# PIE DE PÁGINA
# =========================================================
html(f"""
<div style="height:72px"></div>
<footer class="site-footer">
  <div class="wrap">
    <div><b>{BRAND}</b><div>Estudio jurídico de la mujer en Chile.</div></div>
    <div><div><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div><div><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
    <div><div><a href="#areas" data-scroll="areas">Áreas de práctica</a></div><div><a href="#equipo" data-scroll="equipo">Equipo</a></div><div><a href="#contacto" data-scroll="contacto">Agendar consulta</a></div></div>
  </div>
  <div class="legal">© 2026 {BRAND}. Todos los derechos reservados.</div>
</footer>
""")

# =========================================================
# INTERACCIONES (tema, aviso, scroll suave y aparición sutil)
# =========================================================
components.html("""
<script>
(function () {
  const win = window.parent, doc = win.document, root = doc.documentElement;
  const reduce = win.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const get = (s, k) => { try { return win[s].getItem(k); } catch (e) { return null; } };
  const set = (s, k, v) => { try { win[s].setItem(k, v); } catch (e) {} };

  if (!root.getAttribute('data-theme')) root.setAttribute('data-theme', get('localStorage', 'hh-theme') || 'light');
  doc.querySelectorAll('[data-theme-toggle]').forEach(b => b.setAttribute('aria-pressed', root.getAttribute('data-theme') === 'dark'));
  if (get('sessionStorage', 'hh-alert') === 'closed') root.classList.add('alert-closed');
  root.classList.add('js');

  if (!win.__hhIO) {
    win.__hhIO = new win.IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('in'); win.__hhIO.unobserve(e.target); }
    }), { threshold: 0.12 });
  }
  const observe = () => doc.querySelectorAll('.reveal:not(.in)').forEach(el => reduce ? el.classList.add('in') : win.__hhIO.observe(el));
  observe();
  setTimeout(() => doc.querySelectorAll('.reveal:not(.in)').forEach(el => {
    const r = el.getBoundingClientRect(); if (r.top < win.innerHeight) el.classList.add('in');
  }), 1200);
  if (!win.__hhMO) { win.__hhMO = new win.MutationObserver(observe); win.__hhMO.observe(doc.body, { childList: true, subtree: true }); }

  if (win.__hhInit) return;
  win.__hhInit = true;

  function setTheme(next) {
    const apply = () => {
      root.setAttribute('data-theme', next);
      doc.querySelectorAll('[data-theme-toggle]').forEach(b => b.setAttribute('aria-pressed', next === 'dark'));
      set('localStorage', 'hh-theme', next);
    };
    if (doc.startViewTransition && !reduce) doc.startViewTransition(apply); else apply();
  }

  doc.addEventListener('click', (e) => {
    if (e.target.closest('[data-theme-toggle]')) {
      e.preventDefault();
      setTheme(root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
      return;
    }
    if (e.target.closest('[data-close-alert]')) {
      root.classList.add('alert-closed');
      set('sessionStorage', 'hh-alert', 'closed');
      return;
    }
    const link = e.target.closest('[data-scroll]');
    if (link) {
      const target = doc.getElementById(link.dataset.scroll);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
    }
  });
})();
</script>
""", height=0, width=0)
