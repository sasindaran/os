import streamlit as st
import os
import platform
import subprocess

# Get OS information
os_info = platform.system() + " " + platform.release()

# Function to install Wine
def install_wine():
    try:
        st.write("Installing Wine...")
        
        # Check for the package manager and install Wine
        if os.path.exists("/usr/bin/apt"):
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "-y", "wine"], check=True)
        elif os.path.exists("/usr/bin/dnf"):
            subprocess.run(["sudo", "dnf", "install", "-y", "wine"], check=True)
        elif os.path.exists("/usr/bin/pacman"):
            subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "wine"], check=True)
        else:
            st.error("Unsupported package manager. Please install Wine manually.")

        st.success("Wine installed successfully!")
    except Exception as e:
        st.error(f"Installation failed: {e}")

# Streamlit UI
st.title("Operating System & Wine Installer")
st.write(f"Your operating system: **{os_info}**")

# Install Wine button
if st.button("Install Wine Automatically"):
    install_wine()
