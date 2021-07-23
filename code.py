######## LED GUI ########

from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

#Hardware
ledRed = LED(10)
ledGreen = LED(9)
ledBlue = LED(11)


#GUI DEFINITIONS#
win = Tk()
win.title("LED GUI")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = 'bold')



#Event functions#

#Turn off all LED's
def turnOffLeds():
    ledRed.off()
    ledGreen.off()
    ledBlue.off()
    
#Red
def ledRedFuntion():
    turnOffLeds()
    if ledRed.is_lit:
        ledRed.off()
        ledButtonRed["text"] = "Red LED on"
        
    else:
        ledRed.on()
        ledButtonRed["text"] = "Red LED off"
        
#Green   
def ledGreenFunction():
    turnOffLeds()
    if ledGreen.is_lit:
        ledGreen.off()
        ledButtonGreen["text"] = "Green LED on"
    else:
        ledGreen.on()
        ledButtonGreen["text"] = "Green LED off"
            
#Blue          
def ledBlueFunction():
    turnOffLeds()
    if ledBlue.is_lit:
        ledBlue.off()
        ledButtonBlue["text"] = "Blue LED on"

    else:
        ledBlue.on()
        ledButtonBlue["text"] = "Blue LED off"
      
      
#Close
def close():
    RPi.GPIO.cleanup()
    win.destroy()



## GUI Buttons ##
    
#Red
ledButtonRed = Button(win, text = 'Red LED on', font = myFont, command = ledRedFunction, bg = 'red', height = 1, width = 24)
ledButtonRed.grid(row = 0, column = 1)

#Green
ledButtonGreen = Button(win, text = 'Green LED on', font = myFont, command = ledGreenFunction, bg = 'green', height = 1, width = 24)
ledButtonGreen.grid(row = 1, column = 1)

#Blue
ledButtonBlue = Button(win, text = 'Blue LED on', font = myFont, command = ledBlueFunction, bg = 'blue', height = 1, width = 24)
ledButtonBlue.grid(row = 2, column = 1)


#Exit
exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'bisque2', height = 1, width = 6)
exitButton.grid(row = 3, column = 1)


win.protocol("WM_DELETE_WINDOW", close) #Exit cleanly

