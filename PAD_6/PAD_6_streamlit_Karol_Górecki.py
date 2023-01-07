import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import datetime
import time

st.title("Praca Domowa 06 – Streamlit")

st.header('Karol Górecki')

tab1, tab2 = st.tabs(["Ankieta", "Staty"])

tab1.subheader("Kwestionariusz")
tab2.subheader("Statystyki")

result_first_name = ''
result_first_name = ''

first_name = tab1.text_input("Wpisz swoje imię:")
if tab1.button("Zapisz imię"):
    result = first_name.title()
    tab1.success("Poprawne imię")

second_name = tab1.text_input("Wpisz swoje nazwisko:")
if tab1.button("Zapisz nazwisko"):
    result = second_name.title()
    tab1.success("Poprawne nazwisko")


data = tab2.file_uploader("Prześlij swój zbiór danych", type=['csv'])

my_bar = tab2.progress(0)

counter = 0

if data is not None:
    df = pd.read_csv(data)

    for counter in range(100):
        time.sleep(0.01)
        my_bar.progress(counter + 1)

    my_bar.empty()

    tab2.markdown("### Pierwsze 10 wierszy")
    tab2.dataframe(df.head(10))
    st.set_option('deprecation.showPyplotGlobalUse', False)
    all_columns_names = df.columns.to_list()
    selected_column_names = tab2.multiselect("Wybierz kolumny do wyświetlenia", all_columns_names)
    plot_data = df[selected_column_names]
    status = tab2.radio("Wybierz wykres, który ma zwizuwalizować dane ", ("Bar Chart", "Line Chart"))
    if status == "Bar Chart":
        tab2.bar_chart(plot_data)
    else:
        tab2.line_chart(plot_data)
    tab2.pyplot()






