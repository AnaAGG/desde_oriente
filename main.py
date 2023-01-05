import streamlit as st
from time import sleep
from PIL import Image

# poner el ancho de la página al máximo
st.set_page_config(layout="wide")

# poner título centrado en color negro 
st.markdown("<h1 style='text-align: center; color: black;'>Protocolo P.A.C.A</h1>", unsafe_allow_html=True)
#st.markdown("<h2 style='text-align: center; color: black;'>O más conocido como Paseo-Arte-Comida-Atardecer</h2>", unsafe_allow_html=True)
#st.markdown("<h2 style='text-align: center; color: black;'>(Paseo-Arte-Comida-Atardecer)</h2>", unsafe_allow_html=True)


###########
#funciones#
###########
def cuenta_atras(num = 4, intentos = 0):
    num -= 1
    intentos += 1 
    respuesta_acertada = ["paja", "fardo", "animal", "mamifero", "hierba"]
    if num > 0:
        respuesta = st.text_input(f"¿Qué es una P.A.C.A? intento {intentos}")
        if respuesta == "":
            st.write("necesitamos tu respuesta")            
        elif respuesta in respuesta_acertada:
            st.markdown("<h1 style='text-align: center; color: black;'>LOGRO DESBLOQUEADO</h1>", unsafe_allow_html=True)
            if st.button('Pincha aqui para mas informacion'):
                col1, col2, col3,col4 = st.columns(4)

                with col1:
                    st.markdown("<h1 style='text-align: center; color: black;'>P</h1>", unsafe_allow_html=True)
                    st.image("imagenes/paseo.jpg")
                    st.markdown("**Paseo**")
                    st.write("Bonito paseo bla bla bla")

                with col2:
                    st.markdown("<h1 style='text-align: center; color: black;'>A</h1>", unsafe_allow_html=True)
                    st.image("imagenes/museo-thyssen.jpg")
                    st.markdown("**Arte**")
                    st.write("acceso a las colecciones bla bla bla")
                    st.write("Más información en este [link](https://www.museothyssen.org/)")



                with col3:
                    st.markdown("<h1 style='text-align: center; color: black;'>C</h1>", unsafe_allow_html=True)
                    st.image("imagenes/las-reses.jpg")
                    st.markdown("**Comida**")
                    st.write("En un emblematico restarante bla bla bla")
                    st.write("Más información en este [link](https://lasreses.com/)")


                with col4:
                    st.markdown("<h1 style='text-align: center; color: black;'>A</h1>", unsafe_allow_html=True)
                    st.image("imagenes/circulo.jpg")
                    st.markdown("**Atardecer**")
                    st.write("TErminaremos el día con un cafe disfrutando de los cielos y tejados de Madrid en el Circulo de Bellas Artes")
                    st.write("Más información en este [link](https://www.azoteadelcirculo.com/)")

        else:   
            st.write(f"Error, te quedan {num-1} intentos")
            cuenta_atras(num, intentos)        
    else:
        st.write("Se acabo")

#cargamos y ponemos una imagen
image = Image.open('imagenes/fondo.jpg')
st.image(image, caption='Sunrise by the mountains')
st.write("Es hora de jugar y desbloquar algunos retos para poder conseguir vuestro regalo de Reyes. Tendréis tres intentos para averiguarlo. Si fallaís, tendréis que volver mañana")

cuenta_atras()



