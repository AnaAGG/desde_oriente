import streamlit as st
from time import sleep
from PIL import Image
import time
# poner el ancho de la página al máximo
st.set_page_config(layout="wide")

# poner título centrado en color negro 
st.markdown("<h1 style='text-align: center; color: black;'>Protocolo P.A.C.A</h1>", unsafe_allow_html=True)
#st.markdown("<h2 style='text-align: center; color: black;'>O más conocido como Paseo-Arte-Comida-Atardecer</h2>", unsafe_allow_html=True)
#st.markdown("<h2 style='text-align: center; color: black;'>(Paseo-Arte-Comida-Atardecer)</h2>", unsafe_allow_html=True)


###########
#funciones#
###########
def adivina_escribiendo(num = 4, intentos = 0):
    num -= 1
    intentos += 1 
    respuesta_acertada = ["paja", "fardo", "animal", "mamifero", "hierba"]
    if num > 0:
        st.markdown(f"<h4 style='text-align: legft; color: black;'>📝El tercer reto consiste en saber qué es lo que significa la palabra PACA, en este caso tendréis que escribirlo vosotros</h4>", unsafe_allow_html=True)

        respuesta = st.text_input(f"Intento {intentos} de 3")
        if respuesta == "":
            st.write("necesitamos tu respuesta")            
        elif respuesta in respuesta_acertada:
            st.markdown("<h1 style='text-align: center; color: black;'>TODOS LOS LOGROS HAN SIDO DESBLOQUEADOS</h1>", unsafe_allow_html=True)
            st.markdown("<h3 style='text-align: center; color: black;'>Veamos en que consiste el Protocolo P.A.C.A</h3>", unsafe_allow_html=True)

            if st.button('Pincha aqui para mas información'):
                boton()
        else:   
            st.write(f"Error, te quedan {num-1} intentos")
            adivina_escribiendo(num, intentos)        
    else:
        st.write("Se acabo")





def adivina_imagen( num = 4, intentos = 0):
    num -= 1
    intentos += 1 

    st.markdown(f"<h4 style='text-align: legft; color: black;'>🎬El primer reto consiste en averiguar donde se encuentran las Flechas de Diana</h4>", unsafe_allow_html=True)

    respuesta_acertada = "Dos en la carretera"
    if num > 0:
        respuesta = st.radio(f"Intento {intentos} de 3", ("Elige una opción", "Neptuno", 'Gran Vía', 'Plaza España'))
        if respuesta == "Elige una opción":
            #st.write("necesitamos tu respuesta")  
            pass    
            return "necesitamos tu respuesta"      
        elif respuesta =="Gran Vía":
            st.markdown("<h1 style='text-align: center; color: black;'>LOGRO DESBLOQUEADO</h1>", unsafe_allow_html=True)
            st.markdown("<h3 style='text-align: center; color: black;'>Pasemos al siguiente reto</h3>", unsafe_allow_html=True)
            return "Bien!!!"
        else:   
            st.write(f"Error, te quedan {num-1} intentos")
            adivina_imagen(num, intentos)  
            return "Error"      
    else:
        st.write("Se acabó")
        return "Se acabó"


def adivina_geografía(num = 4, intentos = 0):
    num -= 1
    intentos += 1 

    st.markdown(f"<h4 style='text-align: legft; color: black;'> 🌍El segundo reto consiste en contestar a la siguiente pregunta ¿Cómo se llamaba antes la Calle Alcalá?</h4>", unsafe_allow_html=True)
    

    if num > 0:
        respuesta = st.radio(f"Intento {intentos} de 3", ("Elige una opción", "Calle Grande", 'Calle de la Puerta', 'Calle de los Olivares', 'Calle de la Fuente'))
        if respuesta == "Elige una opción":
            #st.write("necesitamos tu respuesta")  
            pass    
            return "necesitamos tu respuesta"      
        elif respuesta =="Calle de los Olivares":
            st.markdown("<h1 style='text-align: center; color: black;'>LOGRO DESBLOQUEADO</h1>", unsafe_allow_html=True)
            st.markdown("<h3 style='text-align: center; color: black;'>Pasemos al siguiente reto</h3>", unsafe_allow_html=True)
            return "Bien!!!"
        else:   
            st.write(f"Error, te quedan {num-1} intentos")
            adivina_imagen( num, intentos)  
            return "Error"      
    else:
        st.write("Se acabó")
        return "Se acabó"




def boton():
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
        st.write("Terminaremos el día con un cafe disfrutando de los cielos y tejados de Madrid en el Circulo de Bellas Artes")
        st.write("Más información en este [link](https://www.azoteadelcirculo.com/)")

#cargamos y ponemos una imagen
image = Image.open('imagenes/fondo.jpg')
st.image(image, caption='Atardecer en la Almudena')
#st.write("Es hora de jugar y desbloquar algunos retos para poder conseguir vuestro regalo de Reyes. Tendréis tres intentos para averiguarlo. Si fallaís, tendréis que volver mañana")


mensaje_juego = """A lo largo de esta página os iremos planteando algunos retos que tendréis que ir desbloqueando para poder 
                    llegar a vuestro Regalo de Reyes. En cada uno de los retos que os planteamos tendréis tres intentos.
                     Si en alguno de los retos consumís los tres intentos tendréis que volver otro día para intentarlo de nuevo."""

st.markdown(f"<h4 style='text-align: center; color: black;'>{mensaje_juego}</h4>", unsafe_allow_html=True)

with st.empty():
    for seconds in reversed(range(2)):
        st.markdown(f"<h4 style='text-align: center; color: black;'>⏳ Quedan {seconds} para empezar con los retos!!!</h4>", unsafe_allow_html=True)
        time.sleep(3)
    st.markdown("<h1 style='text-align: center; color: black;'>✔️ Empezamos!</h1>", unsafe_allow_html=True)


repuesta1 = adivina_imagen()

if repuesta1 == "Se acabó": 
    st.write("Lo siento, no podemos seguir con los retos")
elif repuesta1 == "necesitamos tu respuesta" or repuesta1 == "Error":
    st.write("❌ Necesitamos que superes este reto para pasar al siguiente")
elif repuesta1  == "Bien!!!":
    respuesta2 = adivina_geografía()
    
    if respuesta2 == "Se acabó": 
        st.write("Lo siento, no podemos seguir con los retos")
    elif respuesta2 == "necesitamos tu respuesta" or respuesta2 == "Error":
        st.write("❌ Necesitamos que superes este reto para pasar al siguiente")
    elif respuesta2  == "Bien!!!":
        adivina_escribiendo()




