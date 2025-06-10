import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Mi Primera App con Streamlit",
    page_icon="👋",
    layout="centered"
)

# Título principal
st.title("¡Hola Mundo con Streamlit!")

# Agregar algo de texto
st.write("Bienvenido a mi primera aplicación con Streamlit.")

# Agregar un subencabezado
st.header("Introducción a Streamlit")

# Texto explicativo
st.markdown("""
Streamlit es una biblioteca de Python que facilita la creación de aplicaciones web 
interactivas para ciencia de datos y machine learning en poco tiempo.
""")

# Crear un widget interactivo - Slider
edad = st.slider("¿Cuál es tu edad?", 18, 100, 25)
st.write(f"Tu edad es: {edad} años.")

# Crear un widget de entrada de texto
nombre = st.text_input("Escribe tu nombre:")
if nombre:
    st.write(f"¡Hola {nombre}! Bienvenido a la computación en la nube.")

# Selectbox para elegir una nube
nube = st.selectbox(
    "¿Qué proveedor de nube te interesa más?",
    ["AWS", "Microsoft Azure", "Google Cloud", "Oracle Cloud", "IBM Cloud"]
)
st.write(f"Has seleccionado: {nube}")

# Checkbox
if st.checkbox("Mostrar información adicional"):
    st.info("Streamlit es ideal para crear dashboards, herramientas de visualización y aplicaciones de machine learning.")
    
# Botón
if st.button("Haz clic aquí"):
    st.balloons()
    st.success("¡Felicidades! Has completado tu primera interacción.")