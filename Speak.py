import pyttsx3

def Say(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Set the voice
    engine.setProperty('rate', 180)
    print("    ")
    print(f"Jarvis: {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("    ")


