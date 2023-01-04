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
        respuesta = st.text_input(f"¿Qué es P.A.C.A? intento {intentos}")
        if respuesta == "":
            st.write("necesitamos tu respuesta")            
        elif respuesta in respuesta_acertada:
            st.markdown("<h1 style='text-align: center; color: black;'>LOGRO DESBLOQUEADO</h1>", unsafe_allow_html=True)
            if st.button('Pincha aqui para mas informacion'):
                st.write('Why hello there')
                col1, col2, col3,col4 = st.columns(4)

                with col1:
                    st.markdown("<h1 style='text-align: center; color: black;'>P</h1>", unsafe_allow_html=True)
                    st.image("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALoAAAC6CAMAAAAu0KfDAAAABlBMVEX///8AAABVwtN+AAABxklEQVR4nO3QUZKDQAwD0eT+l94DgJQeCAXOtr4oGKzneb2MMebivHHSX31mbzljkC5d+hT6tj6dIcuQ+vRMDNKlS59I5zX9ZKKQ98QgXbr0X6X3f9P5NEG6dOnSSTGnk6/SpUv/PXrHEXpHHLsa6dKlT6cfq/nuMzdIly59Cv18SMGF9Wci/Y5IvyM301N9quxEshJZAy0sXbr0x9NJWRqXWH2NnnQR0qVLn0XvUL79KqVfFmmULl36FHpC9xBoByFi+ipduvQh9D4ivUllqwvwq5EuXfpEOjoK6NsJxy6iLyxduvRZ9M4lX8mSx7rieenSpQ+hry6z/TdVrl5E/1e6dOmz6H2B/kyI6TmtmhaLy0iXLv3B9FXWauXq5NSyE+nSpT+enupTyEoESto/oKVLl/54emKREemvPqf/tWCQLl36EHpfKYWc54vxLunSpU+hr2Zbn3Dkfb+yPkG6dOnPp79xTtWErmPXIV269Fn0nQ/hTHomK5FeflK6dOmz6O9N+Lgz6/XsoKVLl/6j9PS1V/LFert06dL/A31nUM13J0iXLn0inRfz9JnbM/3ipEuXPpF+DEGInN5bpEuXPpFujDEX5A/WVTvF1c+o+gAAAABJRU5ErkJggg==")

                with col2:
                    st.header("A")
                    st.image("https://static.streamlit.io/examples/dog.jpg")

                with col3:
                    st.header("C")
                    st.image("https://static.streamlit.io/examples/owl.jpg")
                with col4:
                    st.header("A")
                    st.image("https://static.streamlit.io/examples/owl.jpg")

        else:   
            st.write(f"Error, te quedan {num-1} intentos")
            cuenta_atras(num, intentos)        
    else:
        st.write("Se acabo")

#cargamos y ponemos una imagen
image = Image.open('imagenes/fondo.jpg')
st.image(image, caption='Sunrise by the mountains')
st.write("Tendréis tres intentos para averiguarlo. Si fallaís, tendréis que volver mañana")

cuenta_atras()



