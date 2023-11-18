import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(page_title=" Corridas de Uber em NYC",
                   page_icon='https://blog.uber-cdn.com/cdn-cgi/image/width=2160,quality=80,onerror=redirect,format=auto/wp-content/uploads/sites/272/2011/05/uber-heart-ny.png',
                   layout='wide')

base="dark"
primaryColor="#ef2727"
secondaryBackgroundColor="#013112"
textColor="#f9f5f5"

st.title('Corridas de UBER em NYC :oncoming_automobile:')

col1, col2, col3 = st.columns(3)
with col1:
   st.header("")
   st.image("https://static01.nyt.com/images/2019/04/28/business/28uberamazon1/merlin_153552903_90b21934-ccb2-4d1e-9d08-e0c22cd9550c-articleLarge.jpg?quality=75&auto=webp&disable=upscale")


st.write('Olá pessoal, sejam bem vindos! Esse é o meu primeiro app usando a ferramenta Streamlit, e estou muito feliz! Por favor, aproveitem as ferramentas que deixei disponivel a todos.')
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


@st.cache_data

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Carregando os dados...')
data = load_data(10000)
data_load_state.text("Pronto! (using st.cache_data)")
if st.checkbox('Mostrar dados sem filtro'):
    st.subheader('Dados sem filtro')
    st.write(data)

Data_Video = ('https://www.youtube.com/watch?v=-A1AO0kP3wI')
st.video(Data_Video)

st.subheader('Numero de entrada de passageiros por hora :red_car:')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Mapa do Inicio das Corridas :red_car: {hour_to_filter}:00')
st.map(filtered_data)
hour_to_filter = st.slider('hour', 0, 23, 17)

st.download_button('Download dos Dados', DATA_URL)

st.write('Hey Drivers, escolha sua rádio favorita')
st.button('[Metropolitana](zeno.fm/radio/radiometropolitanaporto/)')
st.button('[ON FM](onfm.pt/on-fm-tv/)')
st.button('[RFM](https://rfm.sapo.pt/emissaopub)')
st.button('[Antena 1](https://antena1.rtp.pt/)')

st.camera_input("Sorria e tire uma foto!")
st.color_picker('Escolha a cor que mais te deixa confortavel!')

with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))

st.chat_input("Say something")

with st.form(key='my_form'):
   username = st.text_input('Username')
   password = st.text_input('Password')
   st.form_submit_button('Login')

st.write('[Se você deseja aprender a criar o seu app, por favor, clique aqui para iniciar](https://docs.streamlit.io/library/get-started)')