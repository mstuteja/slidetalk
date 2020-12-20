#Library to use win32 API in python to control
import win32com.client

#Functions to control flow of slideshow 
class pptcontrol:
    def __init__(self):
        print("hi")

    #function for file selection
    def setPath(self,file):
        self.app = win32com.client.Dispatch("PowerPoint.Application")
        self.presentation = self.app.Presentations.Open(FileName=file, ReadOnly=1)
        self.presentation.SlideShowSettings.Run()

    #function to transition to next slide
    def nextSlide(self):
        print("Next chal raha hai")
        self.presentation.SlideShowWindow.View.Next()

    #function to transition to previous slide
    def prevSlide(self):
        self.presentation.SlideShowWindow.View.Previous()

    #function to exit slideshow
    def endPpt(self):
        self.presentation.SlideShowWindow.View.Exit()
        self.app.Quit()

