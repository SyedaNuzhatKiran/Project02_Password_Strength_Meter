import streamlit as st

def check_password(password):
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("Use At Least 8 Characters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Include an Uppercase Letter.")

    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("Include a Lowercase Letter.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Add a Number (0-9).")

    if any(c in "!@#$%^&*" for c in password):
        score += 1
    else:
        tips.append("Use a Special Character (!@#$%^&*).")

    return score, tips

def main():
    st.set_page_config(page_title="Password Strength Meter", layout="centered")
    st.title("🔐 Password Strength Meter")
    password = st.text_input("Enter your password:", type="password")

    if password:
        score, tips = check_password(password)

        if score == 5:
            st.success("✅ Strong Password! Secure & Safe.")
        elif score >= 3:
            st.warning("⚠️ Moderate Password! Consider improving it.")
        else:
            st.error("❌ Weak Password. Follow these tips:")
            for tip in tips:
                st.write("- " + tip)

main()
