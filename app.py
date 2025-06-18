import streamlit as st
import pandas as pd
import numpy as np
import re
from io import BytesIO
import xlsxwriter
import matplotlib.pyplot as plt
from docx import Document
from docx.shared import Inches
from tempfile import NamedTemporaryFile

st.set_page_config(page_title="Autoevaluación & Plan de Carrera", layout="wide")

FILE_BASE = "Valoracion_Jobs.xlsx"
...
