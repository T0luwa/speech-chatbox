import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import streamlit as st
import speech_recognition as sr
# Load the text file and preprocess the data

with open('youngsheldon.txt', 'r', encoding='utf-8') as f:
    data = f.read().replace('\n', ' ')
# Tokenize the text into sentences
sentences = sent_tokenize(data)
# Define a function to preprocess each sentence
def get_user_input():
    # Create a recognizer object
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise levels
        recognizer.adjust_for_ambient_noise(source)

        # Capture the audio
        audio = recognizer.listen(source)

    try:
        # Use the recognizer to convert speech to text
        user_input = recognizer.recognize_google(audio)
        print("User input (speech):", user_input)
        return user_input

    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("Speech recognition service error:", str(e))

    # If speech recognition fails or user prefers text input, fall back to text input
    user_input = input("User input (text): ")
    return user_input

def chatbot():
    # Initialize the chatbot
    print("Chatbot initialized.")

    while True:
        # Get user input
        user_input = get_user_input()

        # Process user input and generate response
        # Your chatbot logic goes here
        response = "This is the chatbot's response to: " + user_input

        # Print and/or output the chatbot response
        print("Chatbot response:", response)

        # Terminate the loop if a specific condition is met
        if user_input.lower() == "exit":
            break

# Call the chatbot function
chatbot()
# Create a Streamlit app
def main():
    st.title("Chatbot App")
    st.write("Enter your query below.")

    # Radio button to select input type
    input_type = st.radio("Select Input Type", ("Text", "Speech"))

    user_input = ""

    if input_type == "Text":
        user_input = st.text_input("User Input (Text)")

    elif input_type == "Speech":
        user_input = transcribe_speech()

    if st.button("Submit"):
        response = chatbot(user_input)
        st.write("Chatbot Response:", response)
        speak(response)

if _name_ == "_main_":
    main()
