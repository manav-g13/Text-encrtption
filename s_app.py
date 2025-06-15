import streamlit as st
import google.generativeai as genai

# --- HARDCODE YOUR GEMINI API KEY HERE ---
GEMINI_API_KEY = "AIzaSyAPr4cCjCAPLwSC4rXso8F-pUPN_Mnqa3w"

# Validate API key
if not GEMINI_API_KEY:
    st.error("❌ GEMINI_API_KEY is missing!")
    st.stop()

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

# --- Streamlit UI ---
st.set_page_config(page_title="Gemini Chat App", layout="wide", page_icon="🤖")
st.title("🤖 Gemini-powered Q&A App")

# Chat input
user_prompt = st.text_input("Ask a question to Gemini", placeholder="e.g., How does AI work?")

if user_prompt:
    with st.spinner("Gemini is thinking..."):
        try:
            response = model.generate_content(user_prompt)
            st.success("✅ Gemini responded:")
            st.markdown(f"**Response:** {response.text}")
        except Exception as e:
            st.error(f"❌ Gemini API Error: {e}")

# Footer
st.markdown("---")
st.markdown("🚀 Built with ❤️ using Gemini + Streamlit")
