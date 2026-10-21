import base64
import os
import random

import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# CONFIGURACIÓN DE PÁGINA
# =========================================================
st.set_page_config(
    page_title="Abogadas Hermandad | Defensa Legal de la Mujer",
    page_icon="⚖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# DATOS DEL ESTUDIO
# =========================================================
PHONE_DISPLAY = "+56 9 5492 2730"
PHONE_TEL = "+56954922730"
EMAIL = "Lex.Mfrancisca@gmail.com"
WA_LINK = "https://wa.me/56954922730?text=Hola%2C%20quisiera%20agendar%20una%20consulta%20confidencial."


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
# =========================================================
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

:root {
  --bg: #F6F4F0;
  --bg-2: #EEEAE3;
  --surface: #FFFFFF;
  --line: #E4DED3;
  --ink: #1A2233;
  --muted: #5E6675;
  --gold: #C39A3E;
  --gold-2: #E2BE6A;
  --gold-ink: #8E6A1A;
  --gold-soft: rgba(195,154,62,.14);
  --rose: rgba(214,150,170,.35);
  --blue: rgba(120,150,210,.28);
  --nav: rgba(255,255,255,.72);
  --shadow: 0 20px 50px -20px rgba(26,34,51,.22);
  --shadow-sm: 0 8px 24px -12px rgba(26,34,51,.20);
  --on-ink: #FFFFFF;
  --alert-h: 46px;
  --r-lg: 32px;
  --r-md: 22px;
  --r-sm: 14px;
  --spring: cubic-bezier(.34,1.4,.64,1);
  --smooth: cubic-bezier(.22,1,.36,1);
  --serif: 'Fraunces', Georgia, serif;
  --sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
}
:root[data-theme="dark"] {
  --bg: #0C111D;
  --bg-2: #121A2A;
  --surface: #151D2E;
  --line: #243049;
  --ink: #EEF0F5;
  --muted: #A1A9B8;
  --gold: #E2BE6A;
  --gold-2: #F3D58E;
  --gold-ink: #EBC878;
  --gold-soft: rgba(226,190,106,.13);
  --rose: rgba(170,90,140,.30);
  --blue: rgba(70,110,200,.30);
  --nav: rgba(21,29,46,.72);
  --shadow: 0 24px 60px -24px rgba(0,0,0,.70);
  --shadow-sm: 0 10px 28px -14px rgba(0,0,0,.60);
  --on-ink: #0C111D;
}
:root.alert-closed { --alert-h: 0px; }

html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
  background: var(--bg) !important;
  color: var(--ink) !important;
  font-family: var(--sans) !important;
}
#MainMenu, footer, header, [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"] { display: none !important; }
.block-container { padding-top: 7.5rem !important; padding-bottom: 2rem !important; max-width: 1180px !important; }
::selection { background: var(--gold); color: #1A2233; }
h1, h2, h3, h4 { font-family: var(--serif) !important; color: var(--ink) !important; font-weight: 500 !important; letter-spacing: -0.015em; }
a { text-decoration: none !important; color: inherit; }
a:focus-visible, button:focus-visible { outline: 3px solid var(--gold) !important; outline-offset: 3px; }

/* Transición de tema (respaldo si el navegador no soporta View Transitions) */
.t, .site-nav, .card, .case, .step, .team, .contact-panel, [data-testid="stForm"] {
  transition: background-color .6s var(--smooth), border-color .6s var(--smooth), color .6s var(--smooth), box-shadow .6s var(--smooth);
}
::view-transition-old(root), ::view-transition-new(root) { animation: none; mix-blend-mode: normal; }

/* ---------- Barra de progreso ---------- */
.progress { position: fixed; top: 0; left: 0; right: 0; height: 3px; z-index: 1000003; transform-origin: left;
  transform: scaleX(var(--p, 0)); background: linear-gradient(90deg, var(--gold), var(--gold-2)); border-radius: 0 3px 3px 0; }

/* ---------- Alerta de riesgo (roja, parpadeante, cerrable) ---------- */
.alert-bar { position: fixed; top: 0; left: 0; right: 0; height: 46px; z-index: 1000002;
  display: flex; align-items: center; justify-content: center; gap: 14px; padding: 0 56px;
  background: #B91C2E; color: #FFFFFF; font-size: .88rem; font-weight: 600;
  animation: alertBlink 1.6s ease-in-out infinite; transition: transform .5s var(--smooth), opacity .5s var(--smooth); }
.alert-bar.closing { transform: translateY(-100%); opacity: 0; }
:root.alert-closed .alert-bar { display: none; }
@keyframes alertBlink { 0%, 100% { background: #B91C2E; } 50% { background: #E0303F; } }
.alert-icon { width: 26px; height: 26px; border-radius: 50%; background: rgba(255,255,255,.18); display: grid; place-items: center;
  animation: iconPulse 1.6s ease-in-out infinite; flex-shrink: 0; }
@keyframes iconPulse { 0%, 100% { box-shadow: 0 0 0 0 rgba(255,255,255,.55); } 50% { box-shadow: 0 0 0 7px rgba(255,255,255,0); } }
.alert-bar span { color: #FFFFFF; }
.alert-bar a { color: #FFFFFF !important; background: rgba(255,255,255,.18); padding: 5px 12px; border-radius: 999px; font-weight: 700;
  transition: background-color .3s; white-space: nowrap; }
.alert-bar a:hover { background: rgba(255,255,255,.32); }
.alert-close { position: absolute; right: 14px; top: 50%; transform: translateY(-50%); width: 30px; height: 30px; border-radius: 50%;
  border: none; background: rgba(255,255,255,.18); color: #FFFFFF; font-size: 18px; line-height: 1; cursor: pointer;
  display: grid; place-items: center; transition: background-color .3s, transform .3s var(--spring); }
.alert-close:hover { background: rgba(255,255,255,.34); transform: translateY(-50%) rotate(90deg); }

/* ---------- Navegación flotante ---------- */
.site-nav { position: fixed; top: calc(var(--alert-h) + 14px); left: 50%; transform: translateX(-50%); z-index: 1000001;
  width: min(1120px, calc(100% - 28px)); height: 64px; padding: 0 10px 0 20px; border-radius: 999px;
  display: flex; align-items: center; justify-content: space-between;
  background: var(--nav); border: 1px solid var(--line); box-shadow: var(--shadow-sm);
  backdrop-filter: saturate(160%) blur(16px); -webkit-backdrop-filter: saturate(160%) blur(16px);
  transition: top .5s var(--smooth), height .4s var(--smooth), background-color .6s, border-color .6s; }
.site-nav.is-scrolled { height: 56px; }
.brand { display: flex; align-items: center; gap: 10px; font-family: var(--serif); font-size: 1.15rem; font-weight: 600; color: var(--ink); }
.brand-logo { width: 36px; height: 36px; border-radius: 50%; background: var(--gold-soft); display: grid; place-items: center; }
.nav-links { display: flex; align-items: center; gap: 4px; }
.nav-links a.nl { font-size: .87rem; font-weight: 600; color: var(--ink); padding: 9px 14px; border-radius: 999px; transition: background-color .3s, color .3s; }
.nav-links a.nl:hover, .nav-links a.nl.active { background: var(--gold-soft); color: var(--gold-ink); }
.nav-cta { margin-left: 6px; font-size: .87rem; font-weight: 700; padding: 11px 20px; border-radius: 999px;
  background: var(--ink); color: var(--on-ink) !important; transition: transform .35s var(--spring), box-shadow .35s; }
.nav-cta:hover { transform: translateY(-2px); box-shadow: var(--shadow-sm); }

/* ---------- Interruptor de tema con balanza ---------- */
.theme-toggle { position: relative; width: 86px; height: 42px; border-radius: 999px; border: 1px solid var(--line); cursor: pointer;
  background: linear-gradient(135deg, #FFE7B0, #F6C977); overflow: hidden; margin: 0 4px; padding: 0;
  transition: background .6s var(--smooth), border-color .6s; }
:root[data-theme="dark"] .theme-toggle { background: linear-gradient(135deg, #1E2A48, #2D3B63); }
.theme-toggle .sky { position: absolute; inset: 0; }
.theme-toggle .sun { position: absolute; right: 12px; top: 50%; width: 12px; height: 12px; margin-top: -6px; border-radius: 50%;
  background: #FFFFFF; box-shadow: 0 0 10px #FFF6D6; transition: transform .6s var(--spring), opacity .4s; }
.theme-toggle .star { position: absolute; width: 3px; height: 3px; border-radius: 50%; background: #FFFFFF; opacity: 0;
  transform: scale(0); transition: transform .5s var(--spring), opacity .5s; }
.theme-toggle .star.s1 { left: 14px; top: 10px; } .theme-toggle .star.s2 { left: 24px; top: 26px; } .theme-toggle .star.s3 { left: 34px; top: 12px; }
:root[data-theme="dark"] .theme-toggle .sun { transform: translateY(30px); opacity: 0; }
:root[data-theme="dark"] .theme-toggle .star { opacity: 1; transform: scale(1); }
:root[data-theme="dark"] .theme-toggle .star.s2 { transition-delay: .08s; } :root[data-theme="dark"] .theme-toggle .star.s3 { transition-delay: .16s; }
.theme-toggle .knob { position: absolute; top: 4px; left: 4px; width: 32px; height: 32px; border-radius: 50%; background: #FFFFFF;
  box-shadow: 0 4px 10px rgba(0,0,0,.18); display: grid; place-items: center; transition: transform .7s var(--spring), background-color .6s; }
:root[data-theme="dark"] .theme-toggle .knob { transform: translateX(44px); background: #0C111D; }
.mini-beam { transform-origin: 12px 8px; transition: transform .9s var(--spring); }
:root[data-theme="dark"] .mini-beam { transform: rotate(-18deg); }
.theme-toggle:hover .knob { box-shadow: 0 6px 16px rgba(0,0,0,.25); }

/* ---------- Hero centrado con balanza principal ---------- */
.hero { position: relative; text-align: center; padding: 2rem 1rem 3rem; isolation: isolate; }
.blob { position: absolute; border-radius: 50%; filter: blur(70px); z-index: -1; opacity: .9; animation: drift 18s ease-in-out infinite alternate; }
.blob.b1 { width: 420px; height: 420px; background: var(--gold-soft); top: -40px; left: 50%; margin-left: -210px; }
.blob.b2 { width: 320px; height: 320px; background: var(--rose); top: 120px; left: 6%; animation-delay: -6s; }
.blob.b3 { width: 340px; height: 340px; background: var(--blue); top: 80px; right: 4%; animation-delay: -12s; }
@keyframes drift { 0% { transform: translate(0,0) scale(1); } 50% { transform: translate(30px,-20px) scale(1.08); } 100% { transform: translate(-25px,25px) scale(.95); } }

.scale-stage { position: relative; width: 300px; height: 300px; margin: 0 auto 1.2rem; cursor: pointer; }
.scale-stage .halo { position: absolute; inset: 30px; border-radius: 50%;
  background: radial-gradient(circle, var(--gold-soft) 0%, transparent 70%); animation: halo 5s ease-in-out infinite; }
@keyframes halo { 50% { transform: scale(1.12); opacity: .7; } }
.orbit { position: absolute; inset: 0; border-radius: 50%; border: 1px dashed var(--line); animation: spin 40s linear infinite; }
.orbit.o2 { inset: 28px; border-style: solid; border-color: var(--gold-soft); animation-duration: 26s; animation-direction: reverse; }
.orbit::after { content: ""; position: absolute; top: -5px; left: 50%; width: 10px; height: 10px; margin-left: -5px; border-radius: 50%;
  background: var(--gold); box-shadow: 0 0 14px var(--gold); }
.orbit.o2::after { width: 7px; height: 7px; top: -3.5px; margin-left: -3.5px; background: var(--gold-2); }
@keyframes spin { to { transform: rotate(360deg); } }
.ripple { position: absolute; inset: 40px; border-radius: 50%; border: 2px solid var(--gold); opacity: 0; pointer-events: none; }
.ripple.go { animation: ripple 1s var(--smooth); }
@keyframes ripple { from { transform: scale(.6); opacity: .8; } to { transform: scale(1.5); opacity: 0; } }

.scale-svg { position: absolute; inset: 40px; width: calc(100% - 80px); height: calc(100% - 80px); overflow: visible; }
.scale-svg .st { stroke: var(--gold); fill: none; stroke-dasharray: 1; stroke-dashoffset: 1; animation: draw 1.6s var(--smooth) forwards; }
.scale-svg .st.d2 { animation-delay: .35s; } .scale-svg .st.d3 { animation-delay: .7s; } .scale-svg .st.d4 { animation-delay: 1s; }
.scale-svg .fl { fill: var(--gold); opacity: 0; animation: fadeIn .6s ease 1.5s forwards; }
.scale-svg .pan { fill: var(--gold); fill-opacity: 0; animation: panFill .8s ease 1.6s forwards; }
@keyframes draw { to { stroke-dashoffset: 0; } }
@keyframes panFill { to { fill-opacity: .22; } }
@keyframes fadeIn { to { opacity: 1; } }
.beam { transform-origin: 100px 52px; transition: transform 1.4s var(--spring); }
.pan-l { transform-origin: 36px 54px; transition: transform 1.4s var(--spring); }
.pan-r { transform-origin: 164px 54px; transition: transform 1.4s var(--spring); }
:root[data-theme="dark"] .beam { transform: rotate(-14deg); }
:root[data-theme="dark"] .pan-l, :root[data-theme="dark"] .pan-r { transform: rotate(14deg); }

.spark { position: absolute; left: 50%; top: 50%; width: 6px; height: 6px; border-radius: 50%; background: var(--gold-2); pointer-events: none;
  animation: spark .9s var(--smooth) forwards; }
@keyframes spark { from { transform: translate(-50%,-50%) scale(1); opacity: 1; } to { transform: translate(calc(-50% + var(--dx)), calc(-50% + var(--dy))) scale(0); opacity: 0; } }

.particle { position: absolute; border-radius: 50%; background: var(--gold); opacity: .0; z-index: -1; animation: float linear infinite; }
@keyframes float { 0% { transform: translateY(0); opacity: 0; } 15% { opacity: .55; } 85% { opacity: .4; } 100% { transform: translateY(-160px); opacity: 0; } }

.scale-caption { display: inline-flex; align-items: center; gap: 8px; font-size: .82rem; font-weight: 600; color: var(--muted);
  background: var(--surface); border: 1px solid var(--line); padding: 7px 14px; border-radius: 999px; box-shadow: var(--shadow-sm); margin-bottom: 1.8rem; }
.scale-caption .dot { width: 8px; height: 8px; border-radius: 50%; background: #3BAA6E; transition: background-color .6s; }
:root[data-theme="dark"] .scale-caption .dot { background: var(--gold); }
.scale-caption .cd, :root[data-theme="dark"] .scale-caption .cl { display: none; }
:root[data-theme="dark"] .scale-caption .cd { display: inline; }

.hero-title { font-family: var(--serif); font-weight: 500; font-size: clamp(2.5rem, 5.6vw, 4.6rem); line-height: 1.05; color: var(--ink);
  max-width: 15ch; margin: 0 auto 1.4rem; }
.hero-title .w { display: inline-block; opacity: 0; transform: translateY(24px) scale(.98); filter: blur(6px);
  animation: wordIn .9s var(--smooth) forwards; }
@keyframes wordIn { to { opacity: 1; transform: none; filter: blur(0); } }
.hero-title .shine { background: linear-gradient(100deg, var(--gold-ink) 20%, var(--gold-2) 45%, var(--gold-ink) 70%);
  background-size: 250% 100%; -webkit-background-clip: text; background-clip: text; color: transparent;
  animation: wordIn .9s var(--smooth) forwards, shine 5s linear 2s infinite; }
@keyframes shine { to { background-position: -250% 0; } }
.hero-lead { font-size: 1.1rem; line-height: 1.75; color: var(--muted); max-width: 40rem; margin: 0 auto 2.2rem; opacity: 0; animation: fadeUp .9s var(--smooth) 1s forwards; }
.hero-actions { display: flex; justify-content: center; flex-wrap: wrap; gap: 12px; opacity: 0; animation: fadeUp .9s var(--smooth) 1.15s forwards; }
@keyframes fadeUp { from { opacity: 0; transform: translateY(16px); } to { opacity: 1; transform: none; } }

.btn { position: relative; display: inline-flex; align-items: center; gap: 10px; padding: 16px 28px; border-radius: 999px; font-weight: 700; font-size: .95rem;
  transition: transform .35s var(--spring), box-shadow .35s, background-color .4s, color .4s; overflow: hidden; }
.btn-primary { background: linear-gradient(135deg, var(--gold), var(--gold-2)); color: #1A2233 !important; box-shadow: 0 14px 30px -12px var(--gold); }
.btn-primary::after { content: ""; position: absolute; top: 0; left: -60%; width: 40%; height: 100%;
  background: linear-gradient(100deg, transparent, rgba(255,255,255,.55), transparent); transform: skewX(-20deg); animation: sweep 3.5s ease-in-out 2.5s infinite; }
@keyframes sweep { 0% { left: -60%; } 40%, 100% { left: 130%; } }
.btn-primary:hover { transform: translateY(-3px) scale(1.02); box-shadow: 0 20px 40px -14px var(--gold); }
.btn-soft { background: var(--surface); color: var(--ink) !important; border: 1px solid var(--line); box-shadow: var(--shadow-sm); }
.btn-soft:hover { transform: translateY(-3px); }

.trust { display: flex; justify-content: center; flex-wrap: wrap; gap: 10px; margin-top: 2.4rem; opacity: 0; animation: fadeUp .9s var(--smooth) 1.3s forwards; }
.trust span { display: inline-flex; align-items: center; gap: 8px; font-size: .84rem; font-weight: 600; color: var(--ink);
  background: var(--surface); border: 1px solid var(--line); padding: 9px 16px; border-radius: 999px; }
.trust span i { width: 6px; height: 6px; border-radius: 50%; background: var(--gold); }

/* ---------- Secciones ---------- */
.section { padding: 6rem 0 0; scroll-margin-top: 130px; }
.sec-head { text-align: center; max-width: 40rem; margin: 0 auto 3rem; }
.chip { display: inline-block; font-size: .8rem; font-weight: 700; color: var(--gold-ink); background: var(--gold-soft); padding: 7px 14px;
  border-radius: 999px; margin-bottom: 1rem; }
.sec-head h2 { font-size: clamp(2.1rem, 4vw, 3.1rem) !important; margin: 0 0 .9rem !important; line-height: 1.1; }
.sec-head p { color: var(--muted); line-height: 1.75; margin: 0; font-size: 1.02rem; }

/* Tarjetas con inclinación 3D y foco de luz */
.grid3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.4rem; perspective: 1200px; }
.card { position: relative; background: var(--surface); border: 1px solid var(--line); border-radius: var(--r-lg); padding: 2.2rem 2rem;
  box-shadow: var(--shadow-sm); overflow: hidden; transform-style: preserve-3d;
  transform: rotateX(var(--rx, 0deg)) rotateY(var(--ry, 0deg)) translateY(var(--ty, 0));
  transition: transform .5s var(--smooth), box-shadow .5s, border-color .5s, background-color .6s; }
.card::before { content: ""; position: absolute; inset: 0; border-radius: inherit; pointer-events: none; opacity: 0;
  background: radial-gradient(420px circle at var(--mx, 50%) var(--my, 50%), var(--gold-soft), transparent 60%); transition: opacity .4s; }
.card:hover { --ty: -6px; box-shadow: var(--shadow); border-color: var(--gold); }
.card:hover::before { opacity: 1; }
.card > * { position: relative; }
.card-icon { width: 60px; height: 60px; border-radius: 20px; display: grid; place-items: center; margin-bottom: 1.6rem;
  background: linear-gradient(135deg, var(--gold-soft), transparent); border: 1px solid var(--line); transition: transform .5s var(--spring); }
.card:hover .card-icon { transform: rotate(-8deg) scale(1.08); }
.card-icon svg { stroke: var(--gold-ink); }
.card h3 { font-size: 1.55rem !important; margin: 0 0 .7rem !important; line-height: 1.2; }
.card p { color: var(--muted); line-height: 1.7; font-size: .95rem; margin: 0 0 1.4rem; }
.tags { display: flex; flex-wrap: wrap; gap: 8px; }
.tags span { font-size: .78rem; font-weight: 600; color: var(--ink); background: var(--bg-2); padding: 6px 12px; border-radius: 999px; }

/* Proceso */
.steps { position: relative; display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.4rem; }
.steps-line { position: absolute; top: 44px; left: 16%; right: 16%; height: 3px; border-radius: 3px; background: var(--line); overflow: hidden; z-index: 0; }
.steps-line::after { content: ""; position: absolute; inset: 0; background: linear-gradient(90deg, var(--gold), var(--gold-2));
  transform: scaleX(0); transform-origin: left; transition: transform 1.8s var(--smooth); }
.steps.in .steps-line::after { transform: scaleX(1); }
.step { position: relative; z-index: 1; text-align: center; background: var(--surface); border: 1px solid var(--line); border-radius: var(--r-lg);
  padding: 2rem 1.8rem; box-shadow: var(--shadow-sm); }
.step-n { width: 52px; height: 52px; border-radius: 50%; margin: -3.6rem auto 1.2rem; display: grid; place-items: center;
  font-family: var(--serif); font-size: 1.3rem; font-weight: 600; color: #1A2233; background: linear-gradient(135deg, var(--gold), var(--gold-2));
  box-shadow: 0 10px 24px -10px var(--gold); transform: scale(0); transition: transform .7s var(--spring); }
.steps.in .step-n { transform: scale(1); }
.steps.in .step:nth-child(3) .step-n { transition-delay: .5s; } .steps.in .step:nth-child(4) .step-n { transition-delay: 1s; }
.step h4 { font-size: 1.35rem !important; margin: 0 0 .6rem !important; }
.step p { color: var(--muted); font-size: .93rem; line-height: 1.7; margin: 0; }
.steps { padding-top: 2rem; }

/* Equipo */
.team { display: grid; grid-template-columns: .9fr 1.1fr; gap: 3rem; align-items: center; background: var(--surface); border: 1px solid var(--line);
  border-radius: 40px; padding: 2.4rem; box-shadow: var(--shadow); }
.portrait-wrap { position: relative; padding: 8px; border-radius: 32px; background: conic-gradient(from var(--a, 0deg), var(--gold), var(--rose), var(--gold-2), var(--blue), var(--gold));
  animation: rotateA 8s linear infinite; }
@property --a { syntax: '<angle>'; initial-value: 0deg; inherits: false; }
@keyframes rotateA { to { --a: 360deg; } }
.portrait { border-radius: 26px; overflow: hidden; aspect-ratio: 4/5; background: var(--bg-2); }
.portrait img { width: 100%; height: 100%; object-fit: cover; transition: transform 1.2s var(--smooth); }
.team:hover .portrait img { transform: scale(1.05); }
.monogram { width: 100%; height: 100%; display: grid; place-items: center; font-family: var(--serif); font-size: 6rem; color: var(--gold-ink); }
.team h3 { font-size: clamp(2rem, 3.6vw, 2.8rem) !important; margin: .4rem 0 1rem !important; line-height: 1.1; }
.team-bio { color: var(--muted); line-height: 1.8; font-size: 1rem; margin: 0 0 1.6rem; }
.quote { position: relative; background: var(--bg-2); border-radius: var(--r-md); padding: 1.4rem 1.6rem 1.4rem 3.2rem; font-family: var(--serif);
  font-style: italic; font-size: 1.12rem; line-height: 1.55; color: var(--ink); margin: 0 0 1.8rem; }
.quote::before { content: "“"; position: absolute; left: 1rem; top: .2rem; font-size: 3.4rem; color: var(--gold); font-style: normal; }
.pills { display: flex; flex-wrap: wrap; gap: 10px; }
.pill { display: inline-flex; align-items: center; gap: 10px; padding: 12px 18px; border-radius: 999px; background: var(--bg-2);
  color: var(--ink) !important; font-weight: 600; font-size: .9rem; transition: transform .35s var(--spring), background-color .3s; }
.pill:hover { transform: translateY(-3px); background: var(--gold-soft); }
.pill svg { stroke: var(--gold-ink); }

/* Casos */
.marquee { overflow: hidden; padding: 1rem 0 1.6rem;
  mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent); -webkit-mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent); }
.marquee-track { display: flex; gap: 1.2rem; width: max-content; animation: marquee 50s linear infinite; }
.marquee:hover .marquee-track { animation-play-state: paused; }
@keyframes marquee { to { transform: translateX(calc(-50% - .6rem)); } }
.case { width: 340px; flex-shrink: 0; white-space: normal; background: var(--surface); border: 1px solid var(--line); border-radius: var(--r-lg);
  padding: 1.8rem; box-shadow: var(--shadow-sm); transition: transform .45s var(--spring), border-color .4s; }
.case:hover { transform: translateY(-6px) rotate(-.6deg); border-color: var(--gold); }
.case .chip { margin-bottom: .9rem; }
.case h4 { font-size: 1.35rem !important; margin: 0 0 .55rem !important; line-height: 1.2; }
.case p { color: var(--muted); font-size: .9rem; line-height: 1.65; margin: 0; }
.note { text-align: center; font-size: .8rem; color: var(--muted); }

/* Formación */
.cred { padding: 0 !important; }
.cred-img { height: 190px; overflow: hidden; border-radius: var(--r-lg) var(--r-lg) 0 0; }
.cred-img img { width: 100%; height: 100%; object-fit: cover; transition: transform 1.2s var(--smooth); }
.card:hover .cred-img img { transform: scale(1.08); }
.cred-body { padding: 1.6rem 1.8rem 1.9rem; }
.cred-body small { color: var(--gold-ink); font-weight: 700; font-size: .8rem; }
.cred-body h4 { font-size: 1.3rem !important; margin: .4rem 0 .5rem !important; line-height: 1.2; }
.cred-body p { margin: 0; }

/* Contacto */
.contact-panel { height: 100%; border-radius: var(--r-lg); padding: 2.4rem; color: #FFFFFF; position: relative; overflow: hidden;
  background: linear-gradient(150deg, #1A2233, #2B3450); box-shadow: var(--shadow); }
:root[data-theme="dark"] .contact-panel { background: linear-gradient(150deg, #1D2741, #2A2140); }
.contact-panel::after { content: ""; position: absolute; width: 260px; height: 260px; border-radius: 50%; right: -80px; bottom: -80px;
  background: radial-gradient(circle, rgba(226,190,106,.35), transparent 70%); }
.contact-panel h3 { color: #FFFFFF !important; font-size: 1.9rem !important; margin: 0 0 .8rem !important; }
.contact-panel p { color: rgba(255,255,255,.78); line-height: 1.7; margin: 0 0 1.6rem; font-size: .95rem; }
.c-item { display: flex; align-items: center; gap: 14px; padding: 12px; border-radius: 18px; background: rgba(255,255,255,.07); margin-bottom: 10px;
  color: #FFFFFF !important; transition: background-color .3s, transform .35s var(--spring); position: relative; z-index: 1; }
.c-item:hover { background: rgba(255,255,255,.14); transform: translateX(4px); }
.c-item .ci { width: 40px; height: 40px; border-radius: 50%; background: rgba(226,190,106,.18); display: grid; place-items: center; flex-shrink: 0; }
.c-item small { display: block; font-size: .74rem; color: rgba(255,255,255,.65); }
.c-item b { font-size: .95rem; color: #FFFFFF; }
.c-lock { display: flex; gap: 10px; align-items: flex-start; font-size: .82rem; color: rgba(255,255,255,.75); margin-top: 1.2rem; line-height: 1.6; position: relative; z-index: 1; }

[data-testid="stForm"] { background: var(--surface) !important; border: 1px solid var(--line) !important; border-radius: var(--r-lg) !important;
  padding: 2.2rem !important; box-shadow: var(--shadow); }
[data-testid="stForm"] label p { font-weight: 600 !important; font-size: .85rem !important; color: var(--ink) !important; }
[data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea, [data-baseweb="select"] > div {
  background: var(--bg) !important; color: var(--ink) !important; border-radius: var(--r-sm) !important; border: 1.5px solid var(--line) !important;
  transition: border-color .3s, box-shadow .3s; }
[data-testid="stTextInput"] input::placeholder, [data-testid="stTextArea"] textarea::placeholder { color: var(--muted) !important; opacity: .7; }
[data-testid="stTextInput"] input:focus, [data-testid="stTextArea"] textarea:focus { border-color: var(--gold) !important; box-shadow: 0 0 0 4px var(--gold-soft) !important; }
[data-testid="stTextInput"] > div > div, [data-testid="stTextArea"] > div > div { border: none !important; background: transparent !important; }
[data-baseweb="select"] span, [data-baseweb="select"] div { color: var(--ink) !important; }
[data-baseweb="popover"] ul { background: var(--surface) !important; border-radius: var(--r-sm) !important; }
[data-baseweb="popover"] li { color: var(--ink) !important; }
[data-testid="stFormSubmitButton"] > button { width: 100%; border: none !important; border-radius: 999px !important; padding: .95rem 2rem !important;
  background: linear-gradient(135deg, var(--gold), var(--gold-2)) !important; box-shadow: 0 14px 30px -14px var(--gold) !important;
  transition: transform .35s var(--spring), box-shadow .35s !important; }
[data-testid="stFormSubmitButton"] > button p { color: #1A2233 !important; font-weight: 700 !important; }
[data-testid="stFormSubmitButton"] > button:hover { transform: translateY(-3px); box-shadow: 0 20px 40px -14px var(--gold) !important; }
.success { display: flex; gap: 12px; align-items: center; padding: 1rem 1.2rem; margin-top: 1rem; border-radius: var(--r-sm);
  background: rgba(46,139,87,.12); color: #2E8B57; font-weight: 600; font-size: .92rem; animation: pop .6s var(--spring); }
.success span { color: #2E8B57; }
@keyframes pop { from { transform: scale(.9); opacity: 0; } }

/* Footer */
.site-footer { margin-top: 6rem; background: var(--surface); border: 1px solid var(--line); border-radius: 36px; padding: 2.4rem;
  display: grid; grid-template-columns: 1.4fr 1fr 1fr; gap: 2rem; font-size: .88rem; color: var(--muted); }
.site-footer b { display: block; font-family: var(--serif); font-size: 1.3rem; font-weight: 500; color: var(--ink); margin-bottom: .4rem; }
.site-footer a { color: var(--ink); transition: color .3s; }
.site-footer a:hover { color: var(--gold-ink); }
.site-footer div div { margin-bottom: .4rem; }

/* WhatsApp */
.wa { position: fixed; right: 22px; bottom: 22px; z-index: 1000001; width: 60px; height: 60px; border-radius: 50%; background: #25D366;
  display: grid; place-items: center; box-shadow: 0 14px 30px -8px rgba(37,211,102,.6); transition: transform .4s var(--spring); }
.wa::before { content: ""; position: absolute; inset: 0; border-radius: 50%; border: 2px solid #25D366; animation: waPing 2.4s ease-out infinite; }
@keyframes waPing { from { transform: scale(1); opacity: .8; } to { transform: scale(1.7); opacity: 0; } }
.wa:hover { transform: scale(1.1) rotate(-8deg); }
.wa .tip { position: absolute; right: 72px; white-space: nowrap; background: var(--surface); color: var(--ink); font-size: .82rem; font-weight: 600;
  padding: 8px 14px; border-radius: 999px; box-shadow: var(--shadow-sm); opacity: 0; transform: translateX(8px); transition: opacity .3s, transform .3s; pointer-events: none; }
.wa:hover .tip { opacity: 1; transform: none; }

/* Revelado al hacer scroll */
.js .reveal { opacity: 0; transform: translateY(36px) scale(.97); transition: opacity .9s var(--smooth), transform .9s var(--smooth); }
.js .reveal.in { opacity: 1; transform: none; }

/* Responsive */
@media (max-width: 960px) {
  .grid3, .steps { grid-template-columns: 1fr; }
  .steps { gap: 3rem; padding-top: 2.4rem; }
  .steps-line { display: none; }
  .team { grid-template-columns: 1fr; padding: 1.4rem; border-radius: 32px; }
  .nav-links a.nl { display: none; }
  .site-footer { grid-template-columns: 1fr; }
  .alert-bar { font-size: .78rem; gap: 8px; padding: 0 48px 0 12px; justify-content: flex-start; }
  .alert-bar .hide-sm { display: none; }
  .scale-stage { width: 240px; height: 240px; }
  .brand-text { display: none; }
}
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: .01ms !important; animation-iteration-count: 1 !important; transition-duration: .01ms !important; }
  .js .reveal { opacity: 1; transform: none; }
  .alert-bar { animation: none; }
}
"""
st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)

# =========================================================
# ÍCONOS
# =========================================================
def icon(paths: str, size: int = 26) -> str:
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke-width="1.7" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>')

logo = """<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" style="stroke:var(--gold-ink)" aria-hidden="true">
<path d="M12 4v16M8 20h8M5 8h14M5 8l-2.5 6h5L5 8zM19 8l-2.5 6h5L19 8z"/></svg>"""

icon_shield = icon('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>')
icon_family = icon('<circle cx="9" cy="7" r="3"/><circle cx="17" cy="9" r="2.2"/><path d="M3 20v-1a5 5 0 0 1 10 0v1"/><path d="M14 20v-.5a3.5 3.5 0 0 1 7 0v.5"/>')
icon_work = icon('<rect x="3" y="7" width="18" height="13" rx="3"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/><path d="M3 13h18"/>')
icon_mail = icon('<rect x="2" y="4" width="20" height="16" rx="3"/><polyline points="22,6 12,13 2,6"/>', 18)
icon_phone = icon('<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.79 19.79 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>', 18)
icon_alert = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 9v4M12 17h.01"/><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/></svg>'
icon_lock = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#E2BE6A" stroke-width="1.8" aria-hidden="true"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>'
icon_check = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2E8B57" stroke-width="2.4" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>'
icon_wa = '<svg width="30" height="30" viewBox="0 0 24 24" fill="#FFFFFF" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.25-.46-2.38-1.47-.88-.78-1.47-1.75-1.65-2.05-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.06 2.88 1.21 3.08c.15.2 2.1 3.2 5.08 4.48.71.31 1.26.49 1.69.63.71.23 1.36.2 1.87.12.57-.09 1.75-.72 2-1.41.25-.69.25-1.29.17-1.41-.07-.12-.27-.2-.57-.35zM12.04 21.5a9.45 9.45 0 0 1-4.82-1.32l-.35-.21-3.58.94.96-3.49-.23-.36a9.43 9.43 0 0 1-1.45-5.03c0-5.22 4.25-9.47 9.48-9.47a9.4 9.4 0 0 1 6.7 2.78 9.4 9.4 0 0 1 2.77 6.7c0 5.22-4.25 9.46-9.47 9.46zm8.06-17.53A11.32 11.32 0 0 0 12.04.64C5.76.64.65 5.75.65 12.03c0 2.01.52 3.97 1.52 5.7L.55 23.6l6.02-1.58a11.36 11.36 0 0 0 5.47 1.39c6.28 0 11.39-5.11 11.39-11.39 0-3.04-1.18-5.9-3.34-8.05z"/></svg>'

# Mini balanza del interruptor de tema
mini_scale = """<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="stroke:var(--gold)" aria-hidden="true">
<path d="M12 6v14M8 20h8"/><g class="mini-beam"><path d="M4 8h16"/><path d="M5 8l-2.5 6h5L5 8zM19 8l-2.5 6h5L19 8z"/></g></svg>"""

# Balanza principal: se dibuja al cargar; se desbalancea en modo oscuro
main_scale = """
<svg class="scale-svg" viewBox="0 0 200 200" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
  <path class="st" pathLength="1" d="M100 40v128" stroke-width="3.5"/>
  <path class="st d2" pathLength="1" d="M66 180h68M80 180l20-12 20 12" stroke-width="3.5"/>
  <circle class="fl" cx="100" cy="34" r="6"/>
  <g class="beam">
    <path class="st d2" pathLength="1" d="M28 52h144" stroke-width="4"/>
    <circle class="fl" cx="100" cy="52" r="4.5"/>
    <g class="pan-l">
      <path class="st d3" pathLength="1" d="M36 54l-20 54M36 54l20 54" stroke-width="1.8"/>
      <path class="st d4 pan" pathLength="1" d="M10 108h52c0 12-11.6 20-26 20s-26-8-26-20z" stroke-width="2.4"/>
    </g>
    <g class="pan-r">
      <path class="st d3" pathLength="1" d="M164 54l-20 54M164 54l20 54" stroke-width="1.8"/>
      <path class="st d4 pan" pathLength="1" d="M138 108h52c0 12-11.6 20-26 20s-26-8-26-20z" stroke-width="2.4"/>
    </g>
  </g>
</svg>"""

# Partículas doradas flotantes del hero
random.seed(7)
particles = "".join(
    f'<span class="particle" style="left:{random.randint(4, 96)}%;top:{random.randint(30, 95)}%;'
    f'width:{s}px;height:{s}px;animation-duration:{random.uniform(7, 13):.1f}s;animation-delay:-{random.uniform(0, 10):.1f}s"></span>'
    for s in [random.choice([3, 4, 5, 6]) for _ in range(18)]
)

# =========================================================
# ALERTA + NAVEGACIÓN + WHATSAPP
# =========================================================
html(f"""
<div class="progress"></div>
<div class="alert-bar" role="alert">
  <span class="alert-icon">{icon_alert}</span>
  <span><span class="hide-sm">¿Estás en riesgo inminente? </span>Llama ahora:</span>
  <a href="tel:149">149 Carabineros</a>
  <a href="tel:1455">1455 SernamEG</a>
  <button class="alert-close" type="button" data-close-alert aria-label="Cerrar aviso">×</button>
</div>
<nav class="site-nav" aria-label="Navegación principal">
  <a class="brand" href="#inicio" data-scroll="inicio"><span class="brand-logo">{logo}</span><span class="brand-text">Abogadas Hermandad</span></a>
  <div class="nav-links">
    <a class="nl" href="#areas" data-scroll="areas">Áreas</a>
    <a class="nl" href="#proceso" data-scroll="proceso">Proceso</a>
    <a class="nl" href="#equipo" data-scroll="equipo">Equipo</a>
    <a class="nl" href="#casos" data-scroll="casos">Casos</a>
    <button class="theme-toggle" type="button" data-theme-toggle aria-label="Cambiar entre tema claro y oscuro" aria-pressed="false">
      <span class="sky"><span class="sun"></span><span class="star s1"></span><span class="star s2"></span><span class="star s3"></span></span>
      <span class="knob">{mini_scale}</span>
    </button>
    <a class="nav-cta" href="#contacto" data-scroll="contacto">Agendar consulta</a>
  </div>
</nav>
<a class="wa" href="{WA_LINK}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp">{icon_wa}<span class="tip">Escríbenos por WhatsApp</span></a>
""")

# =========================================================
# HERO: balanza principal arriba al centro
# =========================================================
html(f"""
<section class="hero" id="inicio">
  <span class="blob b1"></span><span class="blob b2"></span><span class="blob b3"></span>
  {particles}
  <div class="scale-stage" data-theme-toggle title="Cambiar tema" role="button" aria-label="Cambiar tema">
    <span class="halo"></span><span class="orbit"></span><span class="orbit o2"></span><span class="ripple"></span>
    {main_scale}
  </div>
  <div class="scale-caption"><span class="dot"></span><span class="cl">Modo claro · la balanza está en equilibrio</span><span class="cd">Modo oscuro · la balanza se inclina</span></div>
  <h1 class="hero-title">
    <span class="w" style="animation-delay:.2s">Defensa</span>
    <span class="w" style="animation-delay:.3s">legal</span>
    <span class="w" style="animation-delay:.4s">humana,</span>
    <span class="w shine" style="animation-delay:.5s">cercana</span>
    <span class="w" style="animation-delay:.6s">y</span>
    <span class="w" style="animation-delay:.7s">sin</span>
    <span class="w" style="animation-delay:.8s">prejuicios.</span>
  </h1>
  <p class="hero-lead">Acompañamos a mujeres en violencia intrafamiliar, derecho de familia y acoso laboral, con rigor técnico, total confidencialidad y explicaciones simples en cada paso.</p>
  <div class="hero-actions">
    <a class="btn btn-primary" href="#contacto" data-scroll="contacto">Agendar consulta confidencial</a>
    <a class="btn btn-soft" href="tel:{PHONE_TEL}">{icon_phone}<span>Llamar ahora</span></a>
  </div>
  <div class="trust">
    <span><i></i>Secreto profesional</span>
    <span><i></i>Medidas urgentes en casos VIF</span>
    <span><i></i>Atención online y presencial</span>
  </div>
</section>
""")

# =========================================================
# ÁREAS DE PRÁCTICA
# =========================================================
areas = [
    (icon_shield, "Protección y VIF",
     "Tramitación prioritaria de medidas cautelares y acciones penales para resguardar tu integridad.",
     ["Prohibición de acercamiento", "Salida del agresor", "Querellas"]),
    (icon_family, "Derecho de familia",
     "Representación en los procesos que definen el bienestar de tus hijos y la estabilidad de tu hogar.",
     ["Pensión de alimentos", "Retención AFP", "Cuidado personal", "Divorcio"]),
    (icon_work, "Acoso laboral y Ley Karin",
     "Intervención estratégica ante acoso laboral o sexual y vulneración de derechos en el trabajo.",
     ["Tutela de derechos", "Despido indirecto", "Maternidad"]),
]
area_cards = "".join(
    f"""<article class="card tilt reveal" style="transition-delay:{i * .12}s">
      <div class="card-icon">{ic}</div><h3>{t}</h3><p>{d}</p>
      <div class="tags">{''.join(f'<span>{x}</span>' for x in tags)}</div></article>"""
    for i, (ic, t, d, tags) in enumerate(areas)
)
html(f"""
<section class="section" id="areas">
  <div class="sec-head reveal">
    <span class="chip">Áreas de práctica</span>
    <h2>¿En qué podemos ayudarte?</h2>
    <p>Tres especialidades con un mismo compromiso: proteger tus derechos con estrategia y con la contención que necesitas.</p>
  </div>
  <div class="grid3">{area_cards}</div>
</section>
""")

# =========================================================
# PROCESO
# =========================================================
steps = [
    ("Conversamos", "Nos cuentas tu situación con total confidencialidad. Evaluamos riesgos y alternativas reales."),
    ("Definimos la estrategia", "Te proponemos un plan claro, con etapas y costos explicados sin tecnicismos."),
    ("Te representamos", "Llevamos tu causa ante tribunales y te mantenemos informada de cada avance."),
]
steps_html = "".join(
    f'<div class="step"><div class="step-n">{i + 1}</div><h4>{t}</h4><p>{d}</p></div>'
    for i, (t, d) in enumerate(steps)
)
html(f"""
<section class="section" id="proceso">
  <div class="sec-head reveal">
    <span class="chip">Cómo trabajamos</span>
    <h2>Simple, claro y a tu ritmo</h2>
    <p>Sabrás siempre en qué punto está tu caso y cuál es el siguiente paso.</p>
  </div>
  <div class="steps" data-steps><div class="steps-line"></div>{steps_html}</div>
</section>
""")

# =========================================================
# EQUIPO
# =========================================================
photo = image_to_data_uri("fran.jpg")
portrait = (f'<img src="{photo}" alt="Retrato de María-Francisca Valentina" />'
            if photo else '<div class="monogram">MF</div>')
html(f"""
<section class="section" id="equipo">
  <div class="sec-head reveal">
    <span class="chip">Equipo</span>
    <h2>Quién estará contigo</h2>
    <p>Atención directa con la abogada a cargo de tu causa, desde la primera reunión.</p>
  </div>
  <div class="team reveal">
    <div class="portrait-wrap"><div class="portrait">{portrait}</div></div>
    <div>
      <span class="chip">Abogada fundadora</span>
      <h3>María-Francisca Valentina</h3>
      <p class="team-bio">Especialista en violencia de género, familia, penal y laboral. Combina litigación técnica con un acompañamiento humano para la protección integral de tus derechos.</p>
      <blockquote class="quote">Ninguna mujer debería enfrentar sola un proceso judicial. Mi trabajo es que tengas claridad y respaldo en cada decisión.</blockquote>
      <div class="pills">
        <a class="pill" href="mailto:{EMAIL}">{icon_mail}<span>{EMAIL}</span></a>
        <a class="pill" href="tel:{PHONE_TEL}">{icon_phone}<span>{PHONE_DISPLAY}</span></a>
      </div>
    </div>
  </div>
</section>
""")

# =========================================================
# CASOS DESTACADOS
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
case_cards = "".join(
    f'<article class="case"><span class="chip">{c}</span><h4>{t}</h4><p>{d}</p></article>'
    for c, t, d in cases
)
html(f"""
<section class="section" id="casos">
  <div class="sec-head reveal">
    <span class="chip">Resultados</span>
    <h2>Casos destacados</h2>
    <p>Algunas resoluciones obtenidas para nuestras clientas. Pasa el cursor para detener el carrusel.</p>
  </div>
  <div class="marquee reveal"><div class="marquee-track">{case_cards}{case_cards}</div></div>
  <p class="note">Casos anonimizados. Los resultados anteriores no garantizan resultados futuros.</p>
</section>
""")

# =========================================================
# FORMACIÓN
# =========================================================
creds = [
    ("https://images.unsplash.com/photo-1589829545856-d10d557cf95f?q=80&w=800&auto=format&fit=crop",
     "Universidad de Chile", "Diplomado en Derecho de Familia", "Litigación oral y medidas cautelares en tribunales de familia."),
    ("https://images.unsplash.com/photo-1521791136064-7986c2920216?q=80&w=800&auto=format&fit=crop",
     "Pontificia Universidad Católica", "Certificación en Ley Karin y género", "Prevención, tutela de derechos fundamentales y acoso laboral."),
    ("https://images.unsplash.com/photo-1450133064473-71024230f91b?q=80&w=800&auto=format&fit=crop",
     "Academia Judicial / UDP", "Postítulo en Derecho Penal y VIF", "Estrategia penal y querellas por agresiones graves."),
]
cred_cards = "".join(
    f"""<article class="card cred tilt reveal" style="transition-delay:{i * .12}s">
      <div class="cred-img"><img src="{img}" alt="{t}" loading="lazy"/></div>
      <div class="cred-body"><small>{inst}</small><h4>{t}</h4><p>{d}</p></div></article>"""
    for i, (img, inst, t, d) in enumerate(creds)
)
html(f"""
<section class="section" id="formacion">
  <div class="sec-head reveal">
    <span class="chip">Formación</span>
    <h2>Preparación que respalda tu defensa</h2>
    <p>Especialización continua en las materias que defendemos ante tribunales.</p>
  </div>
  <div class="grid3">{cred_cards}</div>
</section>
""")

# =========================================================
# CONTACTO
# =========================================================
html("""
<section class="section" id="contacto">
  <div class="sec-head reveal">
    <span class="chip">Contacto</span>
    <h2>Agenda tu consulta confidencial</h2>
    <p>Cuéntanos lo esencial. Te respondemos personalmente por el medio que prefieras.</p>
  </div>
</section>
""")

col_info, col_form = st.columns([1, 1.5], gap="medium")

with col_info:
    html(f"""
    <div class="contact-panel reveal">
      <h3>Hablemos con total reserva</h3>
      <p>La primera conversación sirve para entender tu situación y explicarte tus opciones, sin compromiso.</p>
      <a class="c-item" href="tel:{PHONE_TEL}"><span class="ci">{icon_phone}</span><span><small>Teléfono y WhatsApp</small><b>{PHONE_DISPLAY}</b></span></a>
      <a class="c-item" href="mailto:{EMAIL}"><span class="ci">{icon_mail}</span><span><small>Correo electrónico</small><b>{EMAIL}</b></span></a>
      <div class="c-lock">{icon_lock}<span>Todo lo que compartas está protegido por secreto profesional y no se comparte con terceros.</span></div>
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
        mensaje = st.text_area("Cuéntanos brevemente tu caso", placeholder="No necesitas usar términos legales.", height=140)
        submitted = st.form_submit_button("Enviar consulta confidencial")

        if submitted:
            if nombre and (telefono or correo):
                html(f'<div class="success">{icon_check}<span>Consulta enviada. Te contactaremos a la brevedad.</span></div>')
            else:
                st.error("Indica tu nombre y al menos un medio de contacto (teléfono o correo) para poder responderte.")

# =========================================================
# FOOTER
# =========================================================
html(f"""
<footer class="site-footer">
  <div><b>Abogadas Hermandad</b><div>Estudio jurídico de la mujer en Chile.</div><div>© 2026 Todos los derechos reservados.</div></div>
  <div><div><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div><div><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
  <div><div><a href="#areas" data-scroll="areas">Áreas de práctica</a></div><div><a href="#equipo" data-scroll="equipo">Equipo</a></div><div><a href="#contacto" data-scroll="contacto">Agendar consulta</a></div></div>
</footer>
""")

# =========================================================
# INTERACCIONES
# =========================================================
components.html("""
<script>
(function () {
  const win = window.parent;
  const doc = win.document;
  const root = doc.documentElement;
  const reduce = win.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const store = {
    get(k) { try { return win.localStorage.getItem(k); } catch (e) { return null; } },
    set(k, v) { try { win.localStorage.setItem(k, v); } catch (e) {} },
    sget(k) { try { return win.sessionStorage.getItem(k); } catch (e) { return null; } },
    sset(k, v) { try { win.sessionStorage.setItem(k, v); } catch (e) {} }
  };

  // ---------- Estado inicial ----------
  if (!root.getAttribute('data-theme')) root.setAttribute('data-theme', store.get('hh-theme') || 'light');
  if (store.sget('hh-alert') === 'closed') root.classList.add('alert-closed');
  root.classList.add('js');

  // ---------- Revelado al hacer scroll ----------
  if (!win.__hhIO) {
    win.__hhIO = new win.IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); win.__hhIO.unobserve(e.target); } });
    }, { threshold: 0.15, rootMargin: '0px 0px -60px 0px' });
  }
  const observe = () => doc.querySelectorAll('.reveal:not(.in), [data-steps]:not(.in)').forEach(el => {
    reduce ? el.classList.add('in') : win.__hhIO.observe(el);
  });
  observe();
  if (!win.__hhMO) { win.__hhMO = new win.MutationObserver(observe); win.__hhMO.observe(doc.body, { childList: true, subtree: true }); }

  if (win.__hhInit) return;
  win.__hhInit = true;

  // ---------- Sonido suave de madera ----------
  let ctx = null;
  function wood() {
    const AC = win.AudioContext || win.webkitAudioContext;
    if (!AC) return;
    ctx = ctx || new AC();
    const t = ctx.currentTime;
    [[1050, 400, .45, .04], [1600, 800, .18, .025]].forEach(([f0, f1, g, d]) => {
      const o = ctx.createOscillator(), gn = ctx.createGain();
      o.frequency.setValueAtTime(f0, t); o.frequency.exponentialRampToValueAtTime(f1, t + d * .85);
      gn.gain.setValueAtTime(g, t); gn.gain.exponentialRampToValueAtTime(.001, t + d);
      o.connect(gn); gn.connect(ctx.destination); o.start(t); o.stop(t + d + .01);
    });
  }

  // ---------- Destellos dorados desde la balanza ----------
  function sparks() {
    const stage = doc.querySelector('.scale-stage');
    if (!stage || reduce) return;
    const ripple = stage.querySelector('.ripple');
    if (ripple) { ripple.classList.remove('go'); void ripple.offsetWidth; ripple.classList.add('go'); }
    for (let i = 0; i < 14; i++) {
      const s = doc.createElement('span');
      s.className = 'spark';
      const ang = (Math.PI * 2 * i) / 14, dist = 110 + Math.random() * 50;
      s.style.setProperty('--dx', Math.cos(ang) * dist + 'px');
      s.style.setProperty('--dy', Math.sin(ang) * dist + 'px');
      stage.appendChild(s);
      setTimeout(() => s.remove(), 950);
    }
  }

  // ---------- Cambio de tema con revelado circular ----------
  function setTheme(next, x, y) {
    const apply = () => {
      root.setAttribute('data-theme', next);
      doc.querySelectorAll('[data-theme-toggle]').forEach(b => b.setAttribute('aria-pressed', next === 'dark'));
      store.set('hh-theme', next);
    };
    if (!doc.startViewTransition || reduce) { apply(); sparks(); return; }
    const r = Math.hypot(Math.max(x, win.innerWidth - x), Math.max(y, win.innerHeight - y));
    const vt = doc.startViewTransition(apply);
    vt.ready.then(() => {
      root.animate({ clipPath: [`circle(0px at ${x}px ${y}px)`, `circle(${r}px at ${x}px ${y}px)`] },
        { duration: 750, easing: 'cubic-bezier(.22,1,.36,1)', pseudoElement: '::view-transition-new(root)' });
    });
    vt.finished.then(sparks);
  }

  // ---------- Clics ----------
  doc.addEventListener('click', (e) => {
    const toggle = e.target.closest('[data-theme-toggle]');
    if (toggle) {
      e.preventDefault();
      const next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      setTheme(next, e.clientX, e.clientY);
      wood();
      return;
    }
    if (e.target.closest('[data-close-alert]')) {
      const bar = doc.querySelector('.alert-bar');
      if (bar) bar.classList.add('closing');
      setTimeout(() => root.classList.add('alert-closed'), reduce ? 0 : 450);
      store.sset('hh-alert', 'closed');
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

  doc.addEventListener('mousedown', (e) => {
    if (e.target.closest('[data-testid="stFormSubmitButton"] button, .btn-primary, .nav-cta')) wood();
  });

  // ---------- Tarjetas: inclinación 3D y foco de luz ----------
  doc.addEventListener('pointermove', (e) => {
    const card = e.target.closest && e.target.closest('.tilt');
    if (!card || reduce) return;
    const r = card.getBoundingClientRect();
    const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
    card.style.setProperty('--mx', (px * 100) + '%');
    card.style.setProperty('--my', (py * 100) + '%');
    card.style.setProperty('--rx', ((.5 - py) * 8).toFixed(2) + 'deg');
    card.style.setProperty('--ry', ((px - .5) * 10).toFixed(2) + 'deg');
  });
  doc.addEventListener('pointerout', (e) => {
    const card = e.target.closest && e.target.closest('.tilt');
    if (card && !card.contains(e.relatedTarget)) { card.style.setProperty('--rx', '0deg'); card.style.setProperty('--ry', '0deg'); }
  });

  // ---------- Navbar, progreso y enlace activo ----------
  const ids = ['areas', 'proceso', 'equipo', 'casos', 'contacto'];
  let ticking = false;
  doc.addEventListener('scroll', (e) => {
    if (ticking) return;
    ticking = true;
    win.requestAnimationFrame(() => {
      const el = e.target === doc ? doc.scrollingElement : e.target;
      if (el && el.scrollHeight) {
        const max = el.scrollHeight - el.clientHeight, y = el.scrollTop;
        const nav = doc.querySelector('.site-nav'), bar = doc.querySelector('.progress');
        if (nav) nav.classList.toggle('is-scrolled', y > 40);
        if (bar && max > 0) bar.style.setProperty('--p', Math.min(y / max, 1));
      }
      let current = null;
      ids.forEach(id => { const s = doc.getElementById(id); if (s && s.getBoundingClientRect().top < 220) current = id; });
      doc.querySelectorAll('.nav-links a.nl').forEach(a => a.classList.toggle('active', a.dataset.scroll === current));
      ticking = false;
    });
  }, true);
})();
</script>
""", height=0, width=0)
