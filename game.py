# import required modules
import random
import time
import pyfiglet
import pyttsx3
import speech_recognition as sr

# Class - Speech Engine
class SpeechEngine(object):

    # init
    def __init__(self):

        # start speech engine
        self.engine = pyttsx3.init()

        # set rate and volume
        self.engine.setProperty('rate', 160)
        self.engine.setProperty('volume', 1.0)

        # set voice
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        
        # initialize recognizer and set energy threshold
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 400
        self.recognizer.dynamic_energy_threshold = False

        # initialize microphone
        self.microphone = sr.Microphone()
    
    # speak text (Text To Speech)
    def speak(self, text):

        self.engine.say(text)
        self.engine.runAndWait()
    
    # recognize speech (speech to text)
    def recognize_speech(self, recognizer, microphone):

        """
        Transcribe speech recorded from `microphone`.
        Returns a dictionary with three keys:
        "success": a boolean indicating whether or not the API request was
                successful
        "error":   `None` if no error occured, otherwise a string containing
                an error message if the API could not be reached or
                speech was unrecognizable
        "transcription": `None` if speech could not be transcribed,
                otherwise a string containing the transcribed text
        """

        # check that recognizer and microphone arguments are of appropriate types
        if not isinstance(recognizer, sr.Recognizer):
            raise TypeError("recognizer must be Recognizer instance")
        
        if not isinstance(microphone, sr.Microphone):
            raise TypeError("microphone must be Microphone instance")
        
        # adjust recognizer sensitivity to ambient noise
        # and record audio from the microphone
        with microphone as speech_source:
            recognizer.adjust_for_ambient_noise(speech_source)
            audio = recognizer.listen(speech_source)
        
        # response object
        response = {
            "success": True,
            "error": None,
            "transcription": None
        }

        # try recognizing the speech
        # if RequestError / UnknownValueError exception is caught,
        # then update response object accordingly
        try:
            response['transcription'] = recognizer.recognize_google(audio)
        except sr.RequestError:
            # API was unreachable / unresponsive
            response['success'] = False
            response['error'] = 'API unavailable'
        except sr.UnknownValueError:
            # speech was unintelligible
            response['error'] = 'Unable to recognize speech'
        
        return response

    # stop speech engine
    def stop_engine(self):
        self.engine.stop()


# Class - Game Engine
class GameEngine(object):

    def __str__(self):
        return 'Guess The Word !'
    
    # init
    def __init__(self):

        self.words = ['apple', 'banana', 'grape', 'orange', 'mango', 'lemon']
        self.number_of_guesses = 3
        self.prompt_limit = 5
        self.game_speech_engine = SpeechEngine()
        self.word = random.choice(self.words)

    # greet user
    def greet(self):

        greeting = "\nHello World !\nWelcome to Guess The Word Game !\nLet's see if you can read my mind...\n"
        print(greeting)
        self.game_speech_engine.speak(greeting)
    
    # speak instructions
    def instructions(self):

        instructions = (
            "I'm thinking of one of these words:\n"
            "{words}\n"
            "You have {n} tries to guess which one.\n"
            "Let's Go !\n"
        ).format(words=', '.join(self.words), n=self.number_of_guesses)
        print(instructions)
        self.game_speech_engine.speak(instructions)
    
    # start game
    def play_game(self):

        for i in range(self.number_of_guesses):
            
            # get the guess from the user
            # if a transcription is returned, break out of the loop and
            #     continue
            # if no transcription returned and API request failed, break
            #     loop and continue
            # if API request succeeded but no transcription was returned,
            #     re-prompt the user to say their guess again. Do this up
            #     to PROMPT_LIMIT times

            for j in range(self.prompt_limit):

                attempt = 'Guess {}. Speak !'.format(i+1)
                print(attempt)
                self.game_speech_engine.speak(attempt)

                guess = self.game_speech_engine.recognize_speech(self.game_speech_engine.recognizer, self.game_speech_engine.microphone)
                if guess['transcription']:
                    break
                elif not guess['success']:
                    break
                
                pardon = "Sorry ! I didn't catch that. What did you say?\n"
                print(pardon)
                self.game_speech_engine.speak(pardon)

            # if there was an error, stop the game
            if guess['error']:
                error = 'Error: {}'.format(guess['error'])
                print(error)
                self.game_speech_engine.speak(error)
                break
                
            # show the user the transcription
            response = 'You said: {}'.format(guess['transcription'])
            print(response)
            self.game_speech_engine.speak(response)

            # determine if guess is correct and if any attempts remain
            guess_is_correct = guess["transcription"].lower() == self.word.lower()
            user_has_more_attempts = i < self.number_of_guesses - 1

            # determine if the user has won the game
            # if not, repeat the loop if user has more attempts
            # if no attempts left, the user loses the game
            if guess_is_correct:
                win = "Correct! You win!"
                print(pyfiglet.figlet_format(win))
                self.game_speech_engine.speak(win)
                break
            elif user_has_more_attempts:
                try_again = "Incorrect. Try again.\n"
                print(try_again)
                self.game_speech_engine.speak(try_again)
            else:
                you_lose = "Sorry, you lose!\nI was thinking of '{}'.\n".format(self.word)
                print(you_lose)
                self.game_speech_engine.speak(you_lose)
                break
    
    # end game
    def stop_game_engine(self):

        self.game_speech_engine.stop_engine()

# main function
def main():

    # initialize game engine
    obj = GameEngine()
    head = pyfiglet.figlet_format(str(obj))
    print(head)
    
    # greet the user
    obj.greet()

    # tell the instructions
    obj.instructions()

    # play the game
    obj.play_game()

    # stop the game engine
    obj.stop_game_engine()

if __name__ == "__main__":
    
    # call to main() function
    main()     
        
