import streamlit as st
from component import component1_events
from component_nativo import Container
import pandas as pd
import numpy as np
import plotly.express as px
from padding import set_padding
from streamlit_extras.grid import grid
st.markdown("""
  <style>
  </style>
""", unsafe_allow_html=True)


df = px.data.iris()
random_df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="sepal_length",
    color_continuous_scale="reds",
)

st.title("Esse é um exemplo")

st.markdown("""
  <div style="color: white; background-color: blueviolet; padding-bottom: 15px;">
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
  </div>
""", unsafe_allow_html=True)

valor = component1_events("Juarez", "teste1")

set_padding(20)
if(valor is not None):
    st.header("Total de Counts: " + str(valor['count']))
 
     




my_grid = grid(1, [1,1,2], vertical_align="center")

with my_grid.container():
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    st.divider()    
my_grid.dataframe(random_df, use_container_width=True)
with my_grid.container():
    st.write("Total de 1000")
    st.line_chart(random_df, use_container_width=True)

with my_grid.container():
    st.write("Total de 1000")
    st.line_chart(random_df, use_container_width=True)



    


    

    
