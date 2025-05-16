# -*- coding: utf-8 -*-
"""app.py"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import gspread
from gspread_dataframe import get_as_dataframe
from google.oauth2.service_account import Credentials
import json

# Configuración de la página
st.set_page_config(page_title="BrightSpace Instructores", layout="wide")

st.title("📊 Análisis de Actividades en BrightSpace")
st.write("Esta aplicación permite analizar las actividades de los instructores en la plataforma BrightSpace.")

# Autenticación con Google desde secrets.toml
creds_info = json.loads(st.secrets["GCP_SERVICE_ACCOUNT"])
creds = Credentials.from_service_account_info(creds_info)
gc = gspread.authorize(creds)

# Lectura de Google Sheet
SHEET_ID = "1Eh3X8Bwd-0GoF3pyl0Xz6-oCOJm-SW9l5fItahcn99g"
worksheet = gc.open_by_key(SHEET_ID).sheet1
df = get_as_dataframe(worksheet, evaluate_formulas=True).dropna(how="all")

# Limpieza y conversión
cols_metrica = [
    "Cantidad de elementos de calificación",
    "Cantidad de publicaciones de debate",
    "Cantidad de publicaciones de debate iniciado
