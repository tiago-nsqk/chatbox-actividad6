"""
Chatbot básico con Streamlit.
Ejecutar con:  streamlit run app.py
"""
import streamlit as st

# ---------------------------------------------------------------
# 1) "Personalidad" del chatbot — cámbiala por la de tu actividad
# ---------------------------------------------------------------
PERSONALIDAD = """
Eres un chatbot amigable que representa la personalidad combinada
de un grupo de estudiantes. Te gusta la música, el cine, el deporte
y ayudar a resolver dudas de forma cercana y clara.
"""

st.set_page_config(page_title="Mi Chatbot", page_icon="🤖")
st.title("🤖 Mi Chatbot")

# ---------------------------------------------------------------
# 2) Memoria de la conversación (se guarda mientras la app está abierta)
# ---------------------------------------------------------------
if "mensajes" not in st.session_state:
    st.session_state.mensajes = [
        {"role": "assistant", "content": "¡Hola! ¿En qué puedo ayudarte hoy?"}
    ]

# Mostrar el historial
for m in st.session_state.mensajes:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# ---------------------------------------------------------------
# 3) Función que genera la respuesta del bot
#    (aquí empiezas simple; luego la conectas a un modelo de IA real)
# ---------------------------------------------------------------
def generar_respuesta(texto_usuario: str) -> str:
    texto = texto_usuario.lower()
    if "hola" in texto:
        return "¡Hola! ¿Cómo estás?"
    elif "quien eres?" in texto:
        return "Hola Soy el chatbot de la actividad de bases de datos 😄"
    elif "gracias" in texto:
        return "¡Con gusto! Aquí estoy si necesitas algo más."
    elif "bien y tu?" in texto:
        return "Bien, gracias por preguntar. En qué te puedo ayudar?"
    else:
        return f"Entendí que dijiste: “{texto_usuario}”. Cuéntame más."

# ---------------------------------------------------------------
# 4) Caja de texto para chatear
# ---------------------------------------------------------------
entrada = st.chat_input("Escribe tu mensaje...")

if entrada:
    st.session_state.mensajes.append({"role": "user", "content": entrada})
    with st.chat_message("user"):
        st.write(entrada)

    respuesta = generar_respuesta(entrada)

    st.session_state.mensajes.append({"role": "assistant", "content": respuesta})
    with st.chat_message("assistant"):
        st.write(respuesta)
