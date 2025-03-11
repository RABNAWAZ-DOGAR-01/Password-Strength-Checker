import streamlit as st
import re

# Set up page
st.set_page_config(page_title="🔐 Password Strength Analyzer", page_icon="🔒")

# Header
st.title("🔒 Password Strength Analyzer")
st.markdown("""
### 🔍 Is your password strong enough?  
Protect your accounts with a **secure password**. Use this tool to check its strength and get tips to make it **unbreakable!** 🔥  
""")

# Input Field
password = st.text_input("🔑 Enter your password:", type="password")

# Password Strength Logic
score = 0
feedback = []

if password:
    # Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be at least **8 characters** long.")

    # Upper & Lower Case Check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("🔠 Include both **uppercase & lowercase letters**.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔢 Add at least **one number** (0-9).")

    # Special Character Check
    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        feedback.append("🔣 Use at least **one special character** (@, $, !, %, etc.).")

    # Password Strength Feedback
    strength_levels = ["🛑 **Weak**", "🟠 **Fair**", "🟡 **Good**", "🟢 **Strong**", "💪 **Very Strong!**"]
    strength_colors = ["#FF4B4B", "#FFAA33", "#FFD700", "#32CD32", "#008000"]

    strength_index = min(score, 4)
    st.markdown(f"<h2 style='color:{strength_colors[strength_index]};'>{strength_levels[strength_index]}</h2>", unsafe_allow_html=True)

    # Strength Bar
    st.progress((score + 1) / 5)

    # Display Feedback
    if feedback:
        st.markdown("### 🔧 Improvement Tips:")
        for tip in feedback:
            st.write(tip)

else:
    st.info("⏳ Start by entering your password above.")

# Footer
st.markdown("---")
st.caption("🔐 Developed to help you create stronger passwords & stay safe online.")


# Footer message
st.markdown("---")
st.markdown("<p style='text-align: center;'>This code was created by Rabnawaz Dogar</p>", unsafe_allow_html=True)


