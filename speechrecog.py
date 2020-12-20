#library to perform speech recognition
import speech_recognition as sr

#libraries to implement parallel processing in real time 
from multiprocessing import Process
import threading

#time library
import time

#imports from within the directory 
import pptcontrol
import start
import similar

#win32 API client for python
import win32com.client

global t1
global t2

#Setting default values
cur_res = "silent"
next_list = ["next","forward","moving ahead","moving on", "move on to","moving on to"]
back_list = ["back","backward"]
curslide = 0

# Function to perform speech recognition in real time - 1 (Process 1) 
def func1():
    global cur_res
    global t1
    global t2
    try:
        r = sr.Recognizer()
        mic = sr.Microphone(device_index=0) 
        with mic as source:
            audio = r.record(mic, duration=2)
        temp34 = r.recognize_google(audio, language='en-US')
        print(temp34)
        cur_res = temp34
        action()
        time.sleep(1.5)
        func1()
    except:
        time.sleep(2)
        print("Silent")
        func1()

# Function to perform speech recognition in real time - 2 (Process 2) 
def func2():
    global cur_res
    global t1
    global t2
    try:
        temp = sr.Recognizer()
        mic2 = sr.Microphone(device_index=0) 
        with mic2 as source:
            audio2 = temp.record(mic2, duration=2)
        temp3 = temp.recognize_google(audio2, language='en-US')
        print(temp3)
        cur_res = temp3
        action()
        time.sleep(1.5)
        func2()
    except:
        time.sleep(2)
        print("Silent")
        func2()

# Threading (Process 3)
def start(file):
    global t1
    global t2
    global counter
    counter = 0
    t1 = threading.Thread(target=func1)
    t2 = threading.Thread(target=func2)
    t3 = threading.Thread(target=action)
    t1.start()
    t3.start()
    time.sleep(2)
    t2.start()

# Function to use functions from in-directory files to run the main application 
def action():
    global cur_res
    global presentation
    print(cur_res)
    global counter
    global app
    global next_list
    global back_list
    global curslide
    from test import gettotal
    from test import getheaders
    from test import getnextres
    from test import getbackres
    if(counter!=1):
        counter=1
        app = win32com.client.Dispatch("PowerPoint.Application")
        presentation = app.Presentations.Open(FileName="pptsample.pptx", ReadOnly=1, WithWindow=False)
        presentation.SlideShowSettings.Run()
    flag = 0
    list_for_foward = getnextres() + next_list + getheaders()[curslide+1]
    for wor in list_for_foward:
        if(similar.similarcheck(cur_res,wor)>0.3):
            if(curslide < gettotal()):
                presentation.SlideShowWindow.View.Next()
                curslide +=1
                flag = 1
            else:
                presentation.SlideShowWindow.View.Exit()
                app.Quit()
    if(flag != 1):
        list_for_backward = getbackres() + getheaders()[curslide-1] + back_list
        for string2 in list_for_backward:
            if(similar.similarcheck(cur_res,string2)>0.3 and curslide!=0):
                presentation.SlideShowWindow.View.Previous()
                curslide=curslide-1
