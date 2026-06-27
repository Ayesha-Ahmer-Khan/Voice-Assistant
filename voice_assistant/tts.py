import pyttsx3

engine = pyttsx3.init()

# Optional tuning
engine.setProperty("rate", 175)     # speaking speed
engine.setProperty("volume", 1.0)   # 0 to 1


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()