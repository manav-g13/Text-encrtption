import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

# --- Page Config ---
st.set_page_config(page_title="Advanced Split App", layout="wide")

# --- Title and Search ---
st.title("🔍 Stylish Split-Screen App")

search_query = st.text_input("Search", placeholder="Type something...")

# --- Dynamic Feedback ---
if search_query:
    st.success(f"Searching for: {search_query}...")
    time.sleep(0.5)  # Simulate loading delay

st.markdown("---")

# --- Three Columns Layout ---
col1, col2, col3 = st.columns(3)

# --- Column 1: Text and Image ---
with col1:
    st.subheader("📄 Info Panel")
    st.write("This section displays textual content.")

    st.info("This panel could show details related to your search.")

    with st.expander("More Info"):
        st.write("Expandable section with more information.")

    st.image("https://via.placeholder.com/200x150", caption="Sample Image")

# --- Column 2: Metrics and Chart ---
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

# --- Column 3: Interactive Elements ---
with col3:
    st.subheader("⚙️ Interactive Panel")

    option = st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
    st.write(f"You selected: {option}")

    number = st.slider("Select a range value", 0, 100, 25)
    st.write(f"Slider value: {number}")

    if st.button("Run Action"):
        st.success("✅ Action executed successfully!")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
