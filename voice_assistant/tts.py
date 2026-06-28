import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 175)


def speak(text):
    print("Assistant:", text)

    engine.stop()  # clear pending queue
    engine.say(text)
    engine.runAndWait()