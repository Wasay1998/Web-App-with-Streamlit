import re
import random
import string
import streamlit as st

# Function to generate a strong password
def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.sample(chars, length))

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    weak_passwords = {"123456", "password", "123456789", "qwerty", "12345", "123123", "password1"}
    if password.lower() in weak_passwords:
        feedback.append("❌ Your password is too common. Choose a more secure one.")
        score = 0  
    
    return score, feedback


st.markdown(
    """
    <style>
        /* Global text color */
        html, body, .stApp {
            color: white !important;
            background-color: #0d1117 !important;
        }

        /* Input box styling */
        .stTextInput input {
            font-size: 18px !important;
            padding: 12px !important;
            border-radius: 10px !important;
            border: 2px solid #FFD700 !important;
            background-color: #222 !important;
            color: white !important;
            text-align: center;
            box-shadow: 0px 0px 10px rgba(255, 215, 0, 0.4);
        }
        /* Input box styling */
        div[data-testid="stTextInput"] label { 
            color: white !important; /* Input Label Text */
            font-size: 18px;
            font-weight: bold;
        }

        /* Button styling */
        .stButton button {
            font-size: 18px !important;
            padding: 12px !important;
            border-radius: 10px !important;
            background: linear-gradient(to right, #FFD700, #FFA500);
            color: black !important;
            font-weight: bold;
            border: none;
            transition: 0.3s;
            box-shadow: 0px 5px 15px rgba(255, 165, 0, 0.5);
        }

        .stButton button:hover {
            background: linear-gradient(to right, #FFA500, #FF4500);
            transform: scale(1.05);
            box-shadow: 0px 5px 20px rgba(255, 69, 0, 0.6);
        }

        /* Message styling */
        .stSuccess {
            color: #32CD32 !important;
            font-weight: bold;
            text-shadow: 0px 0px 10px #32CD32;
        }
        .stWarning {
            color: #FFA500 !important;
            font-weight: bold;
            text-shadow: 0px 0px 10px #FFA500;
        }
        .stError {
            color: #FF4500 !important;
            font-weight: bold;
            text-shadow: 0px 0px 10px #FF4500;
        }

        /* Navigation Bar */
        .navbar {
            background: linear-gradient(to right, #FFD700, #FFA500);
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: black;
            margin-bottom: 30px;
            box-shadow: 0px 5px 15px rgba(255, 165, 0, 0.5);
        }

        /* Footer */
        .footer {
            text-align: center;
            padding: 20px;
            font-size: 16px;
            color: #FFD700;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Navigation Bar
st.markdown('<div class="navbar">🔐 Password Security Tool</div>', unsafe_allow_html=True)

# Streamlit UI
st.title("🔐 Password Strength Meter")

# Instructions
st.markdown(
    """
    - Enter your password in the input box below.  
    - Click **'Check Strength'** to analyze its security.  
    - If your password is weak, you'll get suggestions for improvement.  
    - If you need a **strong password**, we will generate one for you.  
    """
)

password = st.text_input("Enter your password", type="password")

if st.button("Check Strength"):
    if password:
        score, feedback = check_password_strength(password)
        
        if score >= 5:
            st.success("✅ Strong Password! 🔥")
        elif score >= 3:
            st.warning("⚠️ Moderate Password - Improve it for better security. ⚡")
        else:
            st.error("❌ Weak Password - Follow these tips to strengthen it:")
            for tip in feedback:
                st.write("- ", tip)
            st.info("🔹 Suggested Strong Password: " + generate_strong_password())
    else:
        st.error("❌ Please enter a password to check.")

# Footer
st.markdown('<div class="footer">Developed by Abdul Wasay 🚀</div>', unsafe_allow_html=True)
