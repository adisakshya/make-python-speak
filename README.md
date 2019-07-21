# make-python-speak

This repo illustrates the Speech-To-Text and Text-to-Speech Engine using a simple 'Guess the Word Game'

Before moving on you need to install the modules required to run the scripts: (Make sure you have python3.7 installed)
Run the following command:
```
pip install -r requirements.txt
```
This will install 2 of 3 required modules
Now to install 3rd module PyAudio download it's wheel from this [link]()

# Speech-To-Text

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

There is one package that stands out in terms of ease-of-use: SpeechRecognition.

The SpeechRecognition library acts as a wrapper for several popular speech APIs and is thus extremely flexible. One of these—the Google Web Speech API—supports a default API key that is hard-coded into the SpeechRecognition library. That means you can get off your feet without having to sign up for a service.

Speech-To-Text Example using Speech Recogniton: [speech-to-text.py](https://github.com/adisakshya/make-python-speak/blob/master/examples/speech-to-text.py)