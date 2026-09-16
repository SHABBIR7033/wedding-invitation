import base64
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Wedding Invitation",
    page_icon="💍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).parent
HTML_FILE = BASE_DIR / "wedding_invitation.html"
MUSIC_FILE = BASE_DIR / "assets" / "wedding-music.mp3"

@st.cache_data
def load_invitation():
    html = HTML_FILE.read_text(encoding="utf-8")

    if MUSIC_FILE.exists():
        data = base64.b64encode(MUSIC_FILE.read_bytes()).decode("ascii")
        music_url = f"data:audio/mpeg;base64,{data}"
    else:
        music_url = ""

    return html.replace("__STREAMLIT_MUSIC_DATA__", music_url)

html = load_invitation()

# Keep Streamlit's top bar/menu visible so the deployed app retains its
# native Share / app menu controls. Only remove unnecessary content spacing.
st.markdown(
    """
    <style>
      [data-testid="stAppViewContainer"] {padding:0!important;}
      [data-testid="stMainBlockContainer"] {
          padding:4.5rem 0 0!important;
          max-width:none!important;
      }
      iframe {display:block;width:100%!important;border:0!important;}
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(
    html,
    height=1100,
    scrolling=True,
)
