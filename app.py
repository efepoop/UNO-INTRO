import streamlit as st
from PIL import Image

# =============================
# Configuración
# =============================
st.set_page_config(
    page_title="Mi Primera App — Ferxxo Vibes",
    page_icon="🟢",
    layout="wide",
)

# =============================
# Estilo FEID (neón verde) + botones pro
# =============================
STYLE = r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Chakra+Petch:wght@400;700&family=Urbanist:wght@300;500;700&display=swap');
:root{ --neon:#00FF6A; --ink:#07150b; --ink-soft:#144323; }

/* Fondo y tipografías */
[data-testid="stAppViewContainer"]{
  background: linear-gradient(180deg, #b8ffbf, #ccffd6 55%, #eafff0 100%);
  color: var(--ink);
  font-family:'Urbanist', system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
}
[data-testid="stHeader"]{ background: transparent; }

/* Header bar sutil */
.header-bar {
  width: 100%;
  padding: 8px 16px;
  border-radius: 14px;
  margin: 6px auto 12px;
  background: radial-gradient(900px 200px at 10% 0%, rgba(0,255,106,.22), transparent 70%);
  box-shadow: 0 0 0 1px rgba(0,255,106,.25);
}

/* Títulos */
h1{
  font-family:'Bebas Neue', sans-serif; text-align:center; font-size: clamp(52px, 7vw, 112px);
  letter-spacing:.5px; color:#000;
  text-shadow:0 0 24px rgba(0,255,106,.7), 0 0 44px rgba(0,255,106,.35);
  margin:.35rem 0 .2rem;
}
.subhead{
  text-align:center; font-family:'Chakra Petch', sans-serif; text-transform:uppercase; letter-spacing:.9px;
  color: var(--ink-soft); margin-top:-6px; margin-bottom:12px;
}
.hr{ height:1px; background:linear-gradient(90deg, transparent, rgba(0,255,106,.9), transparent); margin: 20px 0; }

/* Chips */
.chip {
  display:inline-block; padding:.28rem .7rem; border:2px solid var(--neon); border-radius:999px;
  font-family:'Chakra Petch', sans-serif; font-weight:800; letter-spacing:.6px; text-transform:uppercase;
  background:rgba(0,255,106,.12); color:var(--ink-soft); margin-bottom:8px;
}

/* Cards */
.card{
  background: linear-gradient(180deg, rgba(255,255,255,.95), rgba(235,255,243,.92));
  border:1px solid rgba(0,255,106,.35); border-radius:18px; padding:16px;
  box-shadow:0 8px 24px rgba(0,0,0,.06), 0 0 0 2px rgba(0,255,106,.16);
}

/* Imagen portada con borde neón */
.stImage>img{
  display:block; margin:0 auto; border-radius:16px;
  border:4px solid var(--neon); max-height:460px;
  box-shadow:0 0 18px rgba(0,255,106,.5), inset 0 0 10px rgba(0,255,106,.45);
  object-fit:cover;
}

/* Botón profesional */
.stButton>button{
  background:transparent !important; color:var(--neon) !important;
  border:2px solid var(--neon) !important; border-radius:12px;
  font-family:'Chakra Petch', sans-serif; font-weight:800; text-transform:uppercase; letter-spacing:.6px;
  padding:.7rem 1.6rem; display:block; margin:.9rem auto;
  transition: transform .25s ease, box-shadow .25s ease;
  animation: neonPulse 2.5s ease-in-out infinite;
}
.stButton>button:hover{ transform:scale(1.04); box-shadow:0 0 22px rgba(0,255,106,.6); }

@keyframes neonPulse{
  0%{ box-shadow:0 0 8px rgba(0,255,106,.4), 0 0 0 rgba(0,255,106,0); }
  50%{ box-shadow:0 0 18px rgba(0,255,106,.8), 0 0 36px rgba(0,255,106,.45); }
  100%{ box-shadow:0 0 8px rgba(0,255,106,.4), 0 0 0 rgba(0,255,106,0); }
}

/* Sidebar labels un poco más marcados */
section[data-testid="stSidebar"] div[role="radiogroup"] label{ font-weight:700; }
</style>
"""
st.markdown(STYLE, unsafe_allow_html=True)

# =============================
# Header
# =============================
st.markdown("<div class='header-bar'></div>", unsafe_allow_html=True)
st.markdown("<h1>Mi Primera App!!</h1>", unsafe_allow_html=True)
st.markdown("<div class='subhead'>Ferxxo Vibes · Interfaces multimodales</div>", unsafe_allow_html=True)
st.markdown("<div class='hr'></div>", unsafe_allow_html=True)

# =============================
# Portada + Intro
# =============================
left, right = st.columns([1,1])

with left:
    st.markdown("<div class='chip'>Intro</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("¡Bienvenid@! ✨")
    st.write("En este espacio comienzo a desarrollar mis aplicaciones para **interfaces multimodales**.")
    st.write("Puedo construir **frontend** y **backend** de forma sencilla y elegante.")
    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown("<div class='chip'>Portada</div>", unsafe_allow_html=True)
    try:
        image = Image.open('ferqui1.jpg')  # ← CAMBIADA AQUÍ
        st.image(image, caption='Ferxxo vibes · portada', use_container_width=True)
    except Exception:
        st.info("Sube la imagen 'ferqui1.jpg' para mostrar la portada.")

st.markdown("<div class='hr'></div>", unsafe_allow_html=True)

# =============================
# Entrada de texto
# =============================
st.markdown("<div class='chip'>Entrada</div>", unsafe_allow_html=True)
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("Entrada rápida")
texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es:', texto)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='hr'></div>", unsafe_allow_html=True)

# =============================
# Dos columnas (contenido)
# =============================
st.subheader("Sección de prueba (2 columnas)")
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='chip'>Columna A</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Primera columna")
    st.write("Las **interfaces multimodales** mejoran la experiencia de usuario.")
    resp = st.checkbox('Estoy de acuerdo')
    if resp:
        st.success('¡Correcto!')
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='chip'>Columna B</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Segunda columna")
    modo = st.radio("¿Cuál es la modalidad principal en tu interfaz?", ('Visual', 'Auditiva', 'Táctil'))
    if modo == 'Visual':
        st.write('La **vista** es fundamental para tu interfaz.')
    elif modo == 'Auditiva':
        st.write('La **audición** es fundamental para tu interfaz.')
    elif modo == 'Táctil':
        st.write('El **tacto** es fundamental para tu interfaz.')
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='hr'></div>", unsafe_allow_html=True)

# =============================
# Botón + Select
# =============================
st.subheader("Acciones rápidas")
st.markdown("<div class='card'>", unsafe_allow_html=True)

if st.button('Presiona el botón'):
    st.write('¡Gracias por presionar!')
else:
    st.write('No has presionado aún')

st.subheader("Selectbox")
in_mod = st.selectbox(
    "Selecciona la modalidad",
    ("Audio", "Visual", "Háptico"),
)
if in_mod == "Audio":
    set_mod = "Reproducir audio"
elif in_mod == "Visual":
    set_mod = "Reproducir video"
else:
    set_mod = "Activar vibración"
st.write("**La acción es:**", set_mod)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='hr'></div>", unsafe_allow_html=True)

# =============================
# Sidebar
# =============================
with st.sidebar:
    st.subheader("⚙️ Configura la modalidad")
    mod_radio = st.radio(
        "Escoge la modalidad a usar",
        ("Visual", "Auditiva", "Háptica"),
    )
    st.caption("Estética Ferxxo — verde neón profesional")
