import streamlit as st
import streamlit.secrets as secrets
import pandas as pd

# Get the URL for the Google Sheet from the secrets file
gsheets_url = secrets.get_secret("private_gsheets_url")

# Read the Google Sheet into a pandas DataFrame
df = pd.read_csv(gsheets_url)

# Display the DataFrame
st.dataframe(df)
