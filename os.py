import streamlit as st
import subprocess

st.title("Linux Command Line in Streamlit")

# Input field for command
command = st.text_input("Enter a Linux command:", "ls")

if st.button("Run Command"):
    try:
        # Run the command and capture output
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        st.text_area("Output:", result.stdout + result.stderr, height=200)
    except Exception as e:
        st.error(f"Error: {e}")
