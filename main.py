import pyttsx3
import speech_recognition as sr

def initialize_text_to_speech():
    """
    Inicializa el motor de texto a voz y configura la voz.
    """
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    return engine

def speak(text: str, engine):
    """
    Convierte el texto en voz y lo reproduce.

    :param text: El texto que se convertirá en voz.
    :param engine: El motor de texto a voz inicializado.
    """
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    """
    Reconoce el discurso del usuario y guarda el resultado en 'output.txt'.
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print('Di algo...')
        audio = recognizer.listen(source)
        print('Grabación terminada.')

        try:
            text = recognizer.recognize_google(audio, language="es-ES")
            print('Google piensa que dijiste:\n' + text)

            with open('output.txt', 'w') as file:
                file.write(text)

        except sr.UnknownValueError:
            print('No se pudo entender el discurso.')
        except sr.RequestError as e:
            print(f'Error en la solicitud a Google: {e}')

if __name__ == "__main__":
    text_to_speech_engine = initialize_text_to_speech()
    recognize_speech()
