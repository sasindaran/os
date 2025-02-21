import streamlit as st
import platform

# Get the operating system
os_info = platform.system() + " " + platform.release()

# Display it in Streamlit
st.title("Operating System Information")
st.write(f"Your operating system: **{os_info}**")
