import numpy as np
import pandas as pd
import altair as alt
import streamlit as st

#Print title of the Web app
st.title('World Bank Data - India')
India=pd.read_csv('World_Bank_India.csv',skiprows=4)
st.write(India)
st.write(India.index)
