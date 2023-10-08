import streamlit as st
from streamlit_option_menu import option_menu
import time
import subprocess

st.header("Nanoscript")
fileObject = st.file_uploader(label = "Загрузите ваш FASTQ файл" )

