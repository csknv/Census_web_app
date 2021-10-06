# Open Sublime text editor, create a new Python file, copy the following code in it and save it as 'census_main.py'.

# Import modules
import streamlit as st
st.set_page_config(page_title = "Census Visualisation Web App",page_icon = "💥",layout = "centered", initial_sidebar_state = "auto")
import numpy as np
import pandas as pd

@st.cache()
def load_data():
	# Load the Adult Income dataset into DataFrame.

	df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
	df.head()

	# Rename the column names in the DataFrame using the list given above. 

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 
               'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	df.head()



	# Replace the invalid values ' ?' with 'np.nan'.

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required 

	# Delete the rows with the 'dropna()' function
	df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()

import streamlit as st
# Set the title to the home page contents.
st.title("Census Visualisation Web App")
# Provide a brief description for the web app.
st.write("This web app allows a user to explore and visualise the census data.")

# Create the Page Navigator for 'Home' and 'Visualise Data' web pages in 'census_main.py'
# Import 'census_home.py' and 'census_plots.py' .
import census_home
import census_plots
import streamlit as st
# Adding a navigation in the sidebar using radio buttons
# Create a dictionary.
pages_dict = {
             "Home:":census_home,
             "Visualise Data:":census_plots 
         }
# Add radio buttons in the sidebar for navigation and call the respective pages based on user selection.
st.sidebar.title('Navigation')
user_choice = st.sidebar.radio("Go to", tuple(pages_dict.keys()))
if user_choice == "Home":
    home.app() 
else:
    selected_page = pages_dict[user_choice]
    selected_page.app(census_df) 

