import RPi.GPIO as G
import time

G.setwarnings(False)

G.setmode(G.BOARD)
G.setup(7, G.OUT)
G.setup(29, G.OUT)
G.setup(15, G.OUT)

G.setwarnings(False)

def red_light():
    for a in range(5):
        G.output(7, True)
        time.sleep(.5)
        G.output(7, False)
        time.sleep(.5)
    

def green_light():
    for b in range(5):
     
        G.output(15, True)
        time.sleep(.5)
        G.output(15, False)
        time.sleep(.5)

def yellow_light():
    G.output(29, True)
    time.sleep(3)
    G.output(29, False)


while 1 < 100:
    red_light()
    yellow_light()
    green_light()





G.cleanup()
