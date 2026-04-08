import streamlit as st

last_college = ""

def chatbot_response(user):
    global last_college

    if "amity" in user:
        last_college = "amity"
    elif "galgotias" in user:
        last_college = "galgotias"
    elif "sharda" in user:
        last_college = "sharda"

    fees_words = ["fees", "cost", "price"]
    placement_words = ["placement", "package", "job"]

    if any(word in user for word in fees_words):
        if last_college == "amity":
            return "Amity fees: 1.5–2 lakh"
        elif last_college == "galgotias":
            return "Galgotias fees: 1–1.5 lakh"
        elif last_college == "sharda":
            return "Sharda fees: 1.2–2 lakh"
        else:
            return "Please tell the college name first"

    elif any(word in user for word in placement_words):
        if last_college == "amity":
            return "Amity placement: 4–6 LPA"
        elif last_college == "galgotias":
            return "Galgotias placement: 3–5 LPA"
        elif last_college == "sharda":
            return "Sharda placement: 3–6 LPA"
        else:
            return "Please tell the college name first"

    elif "hello" in user or "hi" in user:
        return "Hello! Ask me about colleges"

    elif "bye" in user:
        return "Goodbye!"

    else:
        return "I didn't understand."


#  UI part
st.title("University Chatbot 🎓")

user_input = st.text_input("Ask something:")

if user_input:
    response = chatbot_response(user_input.lower())
    st.write("Bot:", response)
