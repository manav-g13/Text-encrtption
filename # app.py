# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
import os
import google.generativeai as genai
from dotenv import load_dotenv

# --- Page Config ---
st.set_page_config(page_title="Advanced Split App", layout="wide")

# --- Title and Search ---
st.title("🔍 Stylish Split-Screen App")
search_query = st.text_input("Search", placeholder="Type something...")

# --- Dynamic Feedback ---
if search_query:
    st.success(f"Searching for: {search_query}...")
    time.sleep(0.5)  # Simulate delay

st.markdown("---")

# --- Three Columns Layout ---
col1, col2, col3 = st.columns(3)

# --- Column 1: Info Panel ---
with col1:
    st.subheader("📄 Info Panel")
    st.write("This section displays textual content.")
    st.info("This panel could show details related to your search.")
    with st.expander("More Info"):
        st.write("Expandable section with more information.")
    st.image("https://via.placeholder.com/200x150", caption="Sample Image")

# --- Column 2: Analytics Panel ---
with col2:
    st.subheader("📊 Analytics Panel")
    st.metric(label="Total Results", value="234", delta="+12%")
    st.metric(label="Query Speed", value="0.85s")

    # Dummy chart
    data = pd.DataFrame({
        "Category": ["A", "B", "C"],
        "Value": [10, 23, 45]
    })
    fig, ax = plt.subplots()
    ax.bar(data["Category"], data["Value"], color="skyblue")
    st.pyplot(fig)

# --- Column 3: Interactive Panel ---
with col3:
    st.subheader("⚙️ Interactive Panel")
    option = st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
    st.write(f"You selected: {option}")

    number = st.slider("Select a range value", 0, 100, 25)
    st.write(f"Slider value: {number}")

    if st.button("Run Action"):
        st.success("✅ Action executed successfully!")

# --- Footer ---
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")

# --- Gemini Integration ---
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ API key not found. Please set GEMINI_API_KEY in your .env file.")
else:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-pro")

        st.markdown("### 🤖 Gemini Chat")
        user_prompt = st.text_input("Ask Gemini:", "Explain how AI works in a few words")
        if st.button("Get Gemini Response"):
            with st.spinner("Getting response..."):
                response = model.generate_content(user_prompt)
                st.success("Response from Gemini:")
                st.write(response.text)

    except Exception as e:
        st.error(f"❌ Error communicating with Gemini API: {e}")