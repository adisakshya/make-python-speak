# make-python-speak

This repo illustrates use of the Speech-To-Text and Text-to-Speech Engine using a simple 'Guess the Word Game'

### Setting up environment and installing dependencies

Run the following command to create a virtual-environment:
```
$ virtualenv venv
$ source venv/Scripts/activate
```

Before moving on you need to install the modules required to run the scripts: (Make sure you have python3 installed)

Run the following command:
```
$ pip install -r requirements.txt
```
This will install 2 of 3 required modules
Now to install 3rd module PyAudio
- Download it's wheel from this [link](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
- Extract the zip file and run following command in the folder
```
$ pip install <file-name>
```
- If using python3.7 then you can use the file in PyAudio_wheel-python3.7 folder


# The Game - Guess The Word !

![Title](https://github.com/adisakshya/make-python-speak/blob/master/screenshots/1.PNG?raw=true)

You can start the game by running the following command:
```
py game.py
```
This game consists of two components:
- Speech Engine, that handles all the speech input from the user and also converts the text output to speech making the game a lot more iteractive
- Game Engine, that handles all the game related stuff like starting the game, linking with speech engine and handling play

```
Spend some time playing the game, you will be guided by the bot !
after some fun time you can continue reading below about how the Speech Engine actually work
```

# Speech Recognition (Speech-To-Text)

The overwhelming success of speech-enabled products like Amazon Alexa has proven that some degree of speech support will be an essential aspect of household tech for the foreseeable future. If you think about it, the reasons why are pretty obvious.

Incorporating speech recognition into your Python application offers a level of interactivity and accessibility that few technologies can match.

The accessibility improvements alone are worth considering. Speech recognition allows the elderly, the physically and visually impaired to interact with state-of-the-art products and services quickly and naturally—no GUI needed!

## How Speech Recognition Works - Overview

```
- Speech must be converted from physical sound to an electrical signal with a microphone
- Then to digital data with an analog-to-digital converter
- Once digitized, several models can be used to transcribe the audio to text.
```

Most modern speech recognition systems rely on what is known as a Hidden Markov Model (HMM). This approach works on the assumption that a speech signal, when viewed on a short enough timescale (say, ten milliseconds), can be reasonably approximated as a stationary process—that is, a process in which statistical properties do not change over time.

- In a typical HMM, the speech signal is divided into 10-millisecond fragments. The power spectrum of each fragment, which is essentially a plot of the signal’s power as a function of frequency, is mapped to a vector of real numbers known as cepstral coefficients.

- The dimension of this vector is usually small—sometimes as low as 10, although more accurate systems may have dimension 32 or more. The final output of the HMM is a sequence of these vectors.

To decode the speech into text, groups of vectors are matched to one or more phonemes—a fundamental unit of speech.

NOTE: This calculation requires training, since the sound of a phoneme varies from speaker to speaker, and even varies from one utterance to another by the same speaker. A special algorithm is then applied to determine the most likely word (or words) that produce the given sequence of phonemes.

One can imagine that this whole process may be computationally expensive.
In many modern speech recognition systems, neural networks are used to simplify the speech signal
using techniques for feature transformation and dimensionality reduction before HMM recognition.
Voice activity detectors (VADs) are also used to reduce an audio signal to only the portions that are likely to contain speech.
This prevents the recognizer from wasting time analyzing unnecessary parts of the signal.

---
**Fortunately, as a Python programmer, you don’t have to worry about any of this. A number of speech recognition services are available for use online through an API, and many of these services offer Python SDKs. :P**

### Picking a Speech Recognition Package

There is one package that stands out in terms of ease-of-use: [SpeechRecognition](https://github.com/Uberi/speech_recognition)

The SpeechRecognition library acts as a wrapper for several popular speech APIs and is thus extremely flexible. One of these—the Google Web Speech API—supports a default API key that is hard-coded into the SpeechRecognition library. That means you can get off your feet without having to sign up for a service.

Speech-To-Text Example using Speech Recogniton: [speech-to-text.py](https://github.com/adisakshya/make-python-speak/blob/master/examples/speech-to-text.py)


# Speech Synthesis (Text-To-Speech)

Speech synthesis is the artificial production of human speech. A text-to-speech (TTS) system converts normal language text into speech.

An intelligible text-to-speech program allows people with visual impairments or reading disabilities to listen to written words on a home computer. The quality of a speech synthesizer is judged by its similarity to the human voice and by its ability to be understood clearly.

![WikiPedia](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/TTS_System.svg/825px-TTS_System.svg.png)
Image Source: WikiPedia

A text-to-speech system (or "engine") is composed of two parts:

- A front-end
- A back-end

The front-end has two major tasks. 
- It converts raw text containing symbols like numbers and abbreviations into the equivalent of written-out words. This process is often called **text normalization, pre-processing, or tokenization**. 
- The front-end then assigns phonetic transcriptions to each word, and divides and marks the text into prosodic units, like phrases, clauses, and sentences. The process of assigning phonetic transcriptions to words is called **text-to-phoneme or grapheme-to-phoneme conversion**. Phonetic transcriptions and prosody information together make up the symbolic linguistic representation that is output by the front-end.

The back-end—often referred to as the **synthesizer**—then converts the symbolic linguistic representation into sound. In certain systems, this part includes the computation of the target prosody (pitch contour, phoneme durations), which is then imposed on the output speech.

---
**Again fortunately, as a Python programmer, you don’t have to worry about any of this. A number of speech synthesis services are available. :P**

### Picking a Speech Synthesis Package

The one package that I have used here is: [pyttsx3](https://pyttsx3.readthedocs.io/en/latest/)

```
- Easy to set-up
- Easy to use
- Flexible Controls
```

Text-To-Speech Example using pyttsx3: [text-to-speech.py](https://github.com/adisakshya/make-python-speak/blob/master/examples/text-to-speech.py)
