import streamlit as st
import speech_recognition as sr
import pyttsx3
import time

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# Function to speak the assistant's response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user's voice command
def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        print("Listening for a command...")
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)  # Using Google's recognition API
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand that."
    except sr.RequestError:
        return "Sorry, I'm having trouble connecting to the service."

# Function to respond to user commands
def process_command(command):
    if 'hello' in command:
        speak("Hello! How can I assist you?")
        return "Hello! How can I assist you?"
    elif 'time' in command:
        current_time = time.strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
        return f"The current time is {current_time}"
    elif 'your name' in command:
        speak("I am your virtual assistant.")
        return "I am your virtual assistant."
    else:
        speak("I'm sorry, I didn't understand that command.")
        return "I'm sorry, I didn't understand that command."

# Streamlit UI
def main():
    st.title("Virtual Voice Assistant")
    st.write("Click the button below and speak to your assistant!")

    # Button to start voice interaction
    if st.button('Talk to Assistant'):
        st.write("Listening...")
        user_input = listen()
        st.write(f"You said: {user_input}")
        response = process_command(user_input)
        st.write(f"Assistant: {response}")
        
        # Speak the response
        speak(response)

if __name__ == '__main__':
    main()
