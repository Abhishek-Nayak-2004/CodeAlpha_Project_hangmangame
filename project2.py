import nltk
import random
import string
import re

# Download NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Preprocess input text
def preprocess(text):
    # Lowercase the text
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

# Sample responses
responses = {
    "greetings": ["Hello!", "Hi there!", "Greetings!", "How can I help you?"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "default": ["I'm not sure how to respond to that.", "Can you please rephrase?", "Let's talk about something else."]
}

# Function to get a response
def get_response(user_input):
    user_input = preprocess(user_input)
    if any(greet in user_input for greet in ["hi", "hello", "hey", "greetings"]):
        return random.choice(responses["greetings"])
    elif any(thank in user_input for thank in ["thanks", "thank you"]):
        return random.choice(responses["thanks"])
    elif any(bye in user_input for bye in ["bye", "goodbye", "see you"]):
        return random.choice(responses["goodbye"])
    else:
        return random.choice(responses["default"])

# Main chat loop
def chat():
    print("Chatbot: Hello! I am a simple chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()