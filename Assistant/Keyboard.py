import os
import pickle
import sys
from playsound import playsound
from time import sleep
import cv2
from vosk import Model, KaldiRecognizer
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import pyaudio
from djitellopy import tello
import pyttsx3
import time
import subprocess
import pyjokes
from datetime import datetime
from kivy.lang.builder import Builder
Builder.load_file('origins.ky')


tello = tello.Tello()

kivy.require('2.0.0')

engine = pyttsx3.init()
voice_num = 3

model = Model(os.path.join("C:", os.sep, "Users", os.getlogin(), "OneDrive", "Desktop", "voice 3", "Assistant",
                           "voskmodel", "voskmodel"))
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

plan = ["give me a brain, give me more functions, set up home defence"]
add = False
remove = False

camera = False
active = True
DroneControl = False


class MyRoot(BoxLayout):    # Define a function to print the text in a loop
    def __init__(self):
        super(MyRoot, self).__init__()

    def voice(self):
        # noinspection PyUnboundLocalVariable
        while active:
            # noinspection PyUnboundLocalVariable,PyTypeChecker,PyBroadException
            def commands(text):
                if text == "origins turn off":
                    engine.say("I am turning off")
                    engine.runAndWait()
                    global active
                    active = False
                if text == "origins power off":
                    engine.say("I am shutting off fully")
                    engine.runAndWait()
                    sys.exit()
                if text == "origins go boom":
                    engine.say("going boom")
                    engine.say("3")
                    engine.say("2")
                    engine.say("1")
                    engine.runAndWait()
                    playsound("C://Users//cason//OneDrive//Desktop//voice 3//Assistant//boom.mp3")
                if text == "origins what is up":
                    engine.say("nothing do you need anything")
                    engine.runAndWait()
                if text == "origins tell me a joke":
                    engine.say(pyjokes.get_joke())
                    engine.say("haha")
                    engine.runAndWait()
                if text == "hello origins":
                    engine.say("Hello i am origins your assistant")
                    engine.runAndWait()
                elif text == "origins plans":
                    global plan
                    try:
                        with open("save.p", "rb") as f:
                            plan = pickle.load(f)
                    except:
                        plan = dict
                    engine.say(plan)
                    engine.runAndWait()
                elif text == "origins add plans":
                    global add
                    add = True
                    engine.say("ready to add to plans")
                    engine.runAndWait()
                if not text == "origins add plans":
                    if add:
                        plan.append(text)
                        add = False
                        engine.say(f"added {text} to plan")
                        engine.runAndWait()
                        with open("save.p", "wb") as f:
                            pickle.dump(plan, f)
                    if not add: 
                        pass
                elif text == "origins remove plans":
                    global remove
                    remove = True
                    engine.say("ready to remove plans")
                    engine.runAndWait()
                if not text == "origins remove plans":
                    if remove:
                        plan.remove(text)
                        remove = False
                        engine.say(f"removed {text} from plan")
                        engine.runAndWait()
                        with open("save.p", "wb") as f:
                            pickle.dump(plan, f)
                    if not remove:
                        pass
                elif text == "origins open minecraft":
                    engine.say("I am opening Minecraft")
                    engine.runAndWait()
                    subprocess.call('C://Xbox Games//Minecraft Launcher//Content//gamelaunchhelper.exe')
                elif text == "origins open songs":
                    os.system("Spotify")
                    engine.say("I am opening spotify")
                    engine.runAndWait()
                elif text == "origins open discord":
                    subprocess.call(os.path.join("C:", os.sep, "Users", os.getlogin(), "AppData", "Local", "Discord",
                                     "app-1.0.9013", "Discord.exe"))
                    engine.say("opening discord")
                    engine.runAndWait()
                elif text == "origins open calculator":
                    subprocess.call('C://Windows//System32//calc.exe')
                    engine.say("Calculator is open")
                    engine.runAndWait()
                elif text == "origins open trail makers":
                    subprocess.call("C://XboxGames//Trailmakers//Content//Trailmakers.exe")
                    engine.say("Opening Trailmakers")
                    engine.runAndWait()
                elif text == "origins open over wolf":
                    subprocess.call("C://Program Files (x86)//Overwolf//Overwolf.exe")
                    engine.say("Opening overwolf launcher")
                    engine.runAndWait()
                elif text == "origins open road blocks":
                    subprocess.call(os.path.join("C:", os.sep, "Users", os.getlogin(), "AppData//Local//Roblox//Versions//"
                                                                           "version-31b938635c234124//"
                                                                           "RobloxPlayerLauncher.exe"))
                    engine.say("Opening Roblox")
                    engine.runAndWait()
                elif text == "origins what time is it":
                    ntime = time.strftime("%H:%M:%S")
                    engine.say(f"The current time is{ntime}")
                    engine.runAndWait()
                    print(ntime)
                elif text == "origins what day of the week is it":
                    engine.say(datetime.today().strftime('%A'))
                    engine.runAndWait()
                elif text == "origins what month is it":
                    engine.say(datetime.today().strftime('%m'))
                    engine.runAndWait()
                elif text == "origins what day of the month is it":
                    engine.say(f'it is{datetime.today().day}')
                    engine.runAndWait()
                elif text == "origins all info on right now":
                    ntime = time.strftime("%H:%M:%S")
                    engine.say(datetime.now().strftime("%Y"))
                    engine.say(datetime.today().strftime('%m'))
                    engine.say(f'it is{datetime.today().day}')
                    engine.say(datetime.today().strftime('%A'))
                    engine.say(f"The current time is{ntime}")
                    engine.runAndWait()
                elif text == "origins what is date":
                    engine.say(datetime.today().strftime('%m'))
                    engine.say(f'it is{datetime.today().day}')
                    engine.runAndWait()
                elif text == "origins what year is it":
                    engine.say(datetime.now().strftime("%Y"))
                    engine.runAndWait()
                elif text == "origins drone battery":
                    tello.connect()
                    engine.say(f'{tello.get_battery()} percent of battery for oridrone')
                    engine.runAndWait()
                elif text == "origins start drone":
                    tello.connect()
                    tello.takeoff()
                    engine.say("oridrone has been launched")
                    engine.runAndWait()
                elif text == "origins land drone":
                    tello.land()
                    engine.say("oridrone has landed")
                    engine.runAndWait()
                elif text == "origins drone go up":
                    tello.send_rc_control(0, 0, 30, 0)
                    sleep(2)
                    tello.send_rc_control(0, 0, 0, 0)
                    engine.say("oridrone has gone up")
                    engine.runAndWait()
                elif text == "origins drone go down":
                    tello.send_rc_control(0, 0, -30, 0)
                    sleep(2)
                    tello.send_rc_control(0, 0, 0, 0)
                    engine.say("oridrone has gone down")
                    engine.runAndWait()
                elif text == "origins drone go forward":
                    tello.send_rc_control(0, 30, 0, 0)
                    sleep(2)
                    tello.send_rc_control(0, 0, 0, 0)
                    engine.say("oridrone has gone forward")
                    engine.runAndWait()
                elif text == "origins drone go backward":
                    tello.send_rc_control(0, -30, 0, 0)
                    sleep(2)
                    tello.send_rc_control(0, 0, 0, 0)
                    engine.say("oridrone has gone backward")
                    engine.runAndWait()
                elif text == "origins drone go right":
                    tello.send_rc_control(30, 0, 0, 0)
                    sleep(2)
                    tello.send_rc_control(0, 0, 0, 0)
                    engine.say('oridrone has gone right')
                    engine.runAndWait()
                elif text == "origins drone go left":
                    tello.send_rc_control(-30, 0, 0, 0)
                    sleep(2)
                    tello.send_rc_control(0, 0, 0, 0)
                    engine.say('oridrone has gone left')
                    engine.runAndWait()
                elif text == "origins drone turn right":
                    tello.send_rc_control(0, 0, 0, 50)
                    tello.send_rc_control(0, 0, 0, 0)
                    engine.say('oridrone has turned right')
                    engine.runAndWait()
                elif text == "origins drone turn left":
                    tello.send_rc_control(0, 0, 0, -50)
                    tello.send_rc_control(0, 0, 0, 0)
                    engine.say('oridrone has turned left')
                    engine.runAndWait()
                elif text == "origins drone flip":
                    tello.flip_forward()
                    engine.say("oridrone has flipped")
                    engine.runAndWait()
                elif text == "origins turn on drone camera":
                    tello.connect()
                    tello.streamon()
                    global camera
                    camera = True
                    engine.say("camera is on")
                    engine.runAndWait()
                elif text == "origins turn off drone camera":
                    tello.connect()
                    tello.streamoff()
                    camera = False
                    engine.say("camera is off")
                    engine.runAndWait()
                elif text == "origins drone start keyboard control":
                    global DroneControl
                    DroneControl = True
                    engine.say("you are in control of drone")
                    engine.runAndWait()
                elif text == "origins drone stop keyboard control":
                    DroneControl = False
                    engine.say("you are no longer in control of drone")
                    engine.runAndWait()

            data = stream.read(4896, exception_on_overflow=False)
            if recognizer.AcceptWaveform(data):
                text = recognizer.Result()[14:-3]
                print(text)
                commands(text.lower())
            # noinspection PyUnboundLocalVariable
            if camera:
                img = tello.get_frame_read().frame
                img = cv2.resize(img, (360, 240))
                cv2.imshow("Drone Image", img)
                cv2.waitKey(1)
                tello.send_rc_control(0, 0, 0, 0)
            # noinspection PyUnboundLocalVariable
            if DroneControl:
                key = cv2.waitKey(1) & 0xff
                if key == ord('w'):
                    tello.send_rc_control(0, 30, 0, 0)
                elif key == ord('s'):
                    tello.send_rc_control(0, -30, 0, 0)
                elif key == ord('a'):
                    tello.send_rc_control(30, 0, 0, 0)
                elif key == ord('d'):
                    tello.send_rc_control(-30, 0, 0, 0)
                elif key == ord('e'):
                    tello.rotate_clockwise(30)
                elif key == ord('q'):
                    tello.rotate_counter_clockwise(30)
                elif key == ord('r'):
                    tello.send_rc_control(0, 0, 30, 0)
                elif key == ord('f'):
                    tello.send_rc_control(0, 0, -30, 0)
                elif key == ord('x'):
                    tello.flip_forward()


class Origins(App):
    def build(self):
        return MyRoot()


origins = Origins()
origins.run()
