import datetime
import os
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from Listen import Listen
import pygetwindow as gw
import PyPDF2
import smtplib
from PhoneNumer import Phonenumber_location_tracker
from Speak import Say
import keyboard


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# To get current volume (range 0.0 to 1.0)
currentVolumeDb = volume.GetMasterVolumeLevel()



def volume_up():
    # Simulate the key combination to increase volume (adjust as needed)
    keyboard.send('ctrl+up')

def volume_down():
    # Simulate the key combination to decrease volume (adjust as needed)
    keyboard.send('ctrl+down')

def volume_mute():
    # Simulate the key combination to mute volume (adjust as needed)
    keyboard.send('ctrl+shift+m')

def volume_unmute():
    # Simulate the key combination to unmute volume (adjust as needed)
    keyboard.send('ctrl+shift+u')

# Trigger the volume control functions

def InternetSpeed():
    import speedtest
    Say("Wait a few seconds boss, checking your internet speed")
    st = speedtest.Speedtest()
    dl = st.download()
    dl = dl/(1000000) #converting bytes to megabytes
    up = st.upload()
    up = up/(1000000)
    print(dl,up)
    Say(f"Boss, we have {dl} megabytes per second downloading speed and {up} megabytes per second uploading speed")

def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)
def Date():
    date = datetime.date.today()
    Say(date)
def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)    

def NonInputExecution(query):
    import os 
    if "time" in query:
        Time()
    elif "date" in query:
        Date()
    elif "day" in query:
        Day()  
    elif "bye" in query:
        Say("Ok Sir Take Care")
        exit()
    elif "InternetSpeed" in query:
        InternetSpeed()    
    elif "shutdown the system" in query:
        Say("Boss shutting down the system in 10 seconds")
        time.sleep(10)
        os.system("shutdown /s /t 5")
    elif "restart the system" in query:
        Say("Boss restarting the system in 10 seconds")
        time.sleep(10)
        os.system("shutdown /r /t 5")
    elif "sleep the system" in query:
        Say("Boss the system is going to sleep")
        os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")           
    elif 'screenshot' in query:
        import pyautogui
        import os
        from datetime import datetime
        import random

        directory = r'C:\Users\Mr Ali\Desktop\Screenshots_by_JARVIS\\'

        if not os.path.exists(directory):
            os.makedirs(directory)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        unique_id = random.randint(1, 1000)

        file_name = f'SS_by_JARVIS_{timestamp}_{unique_id}.png'
        file_path = os.path.join(directory, file_name)

        ss = pyautogui.screenshot()
        ss.save(file_path, 'PNG')
        Say("Screenshot saved, Sir")
        # Consider using a different way to communicate the message
        print("Screenshot saved, Sir")       


def InputExecution(tag,query):
    
    if "wikipedia" in tag:
        name = " ".join(query)
        import wikipedia
        result = wikipedia.summary(name)
        Say(result)      
    elif "google" in tag:
        query = ' '.join(query).replace("google","").replace("search","").strip()
        import pywhatkit
        pywhatkit.search(query)
    elif "music" in tag:
        play_music()    
    elif "minimize application" in tag:
        minimize_window()
    elif "maximize application" in tag:
        maximize_window()    


                     

    



       
def condition():
    import psutil
    battery = psutil.sensors_battery()
    
    if battery:
        plugged = battery.power_plugged
        percent = battery.percent
        
        if plugged:
            condition = f"The system is plugged in with {percent}% battery remaining."
        else:
            condition = f"The system is running on battery power with {percent}% battery remaining."
    else:
        condition = "Battery information is not available on this system."
    
    return condition

def play_music():
    """
    Play a music file from the system.

    Asks the user for the song title, then plays the song if it exists in the specified directory.
    """
    # Directory where the songs are stored
    directory = r"C:\Users\Mr Ali\Downloads\Video"

    # Ask the user for the song title
    print("Sir, which song do you want to play?")
    song_title = input("You:  ")
    print(f"Playing... {song_title}")

    # Find the song in the directory
    for file in os.listdir(directory):
        if song_title.lower() in file.lower():
            # Command to play the music file
            command = f'start /min "" "{os.path.join(directory, file)}"'

            # Execute the command
            os.system(command)
            return

    print(f"Sorry, I couldn't find a song with the title {song_title}.")

def minimize_window(title):
    try:
        window = gw.getWindowsWithTitle(title)[0]
        window.minimize()
    except IndexError:
        print(f"No window with title '{title}' found.")

def maximize_window(title):
    try:
        window = gw.getWindowsWithTitle(title)[0]
        window.maximize()
    except IndexError:
        print(f"No window with title '{title}' found.")

def pdf_reader():
    Say("Boss enter the name of the book which you want to read")
    n = Listen()
    n = n.strip()+".pdf"
    book_n = open(n,'rb')
    pdfReader = PyPDF2.PdfFileReader(book_n)
    pages = pdfReader.numPages
    Say(f"Boss there are total of {pages} in this book")
    Say("plsase enter the page number Which I nedd to read")
    num = int(Listen(Say("Enter the page number")))
    page = pdfReader.getPage(num)
    text = page.extractText()
    print(text)
    Say(text)





       