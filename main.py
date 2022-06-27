import speech_recognition as sr
import pyttsx3 as tts
import wikipedia as wiki
import datetime as dt
import time
import pywhatkit
import json
import pyjokes
from chitti import reply

run = True
speaker = tts.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', 'en_US')
speaker.setProperty('rate', 170)
r = sr.Recognizer()
mic = sr.Microphone()
tell = 0


def ask_user():
    global tell
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=5)
            print("say something...")
            audio = r.listen(source)

        text = r.recognize_google(audio)
        text = text.lower()
        print("user: ", text)
        if 'mini' in text:
            text = text.replace('mini', '')
        return text
    except:
        speak('Please repeat. I did not understand.')


def show_results(text):
    if 'who is' in text:
        text = text.replace('who is', '')
        data = wiki.summary(text, 3)
        speak(data)
    elif 'what is' in text:
        text = text.replace('who is', '')
        try:
            data = wiki.summary(text, 2)
        except:
            data = 'could not find anything'
        speak(data)
    elif 'is equal to' in text:
        text = text.replace('is equal to', '')
        result = text + ' is equal to ' + str(eval(text))
        speak(result)
    elif 'time' in text:
        # time = str(dt.time())
        '''now = dt.now()
        time = now.strftime("%H:%M %p")'''
        t = time.localtime()
        ct = time.strftime("%I:%M %p", t)
        speak('time is => ' + ct)
    elif 'date' in text:
        date = dt.date.today().strftime("%B %d, %Y")
        speak(date)
    elif 'play' in text:
        text = text.replace('play', '')
        speak("Playing...")
        pywhatkit.playonyt(text)
    elif 'bye-bye' in text:
        print('Bye, See you later')
        global run
        run = False
        speak('Bye, See you later')
    elif 'send a message to' in text:
        name = text.replace('send a message to', '')
        phone_no = 0
        with open('contact_dir.json', 'r') as contacts:
            data = json.load(contacts)
        for key, value in data.items():
            if key in name:
                phone_no = value
        if phone_no == 0:
            speak('contact does not exist')
        else:
            speak('what do you want to say')
            global tell
            tell = 1
            msg = ask_user()
            print('msg: ' + str(msg))
            speak('Sending message...')
            send_message(msg, phone_no)
    elif 'i love you' in text:
        speak('Sorry, I am not available.')
    elif 'tell me a joke' in text:
        joke = pyjokes.get_joke(category='all')
        speak(joke)
    else:
        ans = reply(text)
        speak(str(ans))

def send_message(msg, phone_no):
    t = time.localtime()
    ct = time.strftime("%H:%M", t)
    msg_time = ct.split(':')
    if int(msg_time[1]) < 58:
        msg_time[1] = int(msg_time[1]) + 2
    else:
        msg_time[1] = 0
        if int(msg_time[0] < 24):
            msg_time[0] = int(msg_time[0]) + 1
        else:
            msg_time[0] = 0
    pywhatkit.sendwhatmsg(phone_no, msg, int(msg_time[0]), int(msg_time[1]))


def speak(data):
    speaker.say(data)
    print("Mini: " + data)
    speaker.runAndWait()


# while run:
#speak('oye chotu')
query = ask_user()
#query = 'what is your name'
if query:
    show_results(query)
#speak(str(reply(query)))