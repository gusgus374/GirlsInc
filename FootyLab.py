import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import pathlib
import streamlit as st
import altair as alt
#import folium
#from folium.plugins import HeatMap
#import seaborn as sns

st.set_page_config(
    page_title="FootyLab",
    page_icon="./resources/boots1.png",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Hello, Girls!")

st.image(image="./resources/profile_coachGus.JPG",width=600)

st.header("Welcome to the Girls, Inc. FootyLab!")

st.text("This is the home page of our currently-under-development app!")
st.text("The goal is for us to explore the data we have been collecting on the soccer field right here in the FootyLab.")
st.subheader("BUT HOW ARE WE GONNA DO THIS?!")
st.markdown("Magic. Well... actually by writing some *python code*... which feels like magic, I promise.")

st.markdown("In fact, everything you are currently seeing on the screen was written using python code!!!. Have a look for youself:")

st.code("""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import pathlib
import streamlit as st
import altair as alt
        
st.title("Hello, Girls!")

st.image(image="./resources/profile_coachGus.JPG",width=600)

st.header("Welcome to the Girls, Inc. FootyLab!")

st.text("This is the home page of our currently-under-development app!")
st.text("The goal is for us to explore the data we have been collecting on the soccer field right here in the FootyLab.")
st.subheader("BUT HOW ARE WE GONNA DO THIS?!")
st.markdown("Magic. Well... actually by writing some *python code*... which feels like magic, I promise.")

st.markdown("In fact, everything you are currently seeing on the screen was written using python code!!!. Have a look for youself:")
        """)

st.subheader("See? Magic.")
coach_message = st.chat_message(name="Coach Gus",avatar="./resources/profile_coachGus.JPG")
coach_message.write("Now I'm going to ``cast a spell`` (:wink:) to generate a button:")

st.code("""
        #this spell is actually just python code
st.button("I'm a Button")
        """)
st.button("I'm a Button")

coach_message = st.chat_message(name="Coach Gus",avatar="./resources/profile_coachGus.JPG")
coach_message.write("Okay cool! We can click on our newly casted button but... that's about it. Let's try a more advanced spell:")

st.code("""
uploaded_file = st.file_uploader("Choose a file")
        """)

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
        gps_data = pd.read_csv(uploaded_file)
        with st.expander(label="Collapse/Expand",expanded=True):
            st.write(gps_data)
        coach_message = st.chat_message(name="Coach Gus",avatar="./resources/profile_coachGus.JPG")
        coach_message.write("Let's clean this data up...the code below selects only the rows from the table where the column **Split Name** has the value 'game'")
        coach_message.write('Then we make the table index be Player Name instead of the random column of numbers we see above')
if uploaded_file is not None:    
    with st.echo():
        gps_data = gps_data.loc[gps_data['Split Name'] == 'game']
        gps_data = gps_data.set_index('Player Name', drop=False)
        #let's see where we are at now
        st.dataframe(gps_data,use_container_width=True)
    coach_message = st.chat_message(name="Coach Gus",avatar="./resources/profile_coachGus.JPG")
    coach_message.write("We're getting there! But I think we can do better a little better:")
if uploaded_file is not None:
    with st.echo():
        gps_data = gps_data.drop(['Date','Session Title','Split Name','Tags','Hr Load','Time In Red Zone (min)','Hr Max (bpm)'],axis=1)
        st.dataframe(gps_data)
    coach_message = st.chat_message(name="Coach Gus",avatar="./resources/profile_coachGus.JPG")
    coach_message.write("And when you're *really* weaving your magic wand you can cast some pretty useful spells. Check it out below!")
    coach_message.write("I'm interested in the relationship between distance covered and sprint distance. Here's the code I used to create the graphs you see:")

if uploaded_file is not None:
    with st.echo():
        gps_data['sprint/total distance']=(gps_data['Sprint Distance (yards)']/1000)/gps_data['Distance (miles)']
        chart = alt.Chart(gps_data).mark_circle().encode(
            x='Distance (miles)',
            y='Sprint Distance (yards)',
            size='sprint/total distance',
            color='Player Name').interactive()
        '''
        ## Sprint Distance vs Total Distance
        '''
        st.altair_chart(chart, theme="streamlit", use_container_width=True)
    coach_message = st.chat_message(name="Coach Gus",avatar="./resources/profile_coachGus.JPG")
    coach_message.write("Lastly, let's look at max acceleration, max deceleration, and top speed for this game:")
if uploaded_file is not None:
    chart = alt.Chart(gps_data).mark_circle().encode(
        x='Top Speed (mph)',
        y='Max Acceleration (m/s/s)',
        size='Max Deceleration (m/s/s)',
        color='Player Name').interactive()
    '''
    ## Max Acceleration vs Deceleration
    '''
    st.altair_chart(chart, theme="streamlit", use_container_width=True)