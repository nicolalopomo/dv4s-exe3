import streamlit as st
import pandas as pd
import os

# Streamlit Google Sheets connection
from streamlit_gsheets import GSheetsConnection

# Create a connection object
conn = st.connection("gsheets", type=GSheetsConnection)

# Customize the reading
df = conn.read(spreadsheet=st.secrets.connections.gsheets.spreadsheet)

# Display the new dataframe
st.dataframe(df)

# Define file cwd path
myCWD = os.getcwd()
# Define the path where to save the file
csv_file_path = os.path.join(myCWD, "my_data.csv")

# Write CSV
df.to_csv(csv_file_path, index=False) # Not writing row names

st.success(f"Data saved to {csv_file_path}")


# Display an image
st.image("https://static.streamlit.io/examples/cat.jpg",
         caption="This is a cat!",
         width=100)

# Display a video
# Rember to upload the video in the project folder
video = open("my_video.mp4", "rb")
video_bytes = video.read()
st.video(video_bytes)


st.logo(
    "https://images.seeklogo.com/logo-png/44/1/streamlit-logo-png_seeklogo-441815.png",
    link="https://streamlit.io/gallery",
    icon_image="https://images.seeklogo.com/logo-png/44/1/streamlit-logo-png_seeklogo-441815.png",
)