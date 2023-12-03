import speech_recognition as sr

def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,4)

    try:
        print("Recogninzing...")
        query = r.recognize_google(audio,language="en-ur")
        print(f"You Said : {query}")

    except:
        return ""

    query = str(query)
    return query.lower()



# from vosk import Model, KaldiRecognizer
# import pyaudio

# model = Model("Listen\vosk-model-small-en-us-0.15.zip")
# recognizer = KaldiRecognizer(model, 16000)

# mic = pyaudio.PyAudio()
# stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
# stream.start_stream()

# def Listen():
#     print("")
#     print("Listening...")
#     print("")

#     while True:

#         data = stream.read(4096)

#         if recognizer.AcceptWaveform(data):
#             text = recognizer.Result()
#             p = text[14:-3]
#             print(f"You Said : {p}")

#             if len(p)>0:
#                 return p
            
#             else:
#                 break


