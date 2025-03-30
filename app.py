import streamlit as st
import google.generativeai as genai  # Google AI API

# 🔑 Set Your Google AI API Key (Replace with Your Key)
GOOGLE_API_KEY = "AIzaSyBChtpfxdTTuHGV_UY1-i6EpBhC03-1K1M"
genai.configure(api_key=GOOGLE_API_KEY)

st.set_page_config(page_title="The AI-strologer", page_icon="🔮")

# 🏆 Title & Introduction
st.markdown("""
    <h1 style='text-align: center; color: #007bff;'>🔮 The AI-strologer 🔮</h1>
    <h4 style='text-align: center;'>Let AI predict your future in the funniest way possible!</h4>
""", unsafe_allow_html=True)

# 📌 Function to Call Google AI API (Gemini)
def get_ai_future(name):
    prompt = f"Imagine a funny and bizarre future yet motivational prediction for a person named {name}. Make it witty and creative!"
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

# User input
name = st.text_input("Enter your name:")

if st.button("🔮 Tell Me My Future!"):
    if name:
        prediction = get_ai_future(name)
        st.success(prediction)
    else:
        st.warning("Please enter your name to get a prediction!")

# 📌 Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>🚀 Created by AIPT CLUB</p>", unsafe_allow_html=True)
