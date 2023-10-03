import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Say something')
        audio = r.listen(source)
        print('done')

        try:
            text = r.recognize_google(audio)
            print('Google thinks you said:\n' + text)

            remember = open('output.txt', 'w')
            remember.write(text)
            remember.close()

        except Exception as e:
            print(e)

get()
