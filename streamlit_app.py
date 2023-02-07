import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

st.header ('st.write')

st.write ("hello, *world!* :sunglasses:")

st.write (1234)



#Panda Data Frames
df = pd.DataFrame({
    'First Colum': [1,2,3,4],
    'Second Column': [10,20,30,40]
})
st.write(df)

st.write("Below is DataFrame:", df, "above is a DataFrame.")

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=["a", "b", "c"])

st.write(df2)

c=alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'] 
)
st.write(c)








#####################DAY 1################
# st.write("Hello World")
#st.header("st.button")
#if st.button("Say Hello"):
#    st.write("Why Hello There")

#else:
#    st.write("Goodbye")

#Build Dashboard
#add_sidebar = st.sidebar.selectbox("DA Name", ("Gabriella Burnham","Justin Claypool"))

#if add_sidebar == "Gabriella Burnham":
#    st.write("You selected Gabby")
#
#if add_sidebar =="Justin Claypool":
#    time_select = st.selectbox("Pick a Date:", ("Chart 1", "Chart 2"))

