# Show complete dataset and summary in 'census_home.py'
# Import necessary modules.
import numpy as np
import pandas as pd
import streamlit as st
# Define a function 'app()' which accepts 'census_df' as an input.
def app(census_df):
  st.subheader("View Data")
  st.set_option('deprecation.showPyplotGlobalUse', False)
  # Display dataset within beta_expander.
  with st.beta_expander("View Full Dataset"):
    st.dataframe(census_df)
    # Create three beta_columns.
  st.subheader("Columns Description:")
  # Add a checkbox in the first column. Display the column names of 'census_df' on the click of checkbox.
  if st.checkbox("Show All Column Names"):
    st.write(census_df.columns)
    # Add a checkbox in the second column. Display the column data-types of 'census_df' on the click of checkbox.
  if st.checkbox("View Column data-type"):
    st.write(dict(census_df.dtypes))
    # Add a checkbox in the third column followed by a selectbox which accepts the column name whose data needs to be displayed.
  if st.checkbox("View Column Data"):
    col = st.selectbox("Choose the Column, For which want the data to be displayed:",(census_df.columns))
    st.write(census_df[col])
  # Show dataset summary on click of a checkbox.
  if st.checkbox("Show summary"):
    st.table(census_df.describe())