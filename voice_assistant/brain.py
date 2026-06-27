def generate_response(user_text):
    text = user_text.lower()

    if "hello" in text:
        return "Hello. How can I help you?"

    elif "how are you" in text:
        return "I am functioning normally."

    elif "your name" in text:
        return "I am your assistant."

    elif "bye" in text:
        return "Goodbye."

    else:
        return f"You said {user_text}"