import streamlit as st

# Streamlit Google Sheets connection
from streamlit_gsheets import GSheetsConnection

# Create a connection object
conn = st.connection("gsheets", type=GSheetsConnection)

# Get the dataframe via read method
df = conn.read()

# Display the dataframe
st.dataframe(df)

# Customize the reading
df = conn.read(
    worksheet="Sheet1",
    ttl="10m",
    usecols=[0, 1],
    nrows=3,
)

# Display the new dataframe
st.dataframe(df)