import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rnd
import os
import pathlib
import streamlit as st
import altair as alt
import time

st.title("This is a title!")

st.header("Week 4 - Simulation of Soccer!")

with st.echo():
    #Length of match
    match_minutes = 90
    #Average goals per match
    goals_per_match = 2.79
    #Probability of a goal per minute
    prob_per_minute = np.array(goals_per_match/match_minutes)
    st.write('The probability of a goal per minute is %5.5f. \n' % prob_per_minute )

with st.echo():
    #Count of the number of goals
    goals=0

    for minute in range(match_minutes):

        #Generate a random number between 0 and 1.
        r=rnd.rand(1,1)

        #Prints an X when there is a goal and a zero otherwise.
        if (r < prob_per_minute):
            #Goal - if the random number is less than the goal probability.
            st.write('X')
            goals=goals+1
            time.sleep(0)  #Longer pause
        else:
            st.write('o')
            time.sleep(0.1)  #Short pause

st.write('Final whistle. \n \nThere were ' + str(goals) + ' goals.')
st.button("Re-run simulation")
st.header("What if we did this for 380 games?")
#  We now simulate 380 matches of a football season and look at how well it predicts the
#  distribution of the number of goals. This is done in the code below: we loop over 380 matches,
#  store the number of goals for each match in array and then we make a histogram of the number of goals.
#


def simulateMatch(n, p):
  # n - number of time units
  # p - probability per time unit of a goal
  # display_match == True then display simulation output for match.

  # Count the number of goals
  goals = 0

  for minute in range(n):
      # Generate a random number between 0 and 1.
      r = rnd.rand(1, 1)
      # Prints an X when there is a goal and a zero otherwise.
      if (r < p):
        # Goal - if the random number is less than the goal probability.
        goals = goals + 1

  return goals

# Number of matches
num_matches = 380

# Loop over all the matches and print the number of goals.
goals = np.zeros(num_matches)
for i in range(num_matches):
  goals[i] = simulateMatch(match_minutes, prob_per_minute)
  #print('In match ' + str(i+1) + ' there were ' + str(int(goals[i])) + ' goals.')

# Create a histogram

fig, ax = plt.subplots(num=1)

histogram_range = np.arange(-0.5, 10.51, 1)
histogram_goals = np.histogram(goals, histogram_range)

ax.bar(histogram_goals[1][:-1] + 0.5, histogram_goals[0], color='white', edgecolor='black', linestyle='-', alpha=0.5)
ax.set_ylim(0, 100)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xticks(np.arange(0, 11, step=1))
ax.set_yticks(np.arange(0, 101, step=20))
ax.set_xlabel('Number of goals')
ax.set_ylabel('Number of matches')
with st.expander("The same simulation as above, repeated 380 times"):
    st.write(fig)