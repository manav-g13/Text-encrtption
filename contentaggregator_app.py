import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

# --- Load Environment Variables ---
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# --- Configure Gemini ---
if api_key:
    try:
        genai.configure(api_key=api_key)
        gemini_model = genai.GenerativeModel("gemini-pro")
    except Exception as e:
        gemini_model = None
        gemini_error = str(e)
else:
    gemini_model = None
    gemini_error = "API key not found. Please set GEMINI_API_KEY in your .env file."

# --- Streamlit Page Config ---
st.set_page_config(page_title="Advanced Split App", layout="wide")
st.title("🔍 Stylish Split-Screen App")

# --- Search Box ---
search_query = st.text_input("Search", placeholder="Type something...")
if search_query:
    st.success(f"Searching for: {search_query}...")
    time.sleep(0.5)  # Simulate delay

st.markdown("---")

# --- Three Column Layout ---
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

    # Dummy bar chart
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

st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")

# --- Gemini Chat Panel ---
st.markdown("### 🤖 Gemini Chat")
if gemini_model:
    user_prompt = st.text_input("Ask Gemini:", "Explain how AI works in a few words")
    if st.button("Get Gemini Response"):
        with st.spinner("Getting response..."):
            try:
                response = gemini_model.generate_content(user_prompt)
                st.success("Response from Gemini:")
                st.write(response.text)
            except Exception as e:
                st.error(f"❌ Failed to get Gemini response: {e}")
else:
    st.error(f"❌ Gemini API Error: {gemini_error}")
