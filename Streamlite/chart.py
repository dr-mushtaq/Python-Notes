import streamlit as st
#1. Line Chart in Streamlit
st.title("1. Line Chart in Streamlit")
import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

#2. Area Chart
st.title("2. Area Chart in Streamlit")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.area_chart(chart_data)
# 📊 3. Bar Chart
st.title("3. Bar Chart in Streamlit")   
chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)

#4. Map Chart
st.title("4. Map Chart in Streamlit")
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)

#6. Altair Chart
st.title("6. Altair Chart in Streamlit")
import altair as alt

df = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)
#6. Altair Chart
import altair as alt

df = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)

#7. Plotly Chart
st.title("7. Ploty Chart in Streamlit")
import plotly.figure_factory as ff

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2
hist_data = [x1, x2, x3]
group_labels = ['Group 1', 'Group 2', 'Group 3']

fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])

st.plotly_chart(fig, use_container_width=True)

#8. Graphviz Chart
st.title("8. Graphviz  Chart in Streamlit")

import graphviz as graphviz

graph = graphviz.Digraph()
graph.edge('run', 'intr')
graph.edge('intr', 'runbl')
graph.edge('runbl', 'run')
graph.edge('run', 'kernel')
graph.edge('kernel', 'zombie')
graph.edge('kernel', 'sleep')
graph.edge('kernel', 'runmem')
graph.edge('sleep', 'swap')
graph.edge('swap', 'runswap')
graph.edge('runswap', 'new')
graph.edge('runswap', 'runmem')
graph.edge('new', 'runmem')
graph.edge('sleep', 'runmem')

st.graphviz_chart(graph)
