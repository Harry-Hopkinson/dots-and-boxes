import os

def tryStatement():
    try:
        os.environ["DISPLAY"]
    except:
        os.environ["SDL_VIDEODRIVER"] = "dummy"
