import streamlit as st
import pandas as pd
import numpy as np
 
#disply image
from PIL import Image
image = Image.open('img.JFIF')
st.image(image, caption='Sunrise by the mountains')

#display video
import streamlit as st
st.video('https://youtu.be/FVsvrFAWDTM') 

#displying audio files 
audio_file = open('myaudio.ogg', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/ogg')