import pyttsx3
import webbrowser
from yt_module import handle_youtube
import voice_recognition as vr


def initializer():
    print("Initializing Jarvis")
    engine = pyttsx3.init('espeak')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[11].id)
    return engine


def init_talk(engine):
    query = vr.get_query(engine)
    if 'Jarvis' in query:
        vr.speak(engine, "Yes Sir?")
        queries(engine)
    else:
        init_talk(engine)


def queries(engine):
    query = vr.get_query(engine)
    if 'jarvis' in query.lower():
        vr.speak(engine, "I am at your service sir")
        queries(engine)
    # if 'go to sleep' in query.lower():
    #     speak(engine, "Initializing sleep mode.")
    #     return
    if 'open Google Chrome' in query:
        webbrowser.open('https://www.google.pl/')
    if 'open youtube' in query.lower():
        vr.speak(engine, "Right away Sir")
        handle_youtube(engine)
