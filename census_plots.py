# Code for 'census_plots.py' file.
# Import necessary modules.
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# Define a function 'app()' which accepts 'census_df' as an input.
def app(census_df):
    st.sidebar.subheader("Visualisation Selector")
    # Add a multiselect in the sidebar with label 'Select the Charts/Plots:'
    # Store the current value of this widget in a variable 'plot_list'.
    plot_list = st.sidebar.multiselect("Select the Charts/Plots :",('Box Plot', 'Count Plot', 'Pie Chart'))
    # Display count plot using seaborn module and 'st.pyplot()' 
    if "Count Plot" in plot_list:
      st.subheader("Count Plot")
      plt.figure(figsize =(16,4))
      plt.title("Count of a number of records for unique workclass feature values for different income groups.")
      sns.countplot(x = "workclass",data = census_df,hue = "income")
      st.pyplot()
    # Display pie plot using matplotlib module and 'st.pyplot()'
    if "Pie Chart" in plot_list:
      st.subheader("Pie Chart")
      col = st.multiselect("Select the Features:",(census_df.columns))
      for i in col:
        plt.figure(figsize =(16,4))
        plt.title(f"Pie Chart to display the distribution of records for the {i} feature.")
        pie_data = census_df[i].value_counts()
        plt.pie(pie_data,labels = pie_data.index,autopct = "%1.2f%%",startangle = 30)
        st.pyplot()
    # Display box plot using matplotlib module and 'st.pyplot()'
    if "Box Plot" in plot_list:
      st.subheader("Box Plot")
      col1 = st.multiselect("Select the Features:",(census_df.drop(labels = "hours-per-week",axis = 1).columns))
      for i in col1:
        plt.figure(figsize =(16,4))
        plt.title(f"Boxplot for Hours Per Week for different {i} groups.")
        sns.boxplot(census_df["hours-per-week"],census_df[i])
        st.pyplot()