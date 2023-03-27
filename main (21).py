import random
import speech_recognition as sr

# List of words to guess from
word_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Select a random word from the list
word_to_guess = random.choice(word_list)

# Initialize the speech recognition engine
r = sr.Recognizer()

# Start the game loop
while True:
    # Listen for the user to say a word
    with sr.Microphone() as source:
        print("Say a word:")
        audio = r.listen(source)

    # Try to recognize the word the user said
    try:
        guessed_word = r.recognize_google(audio)
        print(f"You guessed: {guessed_word}")
    except sr.UnknownValueError:
        print("Sorry, I didn't understand what you said.")
        continue

    # Check if the user guessed the correct word
    if guessed_word == word_to_guess:
        print("Congratulations, you guessed the word!")
        break
    else:
        print("Sorry, that's not the word I'm thinking of. Try again.")

