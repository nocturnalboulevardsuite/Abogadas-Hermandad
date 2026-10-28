import base64
import json
import os

import streamlit as st
import streamlit.components.v1 as components

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
#MainMenu, footer:not(.site-footer), header:not(.site-header), [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"] { display: none !important; }
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
.split > * { min-width: 0; }
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

/* Casos: carrusel */
.cases-carousel { position: relative; overflow: hidden; border-top: 1px solid var(--ink); padding: 28px 0 8px;
  -webkit-mask-image: linear-gradient(90deg, transparent 0, #000 6%, #000 94%, transparent 100%);
  mask-image: linear-gradient(90deg, transparent 0, #000 6%, #000 94%, transparent 100%); }
.cases-track { display: flex; width: max-content; animation: cases-scroll var(--cases-dur, 40s) linear infinite; }
.cases-carousel:hover .cases-track, .cases-carousel:focus-within .cases-track { animation-play-state: paused; }
.cases-group { display: flex; gap: 24px; padding-right: 24px; }
.case { flex: 0 0 300px; display: flex; flex-direction: column; gap: 12px; background: var(--surface); border: 1px solid var(--line);
  border-top: 2px solid var(--gold); border-radius: var(--r); padding: 28px 26px; transition: border-color .3s, transform .3s var(--ease); }
.case:hover { border-color: var(--line-2); transform: translateY(-3px); }
.case .cat { font-size: .78rem; font-weight: 600; color: var(--gold-d); letter-spacing: .06em; text-transform: uppercase; }
.case h4 { font-size: 1.4rem !important; line-height: 1.25; margin: 0; }
.case p { color: var(--muted); font-size: .92rem; line-height: 1.7; margin: 0; }
@keyframes cases-scroll { from { transform: translateX(0); } to { transform: translateX(-50%); } }
.case, .case-card, .stat, .chip, .pager-link, .crumbs a { color: var(--ink) !important; }
.chip:hover { color: var(--gold-d) !important; }
.case .more, .case-card .more { margin-top: auto; padding-top: 8px; font-size: .8rem; font-weight: 600; color: var(--ink); transition: color .3s; }
.case:hover .more, .case-card:hover .more { color: var(--gold-d); }

/* Casos: encabezado de la sección (cifras y áreas) */
.cases-head { display: grid; grid-template-columns: 320px 1fr; gap: 64px; align-items: end; margin-bottom: 44px; }
.cases-head > * { min-width: 0; }
.cases-head .sec-title .btn { margin-top: 26px; }
.cases-stats { display: grid; grid-template-columns: repeat(3, 1fr); border: 1px solid var(--line); background: var(--bg); border-radius: var(--r); }
.stat { display: flex; flex-direction: column; gap: 8px; padding: 26px 24px; color: var(--ink); transition: background-color .3s; }
.stat + .stat { border-left: 1px solid var(--line); }
.stat:hover { background: var(--band); }
.stat b { font-family: var(--serif); font-size: clamp(1.9rem, 3vw, 2.4rem); font-weight: 600; line-height: 1; color: var(--gold-d); }
.stat span { font-size: .86rem; line-height: 1.55; color: var(--muted); }
.stat em { margin-top: auto; padding-top: 6px; font-style: normal; font-size: .78rem; font-weight: 600; color: var(--ink); }
.chips { grid-column: 1 / -1; display: flex; flex-wrap: wrap; align-items: center; gap: 8px; padding: 18px 24px; border-top: 1px solid var(--line); }
.chips small { font-size: .78rem; color: var(--muted); margin-right: 6px; }
.chip { font-size: .8rem; font-weight: 500; padding: 6px 12px; border: 1px solid var(--line-2); border-radius: 999px; color: var(--ink); transition: border-color .3s, color .3s; }
.chip:hover { border-color: var(--gold); color: var(--gold-d); }
.cases-foot { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: baseline; gap: 12px; }
.cases-foot .hint { font-size: .8rem; font-weight: 500; color: var(--gold-d); margin-top: 20px; }

/* ---------- Páginas de casos ---------- */
.page-hero { background: var(--band); border-bottom: 1px solid var(--line); padding: 56px 0 0; }
.page-hero.solo { padding-bottom: 64px; }
.crumbs { display: flex; flex-wrap: wrap; gap: 10px; font-size: .8rem; color: var(--muted); margin-bottom: 36px; }
.crumbs a { color: var(--ink); border-bottom: 1px solid var(--line-2); transition: border-color .3s; }
.crumbs a:hover { border-color: var(--gold); }
.crumbs .sep { color: var(--line-2); }
.page-hero .eyebrow { display: block; font-size: .78rem; font-weight: 600; color: var(--gold-d); letter-spacing: .06em; text-transform: uppercase; margin-bottom: 14px; }
.page-hero h1 { font-size: clamp(2.4rem, 5vw, 3.8rem) !important; line-height: 1.08 !important; max-width: 22ch; margin-bottom: 20px !important; }
.page-hero .lead { font-size: 1.08rem; line-height: 1.75; color: var(--muted); max-width: 44rem; margin-bottom: 44px; }
.meta { display: grid; grid-template-columns: repeat(4, 1fr); background: var(--surface); border: 1px solid var(--line); border-bottom: none; border-radius: var(--r) var(--r) 0 0; }
.meta div { padding: 22px 24px; }
.meta div + div { border-left: 1px solid var(--line); }
.meta small { display: block; font-size: .74rem; color: var(--muted); margin-bottom: 6px; }
.meta b { font-weight: 500; font-size: .95rem; line-height: 1.45; color: var(--ink); }

.case-body { display: grid; grid-template-columns: 1fr 340px; gap: 72px; align-items: start; }
.case-body > * { min-width: 0; }
.block { padding-bottom: 44px; margin-bottom: 44px; border-bottom: 1px solid var(--line); }
.block .num { display: block; font-family: var(--serif); font-size: 1.1rem; color: var(--gold); margin-bottom: 8px; }
.block h2 { font-size: clamp(1.7rem, 2.8vw, 2.2rem) !important; line-height: 1.15; margin-bottom: 18px !important; }
.block p { color: var(--muted); font-size: 1rem; line-height: 1.85; }
.block p + p { margin-top: 14px; }
.block.last { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
.block .note { font-size: .8rem; line-height: 1.6; margin-top: 24px; }
.timeline { list-style: none; margin: 8px 0 0 6px; padding: 0; border-left: 1px solid var(--line-2); }
.timeline li { position: relative; padding: 0 0 26px 28px; margin: 0; }
.timeline li:last-child { padding-bottom: 0; }
.timeline li::before { content: ""; position: absolute; left: -7px; top: 6px; width: 13px; height: 13px; border-radius: 50%; background: var(--bg); border: 2px solid var(--gold); }
.timeline b { display: block; font-family: var(--serif); font-size: 1.25rem; font-weight: 600; color: var(--ink); margin-bottom: 4px; }
.timeline span { color: var(--muted); font-size: .95rem; line-height: 1.7; }
.keys { list-style: none; margin: 0; padding: 0; display: grid; gap: 12px; }
.keys li { display: grid; grid-template-columns: 20px 1fr; gap: 14px; padding: 18px 20px; margin: 0; background: var(--surface); border: 1px solid var(--line); border-radius: var(--r); font-size: .95rem; line-height: 1.7; color: var(--ink); }
.keys svg { stroke: var(--gold); margin-top: 4px; }

.case-aside { position: sticky; top: calc(var(--alert-h) + 100px); }
.aside-card { background: var(--deep); color: var(--deep-ink); border-radius: var(--r); padding: 32px 30px; }
.aside-card .big { display: block; font-family: var(--serif); font-size: 3rem; font-weight: 600; line-height: 1; color: #C9A45A; }
.aside-card .big-label { display: block; font-size: .84rem; line-height: 1.5; color: rgba(245,241,232,.7); margin: 10px 0 24px; padding-bottom: 24px; border-bottom: 1px solid rgba(245,241,232,.15); }
.aside-card h3 { color: var(--deep-ink) !important; font-size: 1.6rem !important; line-height: 1.2; margin-bottom: 10px !important; }
.aside-card p { color: rgba(245,241,232,.75); font-size: .92rem; line-height: 1.7; margin-bottom: 22px; }
.aside-card .btn { width: 100%; justify-content: center; margin-bottom: 10px; background: #C9A45A; border-color: #C9A45A; color: #161514 !important; }
.aside-card .btn:hover { background: #F5F1E8; border-color: #F5F1E8; color: #161514 !important; }
.aside-card .btn.ghost { background: transparent; border-color: rgba(245,241,232,.35); color: #F5F1E8 !important; }
.aside-card .btn.ghost:hover { border-color: #F5F1E8; }
.aside-card .fine { font-size: .78rem; line-height: 1.6; color: rgba(245,241,232,.6); margin: 10px 0 0; }

.case-pager { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 72px; }
.pager-link { display: block; padding: 24px 26px; border: 1px solid var(--line); border-radius: var(--r); background: var(--bg); color: var(--ink); transition: border-color .3s; }
.pager-link:hover { border-color: var(--gold); }
.pager-link small { display: block; font-size: .76rem; color: var(--muted); margin-bottom: 6px; }
.pager-link b { font-family: var(--serif); font-size: 1.35rem; font-weight: 600; }
.pager-link.next { text-align: right; }
.cases-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; }
.case-card { display: flex; flex-direction: column; gap: 12px; padding: 28px 26px; background: var(--surface); border: 1px solid var(--line); border-top: 2px solid var(--gold); border-radius: var(--r); color: var(--ink); transition: border-color .3s, transform .3s var(--ease); }
.section.alt .case-card { background: var(--bg); }
.case-card:hover { border-color: var(--line-2); transform: translateY(-3px); }
.case-card .cat { font-size: .78rem; font-weight: 600; color: var(--gold-d); letter-spacing: .06em; text-transform: uppercase; }
.case-card h3 { font-size: 1.5rem !important; line-height: 1.2; }
.case-card p { color: var(--muted); font-size: .92rem; line-height: 1.7; }
.cta-band { background: var(--deep); color: var(--deep-ink); padding: 72px 0; text-align: center; border-bottom: 1px solid rgba(245,241,232,.12); }
.cta-band h2 { color: var(--deep-ink) !important; font-size: clamp(1.9rem, 3.4vw, 2.6rem) !important; margin-bottom: 14px !important; }
.cta-band p { color: rgba(245,241,232,.75); max-width: 36rem; margin: 0 auto 28px; line-height: 1.7; }
.cta-band .actions { display: flex; justify-content: center; flex-wrap: wrap; gap: 12px; }
.cta-band .btn { background: #C9A45A; border-color: #C9A45A; color: #161514 !important; }
.cta-band .btn:hover { background: #F5F1E8; border-color: #F5F1E8; color: #161514 !important; }
.cta-band .btn.ghost { background: transparent; border-color: rgba(245,241,232,.35); color: #F5F1E8 !important; }
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
  .case { flex-basis: 260px; padding: 24px 22px; }
  .cases-head { grid-template-columns: 1fr; gap: 32px; }
  .cases-stats { grid-template-columns: 1fr; }
  .stat + .stat { border-left: none; border-top: 1px solid var(--line); }
  .meta { grid-template-columns: 1fr 1fr; }
  .meta div:nth-child(odd) { border-left: none; }
  .meta div:nth-child(n+3) { border-top: 1px solid var(--line); }
  .case-body { grid-template-columns: 1fr; gap: 40px; }
  .case-aside { position: static; }
  .case-pager { grid-template-columns: 1fr; }
  .page-hero { padding-top: 36px; }
  .cases-group { gap: 16px; padding-right: 16px; }
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
  .cases-carousel { overflow-x: auto; -webkit-mask-image: none; mask-image: none; }
  .cases-group[aria-hidden="true"] { display: none; }
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
# RUTAS
# La portada vive en "/". Cada caso destacado tiene su propia
# página en "?caso=<identificador>" y el listado completo en "?caso=todos".
# =========================================================
def leer_vista():
    try:
        valor = st.query_params.get("caso")
    except AttributeError:  # Versiones antiguas de Streamlit
        valor = st.experimental_get_query_params().get("caso", [None])[0]
    if isinstance(valor, list):
        valor = valor[0] if valor else None
    return (valor or "").strip().lower() or None


VISTA = leer_vista()


def ancla(seccion: str) -> str:
    """Enlace a una sección de la portada: scroll suave en la portada y navegación desde las demás páginas."""
    if VISTA:
        return f'href="./#{seccion}" target="_self" data-nav'
    return f'href="#{seccion}" data-scroll="{seccion}"'


def enlace_caso(slug: str) -> str:
    return f'href="?caso={slug}" target="_self" data-nav'


INICIO_LINK = 'href="./" target="_self" data-nav' if VISTA else 'href="#inicio" data-scroll="inicio"'


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
    <a class="brand" {INICIO_LINK} aria-label="{BRAND}, ir al inicio">{logo}
      <span><span class="brand-name">{BRAND}</span><span class="brand-sub">Estudio jurídico de la mujer</span></span></a>
    <nav class="nav" aria-label="Navegación principal">
      <a class="nl" {ancla("areas")}>Áreas de práctica</a>
      <a class="nl" {ancla("equipo")}>Equipo</a>
      <a class="nl" {ancla("casos") if not VISTA else enlace_caso("todos")}>Casos</a>
      <a class="btn" {ancla("contacto")}>Agendar consulta</a>
    </nav>
  </div>
</header>
<button class="theme-fab" type="button" data-theme-toggle aria-label="Cambiar entre tema claro y oscuro" aria-pressed="false">
  {fab_scale}<span class="tip"><span class="tip-light">Tema oscuro</span><span class="tip-dark">Tema claro</span></span>
</button>
<a class="wa" href="{WA_LINK}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp">{icon_wa}</a>
""")

# =========================================================
# CASOS DESTACADOS (datos)
# Para agregar un caso, copia un bloque y cambia el "slug" (identificador
# único que aparece en la dirección de la página).
# =========================================================
NOTA_CASOS = "Los resultados anteriores no garantizan resultados futuros. Cada caso se evalúa de forma individual."
NOTA_ANONIMATO = ("Los datos de las clientas y de las partes se han omitido o modificado para proteger su identidad. "
                  "El relato se publica con autorización.")

CASOS = [
    {
        "slug": "medida-cautelar-24-horas",
        "cat": "Protección y VIF",
        "titulo": "Medida cautelar en 24 horas",
        "resumen": "Prohibición de acercamiento y salida del agresor del hogar común, otorgadas por el Juzgado de Familia de Santiago.",
        "tribunal": "Juzgado de Familia de Santiago",
        "materia": "Violencia intrafamiliar (Ley 20.066)",
        "logro": "Medidas de protección otorgadas en menos de 24 horas",
        "dato": ("24 h", "para obtener la prohibición de acercamiento y la salida del agresor del hogar"),
        "contexto": [
            "Nuestra clienta convivía con su pareja y llevaba meses viviendo episodios de violencia psicológica que, en las últimas semanas, habían escalado a amenazas y agresiones físicas. Temía por su seguridad y la de sus hijos, pero no sabía si podía pedir que él dejara la casa que compartían.",
            "Llegó a la primera reunión sin denuncia previa y con un temor muy comprensible: que iniciar una acción judicial empeorara la situación en el hogar.",
        ],
        "estrategia": [
            "La prioridad fue su seguridad inmediata. Ese mismo día ordenamos los antecedentes disponibles —mensajes, fotografías, registros de atención médica y el relato de una testigo— y presentamos la denuncia junto con una solicitud de medidas cautelares urgentes ante el Juzgado de Familia.",
            "En la solicitud describimos con precisión el riesgo actual y concreto, para que el tribunal pudiera resolver sin esperar a la audiencia. En paralelo, preparamos con ella un plan de seguridad para las horas siguientes.",
        ],
        "resultado": [
            "En menos de 24 horas el tribunal decretó la prohibición de acercamiento a la clienta, a su domicilio y a su lugar de trabajo, y ordenó la salida del agresor del hogar común con el apoyo de Carabineros.",
            "Con su seguridad resguardada, la causa siguió su curso y pudimos abordar con calma los temas de fondo: la pensión de alimentos y la relación de los niños con su padre en condiciones seguras.",
        ],
        "etapas": [
            ("Primera reunión", "Evaluación del riesgo y revisión de los antecedentes, con total reserva."),
            ("Denuncia y solicitud urgente", "Presentación ante el Juzgado de Familia el mismo día."),
            ("Resolución del tribunal", "Medidas cautelares decretadas en menos de 24 horas."),
            ("Seguimiento", "Control del cumplimiento de las medidas y continuación de la causa."),
        ],
        "claves": [
            "No necesitas una denuncia previa: las medidas de protección pueden pedirse junto con la denuncia.",
            "El tribunal puede ordenar que el agresor abandone el hogar común aunque la vivienda no esté a tu nombre.",
            "Si una medida se incumple, avisa de inmediato a Carabineros (133) y al tribunal: el incumplimiento tiene consecuencias penales.",
        ],
    },
    {
        "slug": "retencion-fondos-afp",
        "cat": "Pensión de alimentos",
        "titulo": "Retención de fondos AFP",
        "resumen": "Cobro de una deuda histórica superior a $14.000.000 mediante retención judicial de fondos previsionales.",
        "tribunal": "Juzgado de Familia",
        "materia": "Cumplimiento de alimentos (Ley 21.484)",
        "logro": "Deuda superior a $14.000.000 pagada con fondos previsionales",
        "dato": ("+$14 M", "de deuda de alimentos recuperada mediante retención de fondos AFP"),
        "contexto": [
            "Durante años, el padre de los hijos de nuestra clienta dejó de pagar la pensión de alimentos fijada por el tribunal. Los apremios tradicionales no habían dado resultado y la deuda acumulada ya superaba los catorce millones de pesos.",
            "Ella había asumido sola todos los gastos de los niños y creía que esa deuda era, en la práctica, imposible de cobrar.",
        ],
        "estrategia": [
            "Comenzamos por pedir una liquidación actualizada de la deuda, que es la base de cualquier medida de cobro. Con la deuda acreditada, solicitamos la inscripción del deudor en el Registro Nacional de Deudores de Pensiones de Alimentos.",
            "Luego activamos las herramientas de la Ley 21.484 sobre pago efectivo de deudas de alimentos: pedimos al tribunal información sobre los fondos del deudor y la retención de lo adeudado desde su cuenta de capitalización individual en la AFP.",
        ],
        "resultado": [
            "El tribunal ordenó a la AFP retener y transferir los fondos necesarios para cubrir la deuda, que fue pagada íntegramente a nuestra clienta.",
            "Además, la inscripción en el registro mantiene un incentivo concreto para que las pensiones futuras se paguen a tiempo.",
        ],
        "etapas": [
            ("Revisión de la causa", "Análisis del historial de pagos y de los apremios ya intentados."),
            ("Liquidación de la deuda", "Cálculo actualizado de lo adeudado, aprobado por el tribunal."),
            ("Registro y búsqueda de fondos", "Inscripción del deudor e informe de sus fondos previsionales."),
            ("Retención y pago", "Orden a la AFP y transferencia de los fondos a la clienta."),
        ],
        "claves": [
            "La ley permite pagar deudas de alimentos con los fondos de la cuenta AFP del deudor.",
            "Una liquidación actualizada de la deuda es el primer paso para pedir cualquier medida de cobro.",
            "La inscripción en el Registro Nacional de Deudores trae consecuencias como la retención de devoluciones de impuestos y restricciones en ciertos trámites.",
        ],
    },
    {
        "slug": "acoso-laboral-ley-karin",
        "cat": "Tutela laboral",
        "titulo": "Acoso laboral, Ley Karin",
        "resumen": "Sentencia favorable con indemnización por vulneración de derechos fundamentales y despido indirecto.",
        "tribunal": "Juzgado de Letras del Trabajo",
        "materia": "Tutela de derechos fundamentales y despido indirecto",
        "logro": "Sentencia favorable con indemnizaciones legales y adicionales",
        "dato": ("Ley Karin", "sentencia favorable por acoso laboral y vulneración de derechos"),
        "contexto": [
            "Nuestra clienta sufría un hostigamiento sistemático por parte de su jefatura: descalificaciones frente al equipo, aislamiento, cambios arbitrarios de funciones y comentarios sobre su vida personal. Su salud se vio afectada y debió tomar licencia médica.",
            "Había hecho una denuncia interna, pero la empresa no investigó adecuadamente ni adoptó medidas para protegerla.",
        ],
        "estrategia": [
            "Reunimos y ordenamos la prueba: correos, mensajes, certificados médicos, la denuncia interna sin respuesta y el testimonio de compañeras que presenciaron los hechos.",
            "Con esos antecedentes, la clienta puso término a su contrato mediante despido indirecto, con una carta debidamente fundada en los incumplimientos graves del empleador. Dentro del plazo legal, presentamos una demanda de tutela de derechos fundamentales ante el Juzgado de Letras del Trabajo.",
        ],
        "resultado": [
            "La sentencia reconoció la vulneración de los derechos fundamentales de nuestra clienta y acogió el despido indirecto.",
            "La empresa fue condenada al pago de las indemnizaciones legales con sus recargos y de una indemnización adicional por la vulneración de derechos.",
        ],
        "etapas": [
            ("Evaluación del caso", "Revisión de los hechos, la prueba disponible y los plazos."),
            ("Despido indirecto", "Carta de término fundada en los incumplimientos del empleador."),
            ("Demanda de tutela", "Presentación ante el Juzgado de Letras del Trabajo."),
            ("Juicio y sentencia", "Audiencias, prueba testimonial y documental, y sentencia favorable."),
        ],
        "claves": [
            "Desde la Ley Karin (Ley 21.643), los empleadores deben tener un protocolo de prevención y un procedimiento para investigar el acoso.",
            "El despido indirecto permite terminar el contrato por incumplimientos graves del empleador y reclamar las indemnizaciones.",
            "Los plazos son breves: en general, 60 días hábiles desde el término del contrato para demandar.",
        ],
    },
    {
        "slug": "cuidado-personal-definitivo",
        "cat": "Derecho de familia",
        "titulo": "Cuidado personal definitivo",
        "resumen": "Resolución que resguarda el interés superior del niño, con régimen de visitas y evaluación psicológica.",
        "tribunal": "Juzgado de Familia",
        "materia": "Cuidado personal y relación directa y regular",
        "logro": "Cuidado personal definitivo con régimen de visitas",
        "dato": ("Definitivo", "cuidado personal otorgado en resguardo del interés superior del niño"),
        "contexto": [
            "Tras una separación conflictiva, los hijos de nuestra clienta vivían con ella, pero no existía ninguna resolución judicial que lo reconociera. El padre amenazaba con no devolverlos después de las visitas y la incertidumbre afectaba la rutina y la tranquilidad de los niños.",
        ],
        "estrategia": [
            "Presentamos una demanda de cuidado personal centrada en lo que más importa al tribunal: el bienestar de los niños. Acreditamos su rutina, su escolaridad, su salud y la red de apoyo con que contaban en el hogar materno.",
            "Solicitamos una evaluación psicológica y que los niños fueran escuchados por el tribunal, con el debido resguardo. Además, propusimos un régimen de relación directa y regular razonable para el padre, mostrando que el objetivo no era alejarlo, sino dar estabilidad.",
        ],
        "resultado": [
            "El tribunal otorgó el cuidado personal definitivo a nuestra clienta y fijó un régimen de visitas claro, con días, horarios y condiciones de entrega, en resguardo del interés superior de los niños.",
            "Con reglas claras, la familia dejó atrás la incertidumbre y los conflictos en cada entrega.",
        ],
        "etapas": [
            ("Primera reunión", "Análisis de la situación familiar y de las pruebas disponibles."),
            ("Demanda", "Presentación de la demanda de cuidado personal y propuesta de visitas."),
            ("Evaluación y audiencia", "Evaluación psicológica y audiencia en que se escuchó a los niños."),
            ("Sentencia", "Cuidado personal definitivo y régimen de visitas fijado por el tribunal."),
        ],
        "claves": [
            "El tribunal decide según el interés superior del niño, no según quién gane el conflicto entre los padres.",
            "Los niños tienen derecho a ser oídos en el proceso, de acuerdo con su edad y madurez.",
            "Proponer un régimen de visitas razonable para el otro progenitor fortalece tu posición ante el tribunal.",
        ],
    },
    {
        "slug": "querella-lesiones-vif",
        "cat": "Derecho penal",
        "titulo": "Querella por lesiones VIF",
        "resumen": "Condena firme del Tribunal de Juicio Oral en lo Penal con prohibición absoluta de contacto.",
        "tribunal": "Tribunal de Juicio Oral en lo Penal",
        "materia": "Lesiones en contexto de violencia intrafamiliar",
        "logro": "Condena firme con prohibición absoluta de contacto",
        "dato": ("Condena", "firme en juicio oral, con prohibición absoluta de contacto"),
        "contexto": [
            "Nuestra clienta fue víctima de una agresión física grave por parte de su expareja, que le causó lesiones acreditadas por un médico. No era el primer episodio, y temía que el proceso penal terminara sin consecuencias reales para el agresor.",
        ],
        "estrategia": [
            "Presentamos una querella criminal para que ella participara activamente en el proceso como víctima, y no solo como testigo. Trabajamos coordinadamente con la Fiscalía y pedimos diligencias clave: peritajes médico-legales, declaraciones de testigos y los antecedentes de episodios anteriores.",
            "Durante la investigación solicitamos medidas cautelares para protegerla y la preparamos para el juicio oral, de modo que pudiera declarar con seguridad y respaldo.",
        ],
        "resultado": [
            "El Tribunal de Juicio Oral en lo Penal condenó al agresor por el delito de lesiones en contexto de violencia intrafamiliar y le impuso la prohibición absoluta de contacto con nuestra clienta.",
            "La sentencia quedó firme, lo que entrega una protección duradera y respaldada por la ley.",
        ],
        "etapas": [
            ("Querella", "Presentación de la querella y solicitud de medidas cautelares."),
            ("Investigación", "Diligencias, peritajes y coordinación con la Fiscalía."),
            ("Preparación del juicio", "Acompañamiento a la clienta y revisión de la prueba."),
            ("Juicio oral y condena", "Sentencia condenatoria que quedó firme."),
        ],
        "claves": [
            "Como víctima puedes presentar una querella y participar activamente en el proceso, además del trabajo de la Fiscalía.",
            "Durante la investigación pueden decretarse medidas cautelares para protegerte.",
            "Guardar evidencia (fotografías, mensajes, atenciones médicas) es fundamental para el éxito del juicio.",
        ],
    },
]
CASOS_POR_SLUG = {c["slug"]: c for c in CASOS}
# Cifras que se muestran sobre el carrusel (deben corresponder a casos reales de la lista).
CASOS_EN_CIFRAS = ["medida-cautelar-24-horas", "retencion-fondos-afp", "querella-lesiones-vif"]

icon_check = icon('<path d="M20 6L9 17l-5-5"/>', 18)


def tarjeta_carrusel(c: dict, copia: bool = False) -> str:
    extra = ' tabindex="-1"' if copia else ""
    return (f'<a class="case" {enlace_caso(c["slug"])}{extra}><span class="cat">{c["cat"]}</span>'
            f'<h4>{c["titulo"]}</h4><p>{c["resumen"]}</p><span class="more">Ver caso completo →</span></a>')


def tarjeta_grilla(c: dict) -> str:
    return (f'<a class="case-card" {enlace_caso(c["slug"])}><span class="cat">{c["cat"]}</span>'
            f'<h3>{c["titulo"]}</h3><p>{c["resumen"]}</p><span class="more">Leer caso completo →</span></a>')


def mayus(texto: str) -> str:
    return texto[:1].upper() + texto[1:]


def bloque_cifras() -> str:
    stats = "".join(
        f'<a class="stat" {enlace_caso(s)}><b>{CASOS_POR_SLUG[s]["dato"][0]}</b>'
        f'<span>{mayus(CASOS_POR_SLUG[s]["dato"][1])}</span><em>{CASOS_POR_SLUG[s]["titulo"]} →</em></a>'
        for s in CASOS_EN_CIFRAS if s in CASOS_POR_SLUG
    )
    chips = "".join(f'<a class="chip" {enlace_caso(c["slug"])}>{c["cat"]}</a>' for c in CASOS)
    return f'<div class="cases-stats t">{stats}<div class="chips"><small>Explorar por área:</small>{chips}</div></div>'


# =========================================================
# PIE DE PÁGINA E INTERACCIONES (compartidos por todas las páginas)
# =========================================================
def render_footer(espaciador: bool = True) -> None:
    html(f"""
<div style="height:{72 if espaciador else 0}px"></div>
<footer class="site-footer">
  <div class="wrap">
    <div><b>{BRAND}</b><div>Estudio jurídico de la mujer en Chile.</div></div>
    <div><div><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div><div><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
    <div><div><a {ancla("areas")}>Áreas de práctica</a></div><div><a {ancla("equipo")}>Equipo</a></div><div><a {enlace_caso("todos")}>Casos destacados</a></div><div><a {ancla("contacto")}>Agendar consulta</a></div></div>
  </div>
  <div class="legal">© 2026 {BRAND}. Todos los derechos reservados.</div>
</footer>
""")


# =========================================================
# INTERACCIONES (tema, aviso, scroll suave y aparición sutil)
# El código se ejecuta en la página principal (no dentro del iframe del
# componente). Así los clics siguen funcionando aunque Streamlit vuelva
# a crear el iframe al recargar.
# =========================================================
PAGE_JS = """
(function () {
  const win = window, doc = document, root = doc.documentElement;
  const reduce = win.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const get = (s, k) => { try { return win[s].getItem(k); } catch (e) { return null; } };
  const set = (s, k, v) => { try { win[s].setItem(k, v); } catch (e) {} };

  function syncState() {
    if (!root.getAttribute('data-theme')) root.setAttribute('data-theme', get('localStorage', 'hh-theme') || 'light');
    const dark = root.getAttribute('data-theme') === 'dark';
    doc.querySelectorAll('[data-theme-toggle]').forEach(b => b.setAttribute('aria-pressed', dark ? 'true' : 'false'));
    if (get('sessionStorage', 'hh-alert') === 'closed') root.classList.add('alert-closed');
    root.classList.add('js');
  }

  const io = new win.IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  }), { threshold: 0.12 });
  function observe() {
    doc.querySelectorAll('.reveal:not(.in)').forEach(el => reduce ? el.classList.add('in') : io.observe(el));
  }
  function refresh() {
    syncState();
    observe();
    syncTitle();
    scrollToHash();
    setTimeout(() => doc.querySelectorAll('.reveal:not(.in)').forEach(el => {
      const r = el.getBoundingClientRect(); if (r.top < win.innerHeight) el.classList.add('in');
    }), 1200);
  }
  win.__hhRefresh = refresh;

  // Título de la pestaña en las páginas de casos
  function syncTitle() {
    const el = doc.querySelector('[data-page-title]');
    if (el && doc.title !== el.dataset.pageTitle) doc.title = el.dataset.pageTitle;
  }
  // Al llegar desde otra página con #seccion, se desplaza a esa sección cuando ya existe
  function scrollToHash() {
    if (win.__hhHashDone || !win.location.hash) return;
    const el = doc.getElementById(decodeURIComponent(win.location.hash.slice(1)));
    if (!el) return;
    win.__hhHashDone = true;
    setTimeout(() => el.scrollIntoView({ behavior: 'auto', block: 'start' }), 400);
  }
  new win.MutationObserver(() => { syncState(); observe(); syncTitle(); scrollToHash(); }).observe(doc.body, { childList: true, subtree: true });

  function setTheme(next) {
    const apply = () => {
      root.setAttribute('data-theme', next);
      doc.querySelectorAll('[data-theme-toggle]').forEach(b => b.setAttribute('aria-pressed', next === 'dark' ? 'true' : 'false'));
      set('localStorage', 'hh-theme', next);
    };
    if (doc.startViewTransition && !reduce) { try { doc.startViewTransition(apply); } catch (e) { apply(); } }
    else apply();
  }

  doc.addEventListener('click', (e) => {
    const t = e.target;
    if (!t || !t.closest) return;
    if (t.closest('.theme-fab, [data-theme-toggle]')) {
      e.preventDefault();
      setTheme(root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
      return;
    }
    if (t.closest('.alert-close, [data-close-alert]')) {
      e.preventDefault();
      root.classList.add('alert-closed');
      set('sessionStorage', 'hh-alert', 'closed');
      return;
    }
    // Enlaces entre páginas (casos, listado, portada): siempre en la misma pestaña
    const nav = t.closest('a[data-nav]');
    if (nav) {
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button === 1) return;
      e.preventDefault();
      win.location.href = nav.href;
      return;
    }
    const link = t.closest('[data-scroll]');
    if (link) {
      const target = doc.getElementById(link.getAttribute('data-scroll'));
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
    }
  }, true);

  win.__hhReady = true;
  refresh();
})();
"""

def activar_interacciones() -> None:
    """Ejecuta PAGE_JS en la página principal.

    En Streamlit reciente se usa st.html (sin iframe). En versiones antiguas
    se usa un componente que inserta el script en la página principal.
    """
    runner = (
        "<script>(function(){"
        "if (window.__hhReady) { if (window.__hhRefresh) window.__hhRefresh(); return; }"
        + PAGE_JS +
        "})();</script>"
    )
    try:
        st.html(runner, unsafe_allow_javascript=True)
        return
    except (TypeError, AttributeError):
        pass  # Versión de Streamlit sin esta opción: se usa el respaldo

    components.html(
        """
<script>
(function () {
  const pwin = window.parent, pdoc = pwin.document;
  const code = """ + json.dumps(PAGE_JS) + """;
  if (pwin.__hhReady) { if (pwin.__hhRefresh) pwin.__hhRefresh(); return; }
  try {
    const s = pdoc.createElement('script');
    s.id = 'hh-runtime';
    s.textContent = code;
    pdoc.head.appendChild(s);
  } catch (e) {}
  if (!pwin.__hhReady) { try { new pwin.Function(code)(); } catch (e) { console.error('No se pudieron activar las interacciones:', e); } }
})();
</script>
""",
        height=0,
        width=0,
    )


# =========================================================
# PÁGINAS DE CASOS
# =========================================================
def parrafos(lista) -> str:
    return "".join(f"<p>{p}</p>" for p in lista)


def render_pagina_caso(c: dict) -> None:
    i = CASOS.index(c)
    anterior, siguiente = CASOS[i - 1], CASOS[(i + 1) % len(CASOS)]
    etapas = "".join(f"<li><b>{t}</b><span>{d}</span></li>" for t, d in c["etapas"])
    claves = "".join(f"<li>{icon_check}<span>{k}</span></li>" for k in c["claves"])
    otros = "".join(tarjeta_grilla(o) for o in CASOS if o is not c)
    html(f"""
<div hidden data-page-title="{c['titulo']} | {BRAND}"></div>
<section class="page-hero t">
  <div class="wrap">
    <nav class="crumbs" aria-label="Ruta de navegación">
      <a {INICIO_LINK}>Inicio</a><span class="sep">/</span><a {enlace_caso("todos")}>Casos destacados</a><span class="sep">/</span><span aria-current="page">{c['titulo']}</span>
    </nav>
    <span class="eyebrow">{c['cat']}</span>
    <h1>{c['titulo']}</h1>
    <p class="lead">{c['resumen']}</p>
    <div class="meta t">
      <div><small>Área</small><b>{c['cat']}</b></div>
      <div><small>Tribunal</small><b>{c['tribunal']}</b></div>
      <div><small>Materia</small><b>{c['materia']}</b></div>
      <div><small>Resultado</small><b>{c['logro']}</b></div>
    </div>
  </div>
</section>
<section class="section t">
  <div class="wrap case-body">
    <article>
      <div class="block reveal"><span class="num">01</span><h2>La situación</h2>{parrafos(c['contexto'])}</div>
      <div class="block reveal"><span class="num">02</span><h2>Nuestra estrategia</h2>{parrafos(c['estrategia'])}</div>
      <div class="block reveal"><span class="num">03</span><h2>Etapas del proceso</h2><ol class="timeline">{etapas}</ol></div>
      <div class="block reveal"><span class="num">04</span><h2>El resultado</h2>{parrafos(c['resultado'])}</div>
      <div class="block last reveal"><span class="num">05</span><h2>Lo que debes saber</h2>
        <ul class="keys">{claves}</ul>
        <p class="note">{NOTA_ANONIMATO} {NOTA_CASOS}</p>
      </div>
    </article>
    <aside class="case-aside">
      <div class="aside-card">
        <span class="big">{c['dato'][0]}</span>
        <span class="big-label">{mayus(c['dato'][1])}</span>
        <h3>¿Vives una situación parecida?</h3>
        <p>Cuéntanos lo esencial con total reserva. Te explicamos tus opciones y los pasos a seguir, sin compromiso.</p>
        <a class="btn" {ancla("contacto")}>Agendar consulta confidencial</a>
        <a class="btn ghost" href="{WA_LINK}" target="_blank" rel="noopener">Escribir por WhatsApp</a>
        <p class="fine">O llámanos al <a href="tel:{PHONE_TEL}" style="color:#F5F1E8;border-bottom:1px solid rgba(245,241,232,.4)">{PHONE_DISPLAY}</a>. Todo lo que compartas está protegido por secreto profesional.</p>
      </div>
    </aside>
  </div>
</section>
<section class="section alt t">
  <div class="wrap">
    <div class="case-pager">
      <a class="pager-link" {enlace_caso(anterior['slug'])}><small>← Caso anterior</small><b>{anterior['titulo']}</b></a>
      <a class="pager-link next" {enlace_caso(siguiente['slug'])}><small>Caso siguiente →</small><b>{siguiente['titulo']}</b></a>
    </div>
    <div class="sec-title reveal" style="margin-bottom:32px">
      <span class="eyebrow">Sigue leyendo</span>
      <h2>Otros casos destacados</h2>
    </div>
    <div class="cases-grid">{otros}</div>
  </div>
</section>
""")


def render_pagina_todos() -> None:
    tarjetas = "".join(tarjeta_grilla(c) for c in CASOS)
    html(f"""
<div hidden data-page-title="Casos destacados | {BRAND}"></div>
<section class="page-hero solo t">
  <div class="wrap">
    <nav class="crumbs" aria-label="Ruta de navegación">
      <a {INICIO_LINK}>Inicio</a><span class="sep">/</span><span aria-current="page">Casos destacados</span>
    </nav>
    <span class="eyebrow">Resultados</span>
    <h1>Casos destacados</h1>
    <p class="lead">Resoluciones obtenidas para nuestras clientas, contadas paso a paso: la situación de la que partimos, la estrategia, las etapas del proceso y el resultado. Todos los casos se presentan de forma anónima.</p>
    {bloque_cifras()}
  </div>
</section>
<section class="section t">
  <div class="wrap">
    <div class="cases-grid">{tarjetas}</div>
    <p class="note">{NOTA_ANONIMATO} {NOTA_CASOS}</p>
  </div>
</section>
<section class="cta-band">
  <div class="wrap">
    <h2>Cada caso es distinto. El tuyo también.</h2>
    <p>La primera conversación sirve para entender tu situación y explicarte tus opciones, con total reserva y sin compromiso.</p>
    <div class="actions">
      <a class="btn" {ancla("contacto")}>Agendar consulta confidencial</a>
      <a class="btn ghost" href="{WA_LINK}" target="_blank" rel="noopener">Escribir por WhatsApp</a>
    </div>
  </div>
</section>
""")


# Si la dirección pide un caso (o el listado), se muestra esa página y se detiene aquí.
if VISTA:
    caso_actual = CASOS_POR_SLUG.get(VISTA)
    if caso_actual:
        render_pagina_caso(caso_actual)
        render_footer()
    else:
        render_pagina_todos()
        render_footer(espaciador=False)
    activar_interacciones()
    st.stop()


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
cases_cards = "".join(tarjeta_carrusel(c) for c in CASOS)
cases_cards_copia = "".join(tarjeta_carrusel(c, copia=True) for c in CASOS)
# El grupo se duplica para que el giro sea continuo; la copia se oculta a lectores de pantalla.
cases_html = (
    f'<div class="cases-track" style="--cases-dur:{len(CASOS) * 8}s">'
    f'<div class="cases-group">{cases_cards}</div>'
    f'<div class="cases-group" aria-hidden="true">{cases_cards_copia}</div>'
    f'</div>'
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
  <div class="wrap">
    <div class="cases-head">
      <div class="sec-title reveal">
        <span class="eyebrow">Resultados</span>
        <h2>Casos destacados</h2>
        <p>Algunas resoluciones obtenidas para nuestras clientas, presentadas de forma anónima. Toca un caso para conocerlo a fondo.</p>
        <a class="btn ghost" {enlace_caso("todos")}>Ver todos los casos →</a>
      </div>
      <div class="reveal">{bloque_cifras()}</div>
    </div>
  </div>
  <div class="wrap reveal">
    <div class="cases-carousel" aria-label="Casos destacados">{cases_html}</div>
    <div class="cases-foot">
      <p class="note">{NOTA_CASOS}</p>
      <span class="hint">Pasa el cursor para pausar el carrusel</span>
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
render_footer()
activar_interacciones()
