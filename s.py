#coding:utf-8

import speech_recognition as sr

def recognize(file):
# obtain audio from the microphone
       r = sr.Recognizer()

       h = sr.WavFile(file)

       with h as source:
           audio = r.record(source)
# recognize speech using Sphintry:
       return(r.recognize_sphinx(audio))


'''

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()

h = sr.WavFile('out.wav')

with h as source:
      audio = r.record(source)
# recognize speech using Sphintry:
#r.recognize_sphinx(audio)



print("Sphinx thinks you said " + r.recognize_sphinx(audio))
'''