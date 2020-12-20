#in-directory imports
from start import totalSlides
from start import headers
from start import next_res
from start import back_res


# Tip: To avoid circular importing errors, added these getter method
def gettotal():
    return totalSlides
def getheaders():
    return headers
def getnextres():
    return next_res
def getbackres():
    return back_res
