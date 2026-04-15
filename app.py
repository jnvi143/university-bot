import streamlit as st

last_college = ""

def chatbot_response(user):
    global last_college

    #  College detection (fixed)
    if "amity" in user:
        last_college = "amity"
    elif "galgotias" in user:
        last_college = "galgotias"
    elif "sharda" in user:
        last_college = "sharda"
    elif "noida international" in user:
        last_college = "niu"
    elif "jiit" in user:
        last_college = "jiit"
    elif "gl bajaj" in user:
        last_college = "glb"

    fees_words = ["fees", "cost", "price"]
    placement_words = ["placement", "package", "job"]

    # Fees
    if any(word in user for word in fees_words):
        if last_college == "amity":
            return "Amity fees: 1.5–2 lakh"
        elif last_college == "galgotias":
            return "Galgotias fees: 1–1.5 lakh"
        elif last_college == "sharda":
            return "Sharda fees: 1.2–2 lakh"
        elif last_college == "niu":
            return "Noida International University fees: ~1 lakh/year"
        elif last_college == "jiit":
            return "JIIT fees: high (~2.5–3 lakh/year)"
        elif last_college == "glb":
            return "GL Bajaj fees: ~1 lakh/year"
        else:
            return "Please tell the college name first"

    #  Placement
    elif any(word in user for word in placement_words):
        if last_college == "amity":
            return "Amity placement: 4–6 LPA"
        elif last_college == "galgotias":
            return "Galgotias placement: 3–5 LPA"
        elif last_college == "sharda":
            return "Sharda placement: 3–6 LPA"
        elif last_college == "niu":
            return "Noida International placement: 6–7 LPA"
        elif last_college == "jiit":
            return "JIIT placement: 10–11 LPA (average)"
        elif last_college == "glb":
            return "GL Bajaj placement: 6–7 LPA"
        else:
            return "Please tell the college name first"

    
    elif user.strip() in ["hi", "hello"]:
        return "Hello! Ask me about colleges"

    elif "bye" in user:
        return "Goodbye!"

    else:
        return "I didn't understand. Ask about fees or placements."

# 🎨 UI part
st.title("University Assistant Bot 🎓")

user_input = st.chat_input("Type your question here:")

if user_input:
    st.chat_message("user").write(user_input)
    response = chatbot_response(user_input.lower())
    st.chat_message("assistant").write(response)

# Sidebar
st.sidebar.title("Menu")
st.sidebar.write("Available Colleges:")
st.sidebar.write("Amity, Sharda, Galgotias, NIU, JIIT, GL Bajaj")
