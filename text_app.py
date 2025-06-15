# streamlit_gemini_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

# --- Load API Key ---
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ API key not found. Please set GEMINI_API_KEY in .env file.")
    st.stop()

# --- Configure Gemini ---
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

# --- Streamlit Page Config ---
st.set_page_config(page_title="Advanced Gemini App", layout="wide")
st.title("🤖 Gemini-Powered Split-Screen App")

# --- Search and Prompt ---
search_query = st.text_input("🔍 Search or Ask Gemini", placeholder="Ask any question...")

if search_query:
    st.success(f"Querying Gemini for: '{search_query}'")
    time.sleep(0.5)
    try:
        response = model.generate_content(search_query)
        gemini_response = response.text
    except Exception as e:
        gemini_response = f"❌ Error: {e}"
else:
    gemini_response = "Awaiting input..."

st.markdown("---")

# --- Three Column Layout ---
col1, col2, col3 = st.columns(3)

# --- Column 1: Info Panel ---
with col1:
    st.subheader("📄 Info Panel")
    st.write("This section can display static or contextual text.")
    st.info("Your prompt will appear here.")

    with st.expander("Prompt Preview"):
        st.write(search_query or "No query entered yet.")

    st.image("https://via.placeholder.com/200x150", caption="Sample Image")

# --- Column 2: Analytics Panel ---
with col2:
    st.subheader("📊 Analytics Panel")
    st.metric(label="Total Queries", value="234", delta="+12%")
    st.metric(label="Response Time", value="0.85s")

    chart_data = pd.DataFrame({
        "Category": ["A", "B", "C"],
        "Value": [10, 23, 45]
    })

    fig, ax = plt.subplots()
    ax.bar(chart_data["Category"], chart_data["Value"], color="lightgreen")
    st.pyplot(fig)

# --- Column 3: Interactive Panel ---
with col3:
    st.subheader("⚙️ Gemini Output Panel")

    st.write("Gemini Response:")
    st.code(gemini_response, language="markdown")

    # More interactive elements
    option = st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
    number = st.slider("Pick a value", 0, 100, 30)

    if st.button("Run Extra Action"):
        st.success("✅ Action executed successfully!")

# Footer
st.markdown("---")
st.markdown("Crafted with ❤️ using Streamlit and Gemini AI")
