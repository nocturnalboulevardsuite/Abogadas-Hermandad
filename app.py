import base64
import os
import random

import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# CONFIGURACIÓN DE PÁGINA
# =========================================================
BRAND = "Hermanas Hermandad"

st.set_page_config(
    page_title=f"{BRAND} | Defensa Legal de la Mujer",
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
# Claro: beige, blanco y texto negro.
# Oscuro: azul espacial con estrellas, detalles dorados y texto blanco.
# =========================================================
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Inter:wght@400;500;600;700&display=swap');

:root {
  --bg: #F3EEE4;
  --bg-2: #EAE3D6;
  --surface: #FFFFFF;
  --surface-2: #F8F5EF;
  --line: #DDD4C4;
  --line-strong: #C9BEAA;
  --ink: #111111;
  --muted: #4B4B4B;
  --accent: #111111;
  --on-accent: #FFFFFF;
  --accent-soft: #EAE3D6;
  --nav: rgba(255,255,255,.86);
  --shadow: 0 24px 48px -28px rgba(17,17,17,.28);
  --shadow-sm: 0 10px 24px -16px rgba(17,17,17,.22);
  --sc-line: #161616;
  --sc-fill: #E9E0CE;
  --halo: radial-gradient(circle, rgba(255,255,255,.95) 0%, rgba(255,255,255,0) 68%);
  --alert-h: 46px;
  --nav-h: 78px;
  --r-lg: 22px;
  --r-md: 16px;
  --r-sm: 12px;
  --ease: cubic-bezier(.22,1,.36,1);
  --ease-io: cubic-bezier(.45,0,.2,1);
  --serif: 'Cormorant Garamond', Georgia, 'Times New Roman', serif;
  --sans: 'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif;
}
:root[data-theme="dark"] {
  --bg: #08102A;
  --bg-2: #0E1A3D;
  --surface: rgba(16,27,62,.78);
  --surface-2: rgba(22,36,80,.60);
  --line: rgba(217,181,101,.20);
  --line-strong: rgba(217,181,101,.38);
  --ink: #FFFFFF;
  --muted: #C7CDDC;
  --accent: #D9B565;
  --on-accent: #08102A;
  --accent-soft: rgba(217,181,101,.14);
  --nav: rgba(8,16,42,.80);
  --shadow: 0 28px 60px -30px rgba(0,0,0,.85);
  --shadow-sm: 0 12px 28px -18px rgba(0,0,0,.75);
  --sc-line: #D9B565;
  --sc-fill: rgba(217,181,101,.16);
  --halo: radial-gradient(circle, rgba(217,181,101,.28) 0%, rgba(217,181,101,0) 66%);
}
:root.alert-closed { --alert-h: 0px; }

html, body, .stApp {
  background: var(--bg) !important;
  color: var(--ink) !important;
  font-family: var(--sans) !important;
  -webkit-font-smoothing: antialiased;
  transition: background-color .9s var(--ease-io), color .9s var(--ease-io);
}
:root[data-theme="dark"] .stApp {
  background: radial-gradient(1200px 600px at 50% -10%, rgba(217,181,101,.22), transparent 60%),
              radial-gradient(900px 700px at 100% 60%, rgba(40,70,160,.35), transparent 60%),
              radial-gradient(800px 600px at 0% 90%, rgba(30,50,130,.40), transparent 60%),
              linear-gradient(180deg, #0A1433 0%, #08102A 50%, #060C22 100%) !important;
  background-attachment: fixed !important;
}
[data-testid="stAppViewContainer"], [data-testid="stMain"] { background: transparent !important; }
[data-testid="stMain"] { position: relative; z-index: 1; }
html, [data-testid="stMain"], [data-testid="stAppViewContainer"] { scroll-behavior: smooth; }
#MainMenu, footer, header, [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"] { display: none !important; }
.block-container { padding-top: calc(var(--alert-h) + var(--nav-h) + 1.5rem) !important; padding-bottom: 2rem !important; max-width: 1100px !important; }
::selection { background: var(--accent); color: var(--on-accent); }
h1, h2, h3, h4 { font-family: var(--serif) !important; color: var(--ink) !important; font-weight: 600 !important; letter-spacing: -0.01em; }
p, li, label, span { color: inherit; }
a { text-decoration: none !important; color: inherit; }
a:focus-visible, button:focus-visible { outline: 2px solid var(--accent) !important; outline-offset: 3px; }
::view-transition-old(root), ::view-transition-new(root) { animation-duration: .9s; animation-timing-function: var(--ease-io); }

.tt, .site-nav, .card, .case, .step, .team, .contact-panel, .site-footer, [data-testid="stForm"] {
  transition: background-color .9s var(--ease-io), border-color .9s var(--ease-io), color .9s var(--ease-io), box-shadow .6s var(--ease), transform .6s var(--ease);
}

/* ---------- Cielo estrellado (solo tema oscuro) ---------- */
.sky { position: fixed; inset: 0; z-index: -1; pointer-events: none; opacity: 0; transition: opacity 1.4s var(--ease-io); }
:root[data-theme="dark"] .sky { opacity: 1; }
.stars { position: absolute; top: 0; left: 0; width: 1px; height: 1px; border-radius: 50%; background: transparent; }
.stars.s2 { animation: twinkle 6s ease-in-out infinite; }
.stars.s3 { animation: twinkle 9s ease-in-out infinite -3s; }
@keyframes twinkle { 0%, 100% { opacity: 1; } 50% { opacity: .35; } }

/* ---------- Barra de progreso ---------- */
.progress { position: fixed; top: 0; left: 0; right: 0; height: 2px; z-index: 1000003; transform-origin: left;
  transform: scaleX(var(--p, 0)); background: var(--accent); }

/* ---------- Alerta de peligro inminente ---------- */
.alert-bar { position: fixed; top: 0; left: 0; right: 0; height: 46px; z-index: 1000002; isolation: isolate;
  display: flex; align-items: center; justify-content: center; gap: 12px; padding: 0 56px;
  background: #A3101F; color: #FFFFFF; font-size: .88rem; font-weight: 600;
  transition: transform .5s var(--ease), opacity .5s var(--ease); }
.alert-bar::before { content: ""; position: absolute; inset: 0; background: #DC1B30; z-index: -1; animation: alertBlink 1.2s steps(1, end) infinite; }
@keyframes alertBlink { 0% { opacity: 1; } 50% { opacity: 0; } }
.alert-bar.closing { transform: translateY(-100%); opacity: 0; }
:root.alert-closed .alert-bar { display: none; }
.alert-icon { width: 26px; height: 26px; border-radius: 50%; background: #FFFFFF; display: grid; place-items: center; flex-shrink: 0; }
.alert-bar strong { color: #FFFFFF; font-weight: 700; }
.alert-bar span { color: #FFFFFF; }
.alert-bar a { color: #A3101F !important; background: #FFFFFF; padding: 5px 12px; border-radius: 8px; font-weight: 700; font-size: .82rem;
  white-space: nowrap; transition: transform .25s var(--ease); }
.alert-bar a:hover { transform: translateY(-1px); }
.alert-close { position: absolute; right: 14px; top: 50%; transform: translateY(-50%); width: 30px; height: 30px; border-radius: 50%;
  border: 1px solid rgba(255,255,255,.55); background: transparent; color: #FFFFFF; font-size: 18px; line-height: 1; cursor: pointer;
  display: grid; place-items: center; transition: background-color .3s, transform .4s var(--ease); }
.alert-close:hover { background: rgba(255,255,255,.18); transform: translateY(-50%) rotate(90deg); }

/* ---------- Navegación ---------- */
.site-nav { position: fixed; top: var(--alert-h); left: 0; right: 0; height: var(--nav-h); z-index: 1000001;
  background: var(--nav); border-bottom: 1px solid var(--line);
  backdrop-filter: saturate(140%) blur(14px); -webkit-backdrop-filter: saturate(140%) blur(14px);
  transition: top .5s var(--ease), height .5s var(--ease), background-color .9s var(--ease-io), border-color .9s var(--ease-io);
  animation: navIn .9s var(--ease) both; }
@keyframes navIn { from { transform: translateY(-100%); opacity: 0; } }
.site-nav.is-scrolled { height: 64px; box-shadow: var(--shadow-sm); }
.nav-inner { max-width: 1100px; height: 100%; margin: 0 auto; padding: 0 24px; display: flex; align-items: center; justify-content: space-between; }
.brand { display: flex; align-items: center; gap: 12px; }
.brand-seal { width: 46px; height: 46px; flex-shrink: 0; transition: transform .8s var(--ease); }
.brand:hover .brand-seal { transform: rotate(-8deg); }
.brand-seal .seal-ring { stroke: var(--sc-line); fill: none; stroke-dasharray: 1; stroke-dashoffset: 1; animation: drawLine 1.6s var(--ease) .3s forwards; }
.brand-seal .seal-mark { stroke: var(--sc-line); fill: none; }
.brand-name { display: block; font-family: var(--serif); font-size: 1.42rem; font-weight: 700; color: var(--ink); line-height: 1; letter-spacing: .01em; }
.brand-sub { display: block; font-size: .72rem; color: var(--muted); margin-top: 5px; letter-spacing: .06em; }
.nav-links { display: flex; align-items: center; gap: 6px; }
.nav-links a.nl { position: relative; font-size: .88rem; font-weight: 500; color: var(--ink); padding: 8px 14px; }
.nav-links a.nl::after { content: ""; position: absolute; left: 14px; right: 14px; bottom: 2px; height: 1px; background: var(--accent);
  transform: scaleX(0); transform-origin: left; transition: transform .5s var(--ease); }
.nav-links a.nl:hover::after, .nav-links a.nl.active::after { transform: scaleX(1); }
.nav-cta { margin-left: 10px; font-size: .86rem; font-weight: 600; padding: 11px 20px; border-radius: 10px;
  background: var(--accent); color: var(--on-accent) !important; transition: transform .4s var(--ease), box-shadow .4s, background-color .9s var(--ease-io); }
.nav-cta:hover { transform: translateY(-2px); box-shadow: var(--shadow-sm); }

/* ---------- Botón de tema (balanza) abajo a la izquierda ---------- */
.theme-fab { position: fixed; left: 24px; bottom: 24px; z-index: 1000001; width: 64px; height: 64px; border-radius: 50%; padding: 0;
  border: 1px solid var(--line-strong); background: var(--surface); box-shadow: var(--shadow); cursor: pointer;
  display: grid; place-items: center; backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);
  transition: transform .5s var(--ease), background-color .9s var(--ease-io), border-color .9s var(--ease-io); }
.theme-fab:hover { transform: translateY(-3px); }
.theme-fab:active { transform: scale(.95); }
.theme-fab svg { width: 38px; height: 38px; overflow: visible; }
.fab-beam { transform-origin: 24px 13px; transition: transform 1.4s var(--ease-io); }
.fab-pan-l { transform-origin: 7px 14px; transition: transform 1.4s var(--ease-io); }
.fab-pan-r { transform-origin: 41px 14px; transition: transform 1.4s var(--ease-io); }
:root[data-theme="dark"] .fab-beam { transform: rotate(-14deg); }
:root[data-theme="dark"] .fab-pan-l, :root[data-theme="dark"] .fab-pan-r { transform: rotate(14deg); }
.theme-fab .fab-tip { position: absolute; left: 76px; white-space: nowrap; background: var(--surface); color: var(--ink); font-size: .8rem; font-weight: 600;
  padding: 8px 14px; border-radius: 10px; border: 1px solid var(--line); box-shadow: var(--shadow-sm);
  opacity: 0; transform: translateX(-6px); transition: opacity .35s, transform .35s var(--ease); pointer-events: none; }
.theme-fab:hover .fab-tip, .theme-fab:focus-visible .fab-tip { opacity: 1; transform: none; }
.tip-dark, :root[data-theme="dark"] .tip-light { display: none; }
:root[data-theme="dark"] .tip-dark { display: inline; }

/* ---------- Balanza (trazos, rellenos y movimiento) ---------- */
.st { fill: none; stroke: var(--sc-line); stroke-width: 1.6; stroke-linecap: round; stroke-linejoin: round;
  stroke-dasharray: 1; stroke-dashoffset: 1; animation: drawLine 1.5s var(--ease) var(--d, 0s) forwards;
  transition: stroke .9s var(--ease-io), fill .9s var(--ease-io); }
.st.sf { fill: var(--sc-fill); fill-opacity: 0; animation: drawLine 1.5s var(--ease) var(--d, 0s) forwards, fillIn 1s ease calc(var(--d, 0s) + .9s) forwards; }
.st.thin { stroke-width: 1; }
.d1 { --d: .15s; } .d2 { --d: .45s; } .d3 { --d: .75s; } .d4 { --d: 1.05s; } .d5 { --d: 1.3s; }
.dot { fill: var(--sc-line); opacity: 0; animation: fadeIn .6s ease 1.6s forwards; transition: fill .9s var(--ease-io); }
.sc-shadow { fill: var(--sc-line); opacity: .08; }
@keyframes drawLine { to { stroke-dashoffset: 0; } }
@keyframes fillIn { to { fill-opacity: 1; } }
@keyframes fadeIn { to { opacity: 1; } }

.beam { transform-origin: 120px 60px; transition: transform 1.8s var(--ease-io); }
.pan-l { transform-origin: 30px 66px; transition: transform 1.8s var(--ease-io); }
.pan-r { transform-origin: 210px 66px; transition: transform 1.8s var(--ease-io); }
:root[data-theme="dark"] .beam { transform: rotate(-12deg); }
:root[data-theme="dark"] .pan-l, :root[data-theme="dark"] .pan-r { transform: rotate(12deg); }
.beam-settle { transform-origin: 120px 60px; animation: sway 2.6s var(--ease-io) 1.9s both; }
.pan-settle-l { transform-origin: 30px 66px; animation: swayBack 2.6s var(--ease-io) 1.9s both; }
.pan-settle-r { transform-origin: 210px 66px; animation: swayBack 2.6s var(--ease-io) 1.9s both; }
@keyframes sway { 0% { transform: rotate(0); } 30% { transform: rotate(3.5deg); } 60% { transform: rotate(-1.6deg); } 85% { transform: rotate(.5deg); } 100% { transform: rotate(0); } }
@keyframes swayBack { 0% { transform: rotate(0); } 30% { transform: rotate(-3.5deg); } 60% { transform: rotate(1.6deg); } 85% { transform: rotate(-.5deg); } 100% { transform: rotate(0); } }

/* ---------- Hero ---------- */
.hero { text-align: center; padding: 2.5rem 0 3.5rem; }
.hero-inner { will-change: transform, opacity; }
.scale-stage { position: relative; width: 300px; height: 290px; margin: 0 auto 1.4rem; }
.scale-stage .halo { position: absolute; inset: -10px; border-radius: 50%; background: var(--halo); transition: background .9s var(--ease-io); }
.scale-stage .ring { position: absolute; left: 50%; top: 50%; width: 270px; height: 270px; margin: -135px 0 0 -135px; border-radius: 50%;
  border: 1px solid var(--line); opacity: 0; transform: scale(.92); animation: ringIn 1.6s var(--ease) .1s forwards; }
.scale-stage .ring.r2 { width: 230px; height: 230px; margin: -115px 0 0 -115px; border-style: dashed; animation-delay: .3s; }
@keyframes ringIn { to { opacity: 1; transform: scale(1); } }
.scale-svg { position: relative; width: 100%; height: 100%; overflow: visible; }

.scale-caption { display: inline-flex; align-items: center; gap: 10px; font-size: .8rem; font-weight: 500; color: var(--muted);
  padding: 7px 14px; border-radius: 999px; border: 1px solid var(--line); background: var(--surface); margin-bottom: 2rem;
  opacity: 0; animation: fadeUp .8s var(--ease) 1.8s forwards; }
.scale-caption .dot2 { width: 7px; height: 7px; border-radius: 50%; background: var(--accent); }
.cd, :root[data-theme="dark"] .cl { display: none; }
:root[data-theme="dark"] .cd { display: inline; }

.hero-title { font-family: var(--serif); font-weight: 600; font-size: clamp(2.6rem, 5.4vw, 4.4rem); line-height: 1.06; color: var(--ink);
  max-width: 17ch; margin: 0 auto 1.4rem; }
.hero-title .ln { display: block; overflow: hidden; padding-bottom: .06em; }
.hero-title .ln > span { display: block; transform: translateY(105%); animation: lineUp 1.1s var(--ease) forwards; }
.hero-title .ln:nth-child(1) > span { animation-delay: .5s; }
.hero-title .ln:nth-child(2) > span { animation-delay: .62s; }
.hero-title em { font-style: italic; font-weight: 500; }
@keyframes lineUp { to { transform: translateY(0); } }
.hero-lead { font-size: 1.08rem; line-height: 1.75; color: var(--muted); max-width: 38rem; margin: 0 auto 2.2rem; opacity: 0; animation: fadeUp .9s var(--ease) .9s forwards; }
.hero-actions { display: flex; justify-content: center; flex-wrap: wrap; gap: 12px; opacity: 0; animation: fadeUp .9s var(--ease) 1.05s forwards; }
@keyframes fadeUp { from { opacity: 0; transform: translateY(14px); } to { opacity: 1; transform: none; } }

.btn { display: inline-flex; align-items: center; gap: 10px; padding: 15px 26px; border-radius: 12px; font-weight: 600; font-size: .94rem;
  transition: transform .45s var(--ease), box-shadow .45s var(--ease), background-color .9s var(--ease-io), color .9s var(--ease-io), border-color .9s var(--ease-io); }
.btn-primary { background: var(--accent); color: var(--on-accent) !important; }
.btn-primary:hover { transform: translateY(-2px); box-shadow: var(--shadow); }
.btn-outline { background: transparent; color: var(--ink) !important; border: 1px solid var(--line-strong); }
.btn-outline:hover { border-color: var(--ink); transform: translateY(-2px); }
.btn svg { stroke: currentColor; }

.trust { display: grid; grid-template-columns: repeat(3, 1fr); max-width: 760px; margin: 3rem auto 0; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line);
  opacity: 0; animation: fadeUp .9s var(--ease) 1.2s forwards; }
.trust div { padding: 1.1rem .8rem; font-size: .86rem; color: var(--muted); }
.trust div + div { border-left: 1px solid var(--line); }
.trust b { display: block; font-family: var(--serif); font-size: 1.2rem; font-weight: 600; color: var(--ink); margin-bottom: 2px; }

/* ---------- Secciones ---------- */
.section { padding: 6.5rem 0 0; scroll-margin-top: 140px; }
.sec-head { text-align: center; max-width: 40rem; margin: 0 auto 3.2rem; }
.eyebrow { display: inline-block; font-size: .8rem; font-weight: 600; color: var(--muted); margin-bottom: .9rem; }
.sec-head h2 { font-size: clamp(2.2rem, 4vw, 3.2rem) !important; margin: 0 0 1rem !important; line-height: 1.08; }
.sec-head .rule { width: 56px; height: 1px; background: var(--accent); margin: 0 auto 1.2rem; transform: scaleX(0); transition: transform 1.2s var(--ease) .2s; }
.sec-head.in .rule { transform: scaleX(1); }
.sec-head p { color: var(--muted); line-height: 1.75; margin: 0; font-size: 1.02rem; }

.grid3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.4rem; }
.card { position: relative; background: var(--surface); border: 1px solid var(--line); border-radius: var(--r-lg); padding: 2.2rem 2rem; box-shadow: var(--shadow-sm); overflow: hidden; }
.card:hover { transform: translateY(-4px); box-shadow: var(--shadow); border-color: var(--line-strong); }
.card::after { content: ""; position: absolute; left: 0; right: 0; top: 0; height: 2px; background: var(--accent); transform: scaleX(0); transform-origin: left; transition: transform .7s var(--ease); }
.card:hover::after { transform: scaleX(1); }
.card-icon { width: 54px; height: 54px; border-radius: 14px; display: grid; place-items: center; margin-bottom: 1.5rem; background: var(--accent-soft); transition: background-color .9s var(--ease-io); }
.card-icon svg { stroke: var(--ink); }
.card h3 { font-size: 1.6rem !important; margin: 0 0 .7rem !important; line-height: 1.15; }
.card p { color: var(--muted); line-height: 1.7; font-size: .95rem; margin: 0 0 1.4rem; }
.list { list-style: none; margin: 0; padding: 1rem 0 0; border-top: 1px solid var(--line); }
.list li { position: relative; padding: 6px 0 6px 20px; font-size: .88rem; color: var(--ink); }
.list li::before { content: ""; position: absolute; left: 0; top: 14px; width: 9px; height: 1px; background: var(--ink); }

/* Proceso */
.steps { position: relative; display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.4rem; padding-top: 1.6rem; }
.steps-line { position: absolute; top: 1.6rem; left: 16.66%; right: 16.66%; height: 1px; background: var(--line); }
.steps-line::after { content: ""; position: absolute; inset: 0; background: var(--accent); transform: scaleX(0); transform-origin: left; transition: transform 2s var(--ease-io) .2s; }
.steps.in .steps-line::after { transform: scaleX(1); }
.step { position: relative; text-align: center; background: var(--surface); border: 1px solid var(--line); border-radius: var(--r-lg); padding: 2.6rem 1.8rem 2rem; box-shadow: var(--shadow-sm); }
.step-n { position: absolute; top: -22px; left: 50%; width: 44px; height: 44px; margin-left: -22px; border-radius: 50%; display: grid; place-items: center;
  font-family: var(--serif); font-size: 1.2rem; font-weight: 700; background: var(--accent); color: var(--on-accent);
  transform: scale(0); transition: transform .8s var(--ease), background-color .9s var(--ease-io), color .9s var(--ease-io); }
.steps.in .step-n { transform: scale(1); }
.steps.in .step:nth-of-type(2) .step-n { transition-delay: .6s; } .steps.in .step:nth-of-type(3) .step-n { transition-delay: 1.2s; }
.step h4 { font-size: 1.4rem !important; margin: 0 0 .6rem !important; }
.step p { color: var(--muted); font-size: .93rem; line-height: 1.7; margin: 0; }

/* Equipo */
.team { display: grid; grid-template-columns: .85fr 1.15fr; gap: 3rem; align-items: center; background: var(--surface); border: 1px solid var(--line);
  border-radius: 28px; padding: 2.4rem; box-shadow: var(--shadow); max-width: 1000px; margin: 0 auto; }
.portrait { border-radius: 20px; overflow: hidden; aspect-ratio: 4/5; background: var(--bg-2); outline: 1px solid var(--line-strong); outline-offset: 8px; }
.portrait img { width: 100%; height: 100%; object-fit: cover; transform: scale(1.04); transition: transform 1.6s var(--ease); }
.team.in .portrait img { transform: scale(1); }
.monogram { width: 100%; height: 100%; display: grid; place-items: center; font-family: var(--serif); font-size: 6rem; color: var(--ink); }
.team .role { font-size: .85rem; font-weight: 600; color: var(--muted); }
.team h3 { font-size: clamp(2.1rem, 3.6vw, 2.8rem) !important; margin: .3rem 0 1rem !important; line-height: 1.08; }
.team-bio { color: var(--muted); line-height: 1.8; font-size: 1rem; margin: 0 0 1.6rem; }
.quote { border-left: 2px solid var(--accent); padding: .2rem 0 .2rem 1.3rem; font-family: var(--serif); font-style: italic; font-size: 1.3rem; line-height: 1.5; color: var(--ink); margin: 0 0 1.8rem; }
.pills { display: flex; flex-wrap: wrap; gap: 10px; }
.pill { display: inline-flex; align-items: center; gap: 10px; padding: 11px 16px; border-radius: 12px; border: 1px solid var(--line);
  color: var(--ink) !important; font-weight: 500; font-size: .9rem; transition: border-color .4s, transform .4s var(--ease); }
.pill:hover { border-color: var(--ink); transform: translateY(-2px); }
.pill svg { stroke: var(--ink); }

/* Casos */
.marquee { overflow: hidden; padding: 1rem 0 1.6rem;
  mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent); -webkit-mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent); }
.marquee-track { display: flex; gap: 1.2rem; width: max-content; animation: marquee 70s linear infinite; }
.marquee:hover .marquee-track { animation-play-state: paused; }
@keyframes marquee { to { transform: translateX(calc(-50% - .6rem)); } }
.case { width: 340px; flex-shrink: 0; white-space: normal; background: var(--surface); border: 1px solid var(--line); border-radius: var(--r-lg); padding: 1.8rem; box-shadow: var(--shadow-sm); }
.case:hover { transform: translateY(-4px); border-color: var(--line-strong); }
.case .tag { display: inline-block; font-size: .76rem; font-weight: 600; color: var(--ink); background: var(--accent-soft); padding: 5px 11px; border-radius: 8px; margin-bottom: 1rem; }
.case h4 { font-size: 1.35rem !important; margin: 0 0 .5rem !important; line-height: 1.2; }
.case p { color: var(--muted); font-size: .9rem; line-height: 1.65; margin: 0; }
.note { text-align: center; font-size: .8rem; color: var(--muted); }

/* Formación */
.cred { padding: 0 !important; }
.cred-img { height: 190px; overflow: hidden; }
.cred-img img { width: 100%; height: 100%; object-fit: cover; filter: grayscale(100%) contrast(1.05); transition: transform 1.4s var(--ease), filter 1s var(--ease); }
.card:hover .cred-img img { transform: scale(1.05); filter: grayscale(0%); }
.cred-body { padding: 1.6rem 1.8rem 1.9rem; }
.cred-body small { color: var(--muted); font-weight: 600; font-size: .8rem; }
.cred-body h4 { font-size: 1.32rem !important; margin: .4rem 0 .5rem !important; line-height: 1.2; }
.cred-body p { margin: 0; }

/* Contacto */
.contact-panel { height: 100%; border-radius: var(--r-lg); padding: 2.4rem; background: #111111; color: #FFFFFF; box-shadow: var(--shadow); }
:root[data-theme="dark"] .contact-panel { background: linear-gradient(160deg, rgba(217,181,101,.22), rgba(16,27,62,.9)); border: 1px solid var(--line-strong); }
.contact-panel h3 { color: #FFFFFF !important; font-size: 1.9rem !important; margin: 0 0 .8rem !important; }
.contact-panel p { color: rgba(255,255,255,.8); line-height: 1.7; margin: 0 0 1.6rem; font-size: .95rem; }
.c-item { display: flex; align-items: center; gap: 14px; padding: 14px 0; border-top: 1px solid rgba(255,255,255,.16); color: #FFFFFF !important; transition: padding-left .4s var(--ease); }
.c-item:hover { padding-left: 6px; }
.c-item .ci { width: 40px; height: 40px; border-radius: 50%; border: 1px solid rgba(255,255,255,.3); display: grid; place-items: center; flex-shrink: 0; }
.c-item .ci svg { stroke: #FFFFFF; }
.c-item small { display: block; font-size: .74rem; color: rgba(255,255,255,.65); }
.c-item b { font-size: .95rem; font-weight: 600; color: #FFFFFF; }
.c-lock { display: flex; gap: 10px; align-items: flex-start; font-size: .82rem; color: rgba(255,255,255,.75); margin-top: 1.2rem; line-height: 1.6; border-top: 1px solid rgba(255,255,255,.16); padding-top: 1.2rem; }

[data-testid="stForm"] { background: var(--surface) !important; border: 1px solid var(--line) !important; border-radius: var(--r-lg) !important; padding: 2.2rem !important; box-shadow: var(--shadow); }
[data-testid="stForm"] label p { font-weight: 600 !important; font-size: .84rem !important; color: var(--ink) !important; }
[data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea, [data-baseweb="select"] > div {
  background: var(--surface-2) !important; color: var(--ink) !important; border-radius: var(--r-sm) !important; border: 1px solid var(--line) !important;
  font-family: var(--sans) !important; transition: border-color .3s, box-shadow .3s; }
[data-testid="stTextInput"] input::placeholder, [data-testid="stTextArea"] textarea::placeholder { color: var(--muted) !important; opacity: .7; }
[data-testid="stTextInput"] input:focus, [data-testid="stTextArea"] textarea:focus { border-color: var(--ink) !important; box-shadow: 0 0 0 3px var(--accent-soft) !important; }
[data-testid="stTextInput"] > div > div, [data-testid="stTextArea"] > div > div { border: none !important; background: transparent !important; }
[data-baseweb="select"] span, [data-baseweb="select"] div { color: var(--ink) !important; }
[data-baseweb="popover"] ul { background: var(--bg) !important; border-radius: var(--r-sm) !important; }
[data-baseweb="popover"] li { color: var(--ink) !important; }
[data-testid="stFormSubmitButton"] > button { width: 100%; border: none !important; border-radius: 12px !important; padding: .95rem 2rem !important;
  background: var(--accent) !important; transition: transform .45s var(--ease), box-shadow .45s var(--ease) !important; }
[data-testid="stFormSubmitButton"] > button p { color: var(--on-accent) !important; font-weight: 600 !important; }
[data-testid="stFormSubmitButton"] > button:hover { transform: translateY(-2px); box-shadow: var(--shadow) !important; }
.success { display: flex; gap: 12px; align-items: center; padding: 1rem 1.2rem; margin-top: 1rem; border-radius: var(--r-sm);
  border: 1px solid rgba(46,139,87,.45); background: rgba(46,139,87,.10); color: #2E8B57; font-weight: 600; font-size: .92rem; animation: fadeUp .6s var(--ease) both; }
.success span { color: #2E8B57; }

/* Footer */
.site-footer { margin-top: 6rem; border-top: 1px solid var(--line); padding: 2.6rem 0 1rem;
  display: grid; grid-template-columns: 1.4fr 1fr 1fr; gap: 2rem; font-size: .88rem; color: var(--muted); }
.site-footer b { display: block; font-family: var(--serif); font-size: 1.4rem; font-weight: 700; color: var(--ink); margin-bottom: .4rem; }
.site-footer a { color: var(--ink); transition: opacity .3s; }
.site-footer a:hover { opacity: .65; }
.site-footer div div { margin-bottom: .45rem; }

/* WhatsApp */
.wa { position: fixed; right: 24px; bottom: 24px; z-index: 1000001; width: 60px; height: 60px; border-radius: 50%; background: #25D366;
  display: grid; place-items: center; box-shadow: 0 14px 30px -10px rgba(37,211,102,.6); transition: transform .45s var(--ease); }
.wa:hover { transform: translateY(-3px); }
.wa .tip { position: absolute; right: 72px; white-space: nowrap; background: var(--surface); color: var(--ink); font-size: .8rem; font-weight: 600;
  padding: 8px 14px; border-radius: 10px; border: 1px solid var(--line); box-shadow: var(--shadow-sm); opacity: 0; transform: translateX(6px); transition: opacity .35s, transform .35s var(--ease); pointer-events: none; }
.wa:hover .tip { opacity: 1; transform: none; }

/* Revelado al hacer scroll */
.js .reveal { opacity: 0; transform: translateY(26px); transition: opacity 1.1s var(--ease), transform 1.1s var(--ease); }
.js .reveal.in { opacity: 1; transform: none; }

/* Responsive */
@media (max-width: 960px) {
  :root { --nav-h: 66px; }
  .grid3, .steps { grid-template-columns: 1fr; }
  .steps { gap: 2.6rem; }
  .steps-line { display: none; }
  .team { grid-template-columns: 1fr; padding: 1.4rem; gap: 2rem; }
  .nav-links a.nl { display: none; }
  .site-footer { grid-template-columns: 1fr; }
  .trust { grid-template-columns: 1fr; }
  .trust div + div { border-left: none; border-top: 1px solid var(--line); }
  .alert-bar { font-size: .76rem; gap: 8px; padding: 0 48px 0 12px; justify-content: flex-start; }
  .alert-bar .hide-sm { display: none; }
  .scale-stage { width: 230px; height: 222px; }
  .scale-stage .ring { width: 210px; height: 210px; margin: -105px 0 0 -105px; }
  .scale-stage .ring.r2 { width: 176px; height: 176px; margin: -88px 0 0 -88px; }
  .brand-sub { display: none; }
  .brand-name { font-size: 1.2rem; }
  .theme-fab { width: 56px; height: 56px; left: 16px; bottom: 16px; }
  .theme-fab .fab-tip { display: none; }
  .wa { right: 16px; bottom: 16px; }
}
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: .01ms !important; animation-iteration-count: 1 !important; transition-duration: .01ms !important; }
  .js .reveal { opacity: 1; transform: none; }
  .alert-bar::before { animation: none; }
}
"""
st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)


# =========================================================
# ÍCONOS Y DIBUJOS
# =========================================================
def icon(paths: str, size: int = 24) -> str:
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>')


icon_shield = icon('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>')
icon_family = icon('<circle cx="9" cy="7" r="3"/><circle cx="17" cy="9" r="2.2"/><path d="M3 20v-1a5 5 0 0 1 10 0v1"/><path d="M14 20v-.5a3.5 3.5 0 0 1 7 0v.5"/>')
icon_work = icon('<rect x="3" y="7" width="18" height="13" rx="2.5"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/><path d="M3 13h18"/>')
icon_mail = icon('<rect x="2" y="4" width="20" height="16" rx="2.5"/><polyline points="22,6 12,13 2,6"/>', 18)
icon_phone = icon('<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.79 19.79 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>', 18)
icon_alert = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#A3101F" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 9v4M12 17h.01"/><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/></svg>'
icon_lock = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="1.6" aria-hidden="true"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>'
icon_check = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2E8B57" stroke-width="2.2" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>'
icon_wa = '<svg width="30" height="30" viewBox="0 0 24 24" fill="#FFFFFF" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.25-.46-2.38-1.47-.88-.78-1.47-1.75-1.65-2.05-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.06 2.88 1.21 3.08c.15.2 2.1 3.2 5.08 4.48.71.31 1.26.49 1.69.63.71.23 1.36.2 1.87.12.57-.09 1.75-.72 2-1.41.25-.69.25-1.29.17-1.41-.07-.12-.27-.2-.57-.35zM12.04 21.5a9.45 9.45 0 0 1-4.82-1.32l-.35-.21-3.58.94.96-3.49-.23-.36a9.43 9.43 0 0 1-1.45-5.03c0-5.22 4.25-9.47 9.48-9.47a9.4 9.4 0 0 1 6.7 2.78 9.4 9.4 0 0 1 2.77 6.7c0 5.22-4.25 9.46-9.47 9.46zm8.06-17.53A11.32 11.32 0 0 0 12.04.64C5.76.64.65 5.75.65 12.03c0 2.01.52 3.97 1.52 5.7L.55 23.6l6.02-1.58a11.36 11.36 0 0 0 5.47 1.39c6.28 0 11.39-5.11 11.39-11.39 0-3.04-1.18-5.9-3.34-8.05z"/></svg>'

# Logo: sello circular con balanza
logo_seal = """
<svg class="brand-seal" viewBox="0 0 48 48" aria-hidden="true">
  <circle class="seal-ring" pathLength="1" cx="24" cy="24" r="22.5" stroke-width="1.2"/>
  <circle class="seal-mark" cx="24" cy="24" r="19" stroke-width=".6" stroke-dasharray="1.2 2"/>
  <g class="seal-mark" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round">
    <path d="M24 14v19M19.5 33.5h9M21 33.5l3-2.2 3 2.2"/>
    <path d="M13.5 18.2Q24 16.6 34.5 18.2"/>
    <path d="M14.5 18.6l-3 7M14.5 18.6l3 7M10.5 25.6h8c-.4 2-2 3.2-4 3.2s-3.6-1.2-4-3.2z"/>
    <path d="M33.5 18.6l-3 7M33.5 18.6l3 7M29.5 25.6h8c-.4 2-2 3.2-4 3.2s-3.6-1.2-4-3.2z"/>
    <circle cx="24" cy="12.6" r="1.3"/>
  </g>
</svg>"""

# Balanza principal (columna clásica, brazo curvo con remates, cadenas y platillos)
def pan(cx: int, cls: str, settle: str) -> str:
    l, r = cx - 28, cx + 28
    return f"""
    <g class="{cls}"><g class="{settle}">
      <circle class="st d4" pathLength="1" cx="{cx}" cy="70" r="3"/>
      <path class="st thin d4" pathLength="1" d="M{cx} 73 L{l + 2} 146"/>
      <path class="st thin d4" pathLength="1" d="M{cx} 73 L{cx} 146"/>
      <path class="st thin d4" pathLength="1" d="M{cx} 73 L{r - 2} 146"/>
      <path class="st sf d5" pathLength="1" d="M{l} 146h56c-2.4 14-13.6 22-28 22s-25.6-8-28-22z"/>
      <path class="st d5" pathLength="1" d="M{l - 2} 146h60"/>
    </g></g>"""


main_scale = f"""
<svg class="scale-svg" viewBox="0 0 240 232" aria-hidden="true">
  <ellipse class="sc-shadow" cx="120" cy="222" rx="74" ry="4"/>
  <path class="st sf d1" pathLength="1" d="M70 216h100a3 3 0 0 0 3-3v-3a3 3 0 0 0-3-3H70a3 3 0 0 0-3 3v3a3 3 0 0 0 3 3z"/>
  <path class="st sf d1" pathLength="1" d="M86 207h68l-7-11H93z"/>
  <path class="st sf d2" pathLength="1" d="M112 196 L115.5 70 H124.5 L128 196 Z"/>
  <path class="st thin d2" pathLength="1" d="M118 78v110M122 78v110"/>
  <path class="st sf d3" pathLength="1" d="M107 70h26l-3.5-6h-19z"/>
  <circle class="st sf d3" pathLength="1" cx="120" cy="52" r="6.5"/>
  <path class="st d3" pathLength="1" d="M120 45.5v-7"/>
  <circle class="dot" cx="120" cy="36" r="2.6"/>
  <g class="beam"><g class="beam-settle">
    <path class="st sf d3" pathLength="1" d="M28 62.5 Q120 54 212 62.5 L212 67.5 Q120 60 28 67.5 Z"/>
    <circle class="st sf d4" pathLength="1" cx="25" cy="65" r="4.2"/>
    <circle class="st sf d4" pathLength="1" cx="215" cy="65" r="4.2"/>
    <circle class="st sf d3" pathLength="1" cx="120" cy="60" r="6"/>
    <circle class="dot" cx="120" cy="60" r="2"/>
    {pan(30, "pan-l", "pan-settle-l")}
    {pan(210, "pan-r", "pan-settle-r")}
  </g></g>
</svg>"""

# Balanza del botón de tema
fab_scale = """
<svg viewBox="0 0 48 48" fill="none" stroke-linecap="round" stroke-linejoin="round" style="stroke:var(--sc-line)" aria-hidden="true">
  <path d="M17 43h14M20 43l4-3 4 3" stroke-width="1.8"/>
  <path d="M24 10v30" stroke-width="2"/>
  <circle cx="24" cy="7.5" r="1.8" style="fill:var(--sc-line)" stroke="none"/>
  <g class="fab-beam">
    <path d="M6 13.4Q24 11 42 13.4" stroke-width="2"/>
    <g class="fab-pan-l"><path d="M7 14l-5 11M7 14l5 11" stroke-width="1.1"/><path d="M1 25h12c-.6 3-3 4.8-6 4.8S1.6 28 1 25z" stroke-width="1.5" style="fill:var(--sc-fill)"/></g>
    <g class="fab-pan-r"><path d="M41 14l-5 11M41 14l5 11" stroke-width="1.1"/><path d="M35 25h12c-.6 3-3 4.8-6 4.8S35.6 28 35 25z" stroke-width="1.5" style="fill:var(--sc-fill)"/></g>
  </g>
</svg>"""


# Estrellas del modo oscuro (generadas una vez)
def star_shadows(n: int, seed: int, color: str) -> str:
    rnd = random.Random(seed)
    return ", ".join(f"{rnd.uniform(0, 100):.2f}vw {rnd.uniform(0, 100):.2f}vh {color}" for _ in range(n))


stars_html = (
    f'<div class="sky" aria-hidden="true">'
    f'<span class="stars" style="box-shadow:{star_shadows(140, 1, "rgba(255,255,255,.55)")}"></span>'
    f'<span class="stars s2" style="width:2px;height:2px;box-shadow:{star_shadows(45, 2, "rgba(255,255,255,.9)")}"></span>'
    f'<span class="stars s3" style="width:2px;height:2px;box-shadow:{star_shadows(22, 3, "rgba(240,210,140,.95)")}"></span>'
    f'</div>'
)

# =========================================================
# ALERTA + NAVEGACIÓN + BOTONES FLOTANTES
# =========================================================
html(f"""
{stars_html}
<div class="progress"></div>
<div class="alert-bar" role="alert">
  <span class="alert-icon">{icon_alert}</span>
  <span><strong>¿Estás en peligro inminente?</strong> <span class="hide-sm">Llama de inmediato:</span></span>
  <a href="tel:149">149 Fono Familia Carabineros</a>
  <a class="hide-sm" href="tel:133">133 Carabineros</a>
  <a class="hide-sm" href="tel:1455">1455 SernamEG</a>
  <button class="alert-close" type="button" data-close-alert aria-label="Cerrar aviso">×</button>
</div>
<nav class="site-nav" aria-label="Navegación principal">
  <div class="nav-inner">
    <a class="brand" href="#inicio" data-scroll="inicio" aria-label="{BRAND}, ir al inicio">
      {logo_seal}
      <span><span class="brand-name">{BRAND}</span><span class="brand-sub">Estudio jurídico de la mujer</span></span>
    </a>
    <div class="nav-links">
      <a class="nl" href="#areas" data-scroll="areas">Áreas</a>
      <a class="nl" href="#proceso" data-scroll="proceso">Proceso</a>
      <a class="nl" href="#equipo" data-scroll="equipo">Equipo</a>
      <a class="nl" href="#casos" data-scroll="casos">Casos</a>
      <a class="nav-cta" href="#contacto" data-scroll="contacto">Agendar consulta</a>
    </div>
  </div>
</nav>
<button class="theme-fab" type="button" data-theme-toggle aria-label="Cambiar entre tema claro y oscuro" aria-pressed="false">
  {fab_scale}<span class="fab-tip"><span class="tip-light">Activar tema oscuro</span><span class="tip-dark">Volver al tema claro</span></span>
</button>
<a class="wa" href="{WA_LINK}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp">{icon_wa}<span class="tip">Escríbenos por WhatsApp</span></a>
""")

# =========================================================
# HERO
# =========================================================
html(f"""
<section class="hero" id="inicio">
  <div class="hero-inner">
    <div class="scale-stage" aria-hidden="true">
      <span class="halo"></span><span class="ring"></span><span class="ring r2"></span>
      {main_scale}
    </div>
    <div class="scale-caption"><span class="dot2"></span><span class="cl">Tema claro · balanza en equilibrio</span><span class="cd">Tema oscuro · balanza inclinada</span></div>
    <h1 class="hero-title">
      <span class="ln"><span>Defensa legal especializada,</span></span>
      <span class="ln"><span><em>humana y sin prejuicios.</em></span></span>
    </h1>
    <p class="hero-lead">Representamos a mujeres en violencia intrafamiliar, derecho de familia y acoso laboral, con rigor técnico, absoluta confidencialidad y explicaciones claras en cada etapa.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="#contacto" data-scroll="contacto">Agendar consulta confidencial</a>
      <a class="btn btn-outline" href="tel:{PHONE_TEL}">{icon_phone}<span>Llamar {PHONE_DISPLAY}</span></a>
    </div>
    <div class="trust">
      <div><b>Confidencialidad</b>Secreto profesional garantizado</div>
      <div><b>Urgencias VIF</b>Medidas de protección prioritarias</div>
      <div><b>Cercanía</b>Atención online y presencial</div>
    </div>
  </div>
</section>
""")


def section_head(eyebrow: str, title: str, text: str) -> str:
    return f"""<div class="sec-head reveal"><span class="eyebrow">{eyebrow}</span><h2>{title}</h2><div class="rule"></div><p>{text}</p></div>"""


# =========================================================
# ÁREAS DE PRÁCTICA
# =========================================================
areas = [
    (icon_shield, "Protección y VIF",
     "Tramitación prioritaria de medidas cautelares y acciones penales para resguardar tu integridad.",
     ["Prohibición de acercamiento", "Salida del agresor del hogar", "Querellas por lesiones"]),
    (icon_family, "Derecho de familia",
     "Representación en los procesos que definen el bienestar de tus hijos y la estabilidad de tu hogar.",
     ["Pensión de alimentos y retención AFP", "Cuidado personal y visitas", "Divorcio"]),
    (icon_work, "Acoso laboral y Ley Karin",
     "Intervención estratégica ante acoso laboral o sexual y vulneración de derechos en el trabajo.",
     ["Tutela de derechos fundamentales", "Despido indirecto", "Despido por maternidad"]),
]
area_cards = "".join(
    f"""<article class="card reveal" style="transition-delay:{i * .12}s">
      <div class="card-icon">{ic}</div><h3>{t}</h3><p>{d}</p>
      <ul class="list">{''.join(f'<li>{x}</li>' for x in items)}</ul></article>"""
    for i, (ic, t, d, items) in enumerate(areas)
)
html(f"""
<section class="section" id="areas">
  {section_head("Áreas de práctica", "¿En qué podemos ayudarte?", "Tres especialidades con un mismo compromiso: proteger tus derechos con estrategia y con la contención que cada caso necesita.")}
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
  {section_head("Cómo trabajamos", "Un proceso claro y ordenado", "Sabrás siempre en qué punto está tu caso y cuál es el siguiente paso.")}
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
  {section_head("Equipo", "Quién estará contigo", "Atención directa con la abogada a cargo de tu causa, desde la primera reunión hasta la sentencia.")}
  <div class="team reveal">
    <div class="portrait">{portrait}</div>
    <div>
      <span class="role">Abogada fundadora</span>
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
    f'<article class="case"><span class="tag">{c}</span><h4>{t}</h4><p>{d}</p></article>'
    for c, t, d in cases
)
html(f"""
<section class="section" id="casos">
  {section_head("Resultados", "Casos destacados", "Algunas resoluciones obtenidas para nuestras clientas. Pasa el cursor para detener el carrusel.")}
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
    f"""<article class="card cred reveal" style="transition-delay:{i * .12}s">
      <div class="cred-img"><img src="{img}" alt="{t}" loading="lazy"/></div>
      <div class="cred-body"><small>{inst}</small><h4>{t}</h4><p>{d}</p></div></article>"""
    for i, (img, inst, t, d) in enumerate(creds)
)
html(f"""
<section class="section" id="formacion">
  {section_head("Formación", "Preparación que respalda tu defensa", "Especialización continua en las materias que defendemos ante tribunales.")}
  <div class="grid3">{cred_cards}</div>
</section>
""")

# =========================================================
# CONTACTO
# =========================================================
html(f"""
<section class="section" id="contacto">
  {section_head("Contacto", "Agenda tu consulta confidencial", "Cuéntanos lo esencial. Te respondemos personalmente por el medio que prefieras.")}
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
  <div><b>{BRAND}</b><div>Estudio jurídico de la mujer en Chile.</div><div>© 2026 Todos los derechos reservados.</div></div>
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
  doc.querySelectorAll('[data-theme-toggle]').forEach(b => b.setAttribute('aria-pressed', root.getAttribute('data-theme') === 'dark'));
  if (store.sget('hh-alert') === 'closed') root.classList.add('alert-closed');
  root.classList.add('js');

  // ---------- Revelado al hacer scroll ----------
  if (!win.__hhIO) {
    win.__hhIO = new win.IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); win.__hhIO.unobserve(e.target); } });
    }, { threshold: 0.14, rootMargin: '0px 0px -60px 0px' });
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
    [[1050, 400, .35, .04], [1600, 800, .14, .025]].forEach(([f0, f1, g, d]) => {
      const o = ctx.createOscillator(), gn = ctx.createGain();
      o.frequency.setValueAtTime(f0, t); o.frequency.exponentialRampToValueAtTime(f1, t + d * .85);
      gn.gain.setValueAtTime(g, t); gn.gain.exponentialRampToValueAtTime(.001, t + d);
      o.connect(gn); gn.connect(ctx.destination); o.start(t); o.stop(t + d + .01);
    });
  }

  // ---------- Cambio de tema con fundido ----------
  function setTheme(next) {
    const apply = () => {
      root.setAttribute('data-theme', next);
      doc.querySelectorAll('[data-theme-toggle]').forEach(b => b.setAttribute('aria-pressed', next === 'dark'));
      store.set('hh-theme', next);
    };
    if (doc.startViewTransition && !reduce) doc.startViewTransition(apply); else apply();
  }

  // ---------- Clics ----------
  doc.addEventListener('click', (e) => {
    if (e.target.closest('[data-theme-toggle]')) {
      e.preventDefault();
      setTheme(root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
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

  // ---------- Navbar, progreso, parallax y enlace activo ----------
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
        const hero = doc.querySelector('.hero-inner');
        if (hero && !reduce && y < 1000) {
          hero.style.transform = `translate3d(0, ${y * 0.16}px, 0)`;
          hero.style.opacity = String(Math.max(1 - y / 750, 0.2));
        }
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
