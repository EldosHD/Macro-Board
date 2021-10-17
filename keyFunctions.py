from os import set_inheritable
import subprocess
import pyperclip
from pynput.mouse import Button,Controller
import json
import time
import threading

mouse = Controller() #init mouse object

settings = {} #init settings dict

leftPressed = False
rightPressed = False

leftAutoClicker = False
rightAutoclicker = False

def openExplorerAt(path:str):
    subprocess.Popen(r'explorer /e, "' + path + '"')

def loadSettings():
    #load settings from settings.json in the dict: settings
    global settings
    with open('settings.json') as jsonFile:
        settings = json.load(jsonFile)


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.programRunning = True

    def startClicking(self):
        self.running = True

    def stopClicking(self):
        self.running = False

    def exit(self):
        self.stopClicking()
        self.programRunning = False

    def run(self):
        while self.programRunning:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


def autoclicker(clickThread):
    if clickThread.running:
        clickThread.stopClicking()
    else:
        clickThread.startClicking()



#----------Start of keyfunctions----------
#upper row
def functionEscape():
    pass

def functionF1():
    pass

def functionF2():
    pass

def functionF3():
    pass

def functionF4():
    pass

def functionF5():
    pass

def functionF6():
    pass

def functionF7():
    pass

def functionF8():
    pass

def functionF9():
    pass

def functionF10():
    pass

def functionF11():
    pass

def functionF12():
    pass

#second row
def functionBackslash():
    pass

def function1():
    pass

def function2():
    pass

def function3():
    pass

def function4():
    pass

def function5():
    pass

def function6():
    pass

def function7():
    pass

def function8():
    pass

def function9():
    pass

def function0():
    pass

def functionRightbracket():
    pass

def functionLeftbracket():
    pass

def functionBackspace():
    pass

#thrid row
def functionTab():
    pass

def functionQ():
    openExplorerAt(r'C:\Users\Valen\AppData\Roaming\.minecraft')

def functionW():
    openExplorerAt(r'C:\Users\Valen\AppData\Roaming\.minecraft\mods')

def functionE():
    openExplorerAt(r'C:\Users\Valen\OneDrive\Desktop\HotSwap Mods')

def functionR():
    pyperclip.copy('1495774276')

def functionT():
    pass

def functionZ():
    pass

def functionU():
    pass

def functionI():
    pass

def functionO():
    pass

def functionP():
    pass

def functionSemicolon():
    pass

def functionEquals():
    pass

def funtionEnter():
    pass

#fourth row
def functionCapslock():
    pass

def functionA():
    openExplorerAt(r'C:\Users\Valen\Downloads')

def functionS():
    openExplorerAt('C:\\')

def functionD():
    openExplorerAt('D:\\')    

def functionF():
    openExplorerAt(r'C:\Users\Valen\OneDrive')

def functionG():
    pass

def functionH():
    pass

def functionJ():
    pass

def functionK():
    pass

def functionL():
    pass

def functionApo(): #ö
    pass

def functionSinglequote():
    pass

def functionSlash():
    pass

#fith row
def functionRShift():
    pass

def functionY():
    openExplorerAt(r'C:\Users\Valen\OneDrive\Uni')

def functionX():
    openExplorerAt(r'C:\Users\Valen\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')

def functionC():
    openExplorerAt(r'C:\2nd-keyboard')

def functionV():
    openExplorerAt(r'C:\Users\Valen\OneDrive\Dokumente')

def functionB():
    pass

def functionN():
    pass

def functionM():
    pass

def functionComma():
    pass

def functionPeriod():
    pass

def functionMinus():
    pass

#last row
def functionRCtrl():
    pass

def functionAlt():
    pass

def functionSpace():
    pass

#block above arrow keys
def functionInsert():
    pass

def functionHome():
    pass

def functionPageup():
    pass

def functionDelete():
    pass

def functionEnd():
    pass

def functionPagedown():
    pass

#arrowkeys
def functionUp():
    pass

def functionLeft():
    pass

def functionRight():
    pass

def functionDown():
    pass

#numblock
def functionNum0():
    pass

def functionNum1():
    pass

def functionNum2():
    pass

def functionNum3():
    pass

def functionNum4():
    mouse.press(Button.right)

def functionNum5():
    #add autoclick rightclick feature
    pass

def functionNum6():
    pass

def functionNum7():
    mouse.press(Button.left)

def functionNum8():
    #add autoclick leftclick feature
    #use 2 seperate threads for each clicker that get created at the start of the program
    delay = 0.5
    button = Button.left
    clickThread = ClickMouse(delay, button)
    clickThread.start()
    autoclicker(clickThread)


def functionNum9():
    pass

def functionNumDelete():
    pass

def functionNumPlus():
    pass

def functionNumMinus():
    pass

def functionNumMult():
    pass

def functionNumDiv():
    pass

# input('Turn on')
# functionNum8()
# input('turn off')
# functionNum8()