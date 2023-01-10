<<<<<<< HEAD
import streamlit as st
import pandas as pd
 
st.header("Map")
 
data = {"lat":[28.704060, 28.459497, 13.082680, 17.385044, 23.0225],
        "lon":[77.102493, 77.026634, 80.270721, 78.486671, 72.5714],
        "City": ["Delhi", "Gurgaon", "Chennai", "Hyderabad", "Ahemdabad"]}
 
df = pd.DataFrame(data)
df
=======
import streamlit as st
import pandas as pd
 
st.header("Map")
 
data = {"lat":[28.704060, 28.459497, 13.082680, 17.385044, 23.0225],
        "lon":[77.102493, 77.026634, 80.270721, 78.486671, 72.5714],
        "City": ["Delhi", "Gurgaon", "Chennai", "Hyderabad", "Ahemdabad"]}
 
df = pd.DataFrame(data)
df
>>>>>>> e8346912a3977fa93c7a3f304041ca6f1b389e0f
st.map(data=df)