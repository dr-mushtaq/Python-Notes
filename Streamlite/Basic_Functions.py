# iris_app.py
import streamlit as st
from sklearn.datasets import load_iris
import pandas as pd

# Load Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Title and intro
st.title("🌼 Iris Dataset Explorer")
st.write("Use the controls below to explore the classic Iris flower dataset.")

# Slider to select number of rows
num_rows = st.slider("How many rows to show?", min_value=5, max_value=150, value=10)

# Show table
st.write("Here are the first few rows of the dataset:")
st.dataframe(df.head(num_rows))

# Selectbox to choose a feature to plot
feature = st.selectbox("Pick a feature to plot", iris.feature_names)

# Plotting line chart
st.line_chart(df[feature])
