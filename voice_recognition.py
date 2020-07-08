import speech_recognition as sr
import jarvis_module as jm


# not used as of now
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen((source))
    return r, audio


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen((source))

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='english')
        print(f'user said: {query}\n')
    except Exception as e:
        print("Say that again please\n")
        query = None

    return query


def get_query(engine):
    query = None
    while query is None:
        # r, audio = get_audio()
        query = command()
    if 'go to sleep' in query.lower():
        speak(engine, "Initializing sleep mode.")
        jm.init_talk(engine)
    return query


def speak(engine, text):
    engine.say(text)
    engine.runAndWait()
