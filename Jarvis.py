import random
import json
import torch
from Brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize
import win32gui
import win32con
from Memory import Memory


ai_memory = Memory()

def change_window_state(title, state):
    def window_enum_callback(hwnd, _):
        if win32gui.IsWindowVisible(hwnd) and title.lower() in win32gui.GetWindowText(hwnd).lower():
            win32gui.ShowWindow(hwnd, state)

    win32gui.EnumWindows(window_enum_callback, None)


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json",'r') as json_data:
    intents = json.load(json_data)
    
FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()


# {strTime}
# {strTime}
#----------------------------------
def WishMe():
    import datetime
    hour = int(datetime.datetime.now().hour)
    strTime = datetime.datetime.now().strftime("%H:%M")
    if hour>=13 and hour<18:
        Say(f"Good Morning Sir!  ")
        print(f'Good morning sir!  ')

    elif hour>=0 and hour<6:
        Say(f"Good Afternoon sir! Its {strTime}")
        print(f"Good afternoon sir! Its {strTime}")

    else:
        Say(f"Good evening sir! Its {strTime}")
        print(f"Good evening sir! Its {strTime}")



#----------------------------------

Name = "Jarvis"
from Listen import Listen
from Speak import Say
from Task import NonInputExecution
from Task import InputExecution
# Say("unhhnhnu")

def save_chat_to_file(chat_history):
    with open('history.txt', 'a') as file:
        for chat in chat_history:
            file.write(chat + '\n')

chat_history = []


if __name__ == "__main__":
        WishMe()

while True:
    
    sentence = input("you: ")
    result = str(sentence)
    chat_history.append("User: " + result)
    ai_memory.store_chat_memory("User: " + result)   

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)

    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    predicted_tag = tags[predicted.item()]

    if prob.item() > 0.99:
        for intent in intents['intents']:
            if predicted_tag == intent["tag"]:
                reply = random.choice(intent["responses"])
                chat_history.append("Jarvis: " + reply)

                ai_memory.store_chat_memory("Jarvis: " + reply)
    

        if "time" in reply:
            NonInputExecution(reply)
        elif "date" in reply:
            NonInputExecution(reply)
        elif "day" in reply:
            NonInputExecution(reply)  
        elif 'volume Down' in reply:
            from Task import volume_down
            volume_down()
        elif 'volume up' in reply:
            from Task import volume_up
            volume_up()
        elif 'volume mute' in reply:
            from Task import volume_mute
            volume_mute()
        elif "volume unmute" in reply:
            from Task import volume_unmute 
            volume_unmute()   
        elif "screenshot" in reply:
            NonInputExecution(reply)    
        elif "shutdown the system" in reply:
            NonInputExecution(reply)  
        elif " restart the system" in reply:
            NonInputExecution(reply)
        elif "sleep the system" in reply:
            NonInputExecution(reply)
        elif 'minimize' in tag:
            title = tag.replace('minimize', '').strip()  # get the title from the command
            change_window_state(title, win32con.SW_MINIMIZE)  # minimize the window
        elif 'maximize' in tag:
            title = tag.replace('maximize', '').strip()  # get the title from the command
            change_window_state(title, win32con.SW_MAXIMIZE)
        elif "InternetSpeed" in tag:
            NonInputExecution(reply)
        elif "condition" in tag:
            from Task import condition
            condition = condition()
            Say(condition) 
        elif "weather" in tag:
            from Features.Weather import weather
            response = weather()
            Say(response)
        elif "News" in tag:    
            from Features.news import tell_news
            tell_news()                                 
        elif "wikipedia" in reply:
            InputExecution(reply,sentence)
        elif "google" in tag:
            InputExecution(reply,sentence)   
        elif "music" in tag:
            from Task import play_music
            play_music()  
        elif "Download Movies" in tag:
            from Features.Downlod_from_multilive import download_file_from_website
            download_file_from_website()    

        elif "schedule" in tag:
            from Task import schedule_task
            schedule_task()
        elif "check schedule" in tag:
            from Task import check_schedule
            check_schedule()
        elif "mark task complete" in tag:
            from Task import mark_task_complete
            mark_task_complete()        
        elif "list task completed" in tag:
            from Task import list_completed_tasks
            list_completed_tasks()
        elif "notify upcoming task" in tag:
            from Task import notify_upcoming_tasks
            notify_upcoming_tasks()

        elif "open" in tag:
            from open_close import open_application
            open_application(Name)
        elif "close" in tag:
            from open_close import close_application
            close_application(Name)

        elif 'goodbye' in tag or 'bye' in tag:
            import sys
            Say('Thanks for using me sir, have a good day! Jarvis is signing out of duty.')
            sys.exit()   
        else:
            Say(reply)





        save_chat_to_file(chat_history)
        
        ai_memory.display_memory()


