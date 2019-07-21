# import required module
import speech_recognition as sr

print('Get Ready !')

# initialize recognizer
recognizer = sr.Recognizer()

# initialize microphone
mic = sr.Microphone()

print('Speak !')

# with mic as audio source listen for user speech
with mic as source:
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

# print speech instance
print('Speech Instance: ', audio)

# print speech text
speech_text = recognizer.recognize_google(audio)
print('Speech Text: ', speech_text)