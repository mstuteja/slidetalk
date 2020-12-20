#speech recognition library
import speech_recognition as sr

#parallel processing tools
from multiprocessing import Process

#time library
import time

#in-directory imports 
import pptcontrol
import extractdata as exda
import pptcontrol as cont
from speechrecog import start

global totalSlides
totalSlides = 0
next_extra = ""
back_extra = ""

global headers
headers = []

global next_res
next_res = []
global back_res
back_res = []

# Function to implement manipulation of lists and simultaneous initiation of speech recognition in real time
def startf(file):
    Process()
    start(file)

# Function to convert user input into lists for further processing 
def process():
    global next_extra
    global back_extra
    global next_res
    global back_res
    next_res = next_extra.split(",")
    back_res = back_extra.split(",")

# Function to extract required data to understand user input futher processing 
def predata(path):
    global headers
    global totalSlides
    pptpath = path
    try:
        pptdata = exda.extractText(pptpath)
        headers = exda.getHeader(pptdata)
        print(headers)
        totalSlides = len(pptdata)
        return "Done"
    except:
        return "Error"
