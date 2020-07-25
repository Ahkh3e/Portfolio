import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
from numpy import empty
@st.cache
def fetch_data():
    df = pd.read_json('https://covidtracking.com/api/v1/us/daily.json')
    df['date'] = pd.to_datetime(df['date'], format="%Y%m%d")
    df.set_index('date', inplace=True)
    df.sort_index(ascending=True, inplace=True)
    return df
def data(charts):
    return pd.DataFrame(df, charts)
options = ['positive',
    'positiveIncrease',
    'death',
    'deathIncrease',
    'hospitalizedCurrently',
'hospitalizedIncrease',
    'hospitalizedCumulative',
    'inIcuCurrently',
    'inIcuCumulative',
'onVentilatorCurrently',
    'onVentilatorCumulative',
'recovered',
'totalTestResultsIncrease',
    'totalTestResults']
df = fetch_data()
    ## Build page
st.title('COVID-19 Dashboard')
st.header('US data')
st.subheader('Source: https://covidtracking.com')
start_date = st.sidebar.date_input("Start Date", value=datetime(2020,3,1))
end_date = st.sidebar.date_input("End Date", value=df.index.max())
charts = st.sidebar.multiselect("Select individual charts to display:",
                options=list(options))
st.area_chart(df[charts])
st.pyplot()
