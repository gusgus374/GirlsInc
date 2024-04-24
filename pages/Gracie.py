import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import pathlib
import streamlit as st
import altair as alt

st.title("Hello Grace, It's Me")

st.write("Well,I'm me and your you. Where does that lead us?")


st.button ("Hello :)")
st.button("Reset",type='primary')
if st.button (":wink:"):
    st.write ("Hi!")
    st.image(image="./resources/gracie_kick.JPG",width=800)
    st.write("… Na-na, na-na, na-na-na-na-na Sì, ce l'ha Trucco allo specchio nella sua camera da letto Calze a rete alte fino alla coscia e stivali neri Naso trafitto dal profumo della sigaretta Mezza morta ma sembra ancora così carina (sì) Lei è un mostro sotto mentite spoglie E conosce tutte le parole delle canzoni trap Scatta foto con un rossetto rosso ciliegia Dice che esce solo con ragazzi con un grosso")