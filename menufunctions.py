

import functions #importing def functions from function.py
import pyaudio
import speech_recognition as sr #import speech recognition from library




def get_audio():
    # This function gets audio input from the user through their microphone

    # Initialize the speech recognition class
    r = sr.Recognizer()

    # Use the microphone to capture the user's speech
    with sr.Microphone() as source:
        # Prompt the user to speak
        print("What is your answer:")

        # Capture the user's speech
        audio = r.listen(source)

    # Try to recognize the speech in the audio and convert it to text
    try:
        # Print the recognized text
        print("You said: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        # Print an error message if the speech could not be recognized
        print("Sorry, I could not understand the audio.")
    



"""
# Import the necessary modules for handling audio input/output
import speech_recognition as sr
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# Create a function to switch between text and audio input
def switch_input_mode():
  # Prompt the user to choose the input mode
  input_mode = input("Enter '1' for text input or '2' for audio input: ")

  # If the user chooses text input, return 'text'
  if input_mode == "1":
    return "text"

  # If the user chooses audio input, return 'audio'
  elif input_mode == "2":
    return "audio"

  # If the user enters an invalid input, print an error message and switch to text input mode
  else:
    print("Invalid input. Switching to text input mode.")
    return "text"




# Create a function to handle text input
def handle_text_input(prompt):
  # Prompt the user for input
  return input(prompt)

# Create a function to handle audio input
def handle_audio_input(prompt):
  # Initialize the recognizer
  r = sr.Recognizer()

  # Use the speech engine to speak the prompt to the user
  engine.say(prompt)
  engine.runAndWait()

  # Listen for the user's response
  with sr.Microphone() as source:
    audio = r.listen(source)

  # Recognize the user's response
  try:
    return r.recognize_google(audio)
  except sr.UnknownValueError:
    print("Sorry, I couldn't understand what you said. Please try again.")
    return handle_audio_input(prompt)
"""