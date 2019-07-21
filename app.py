import random
import time

import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 140)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
engine.setProperty('volume', 1.0)    # setting up volume level between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       # getting details of current voice
engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":
    # set the list of words, maxnumber of guesses, and prompt limit
    WORDS = ["apple", "banana", "grape", "orange", "mango", "lemon"]
    NUM_GUESSES = 3
    PROMPT_LIMIT = 5

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # get a random word from the list
    word = random.choice(WORDS)

    # format the instructions string
    instructions = (
        "I'm thinking of one of these words:\n"
        "{words}\n"
        "You have {n} tries to guess which one.\n"
    ).format(words=', '.join(WORDS), n=NUM_GUESSES)

    # show instructions and wait 3 seconds before starting the game
    # print(instructions)
    print(instructions)
    engine.say(instructions)
    engine.runAndWait()

    time.sleep(2)

    for i in range(NUM_GUESSES):
        # get the guess from the user
        # if a transcription is returned, break out of the loop and
        #     continue
        # if no transcription returned and API request failed, break
        #     loop and continue
        # if API request succeeded but no transcription was returned,
        #     re-prompt the user to say their guess again. Do this up
        #     to PROMPT_LIMIT times
        for j in range(PROMPT_LIMIT):
            sententce = 'Guess {}. Speak!'.format(i+1)
            print(sententce)
            engine.say(sententce)
            engine.runAndWait()

            guess = recognize_speech_from_mic(recognizer, microphone)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            sorry = "I didn't catch that. What did you say?"
            
            print(sorry)
            engine.say(sorry)
            engine.runAndWait()

        # if there was an error, stop the game
        if guess["error"]:
            error = "ERROR: {}".format(guess["error"])
            print(error)
            engine.say(error)
            engine.runAndWait()
            break

        # show the user the transcription
        response = "You said: {}".format(guess["transcription"])
        print(response)
        engine.say(response)
        engine.runAndWait()

        # determine if guess is correct and if any attempts remain
        guess_is_correct = guess["transcription"].lower() == word.lower()
        user_has_more_attempts = i < NUM_GUESSES - 1

        # determine if the user has won the game
        # if not, repeat the loop if user has more attempts
        # if no attempts left, the user loses the game
        if guess_is_correct:
            win = "Correct! You win!".format(word)
            print(win)
            engine.say(win)
            engine.runAndWait()
            break
        elif user_has_more_attempts:
            try_again = "Incorrect. Try again."
            print(try_again)
            engine.say(try_again)
            engine.runAndWait()
        else:
            lose = "Sorry, you lose!\nI was thinking of '{}'.".format(word)
            print(lose)
            engine.say(lose)
            engine.runAndWait()
            break