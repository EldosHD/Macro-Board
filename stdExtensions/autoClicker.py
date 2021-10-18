import threading
import time
import std
from pynput.mouse import Controller,Button

mouseClicker = Controller() #creating mouse object

class ClickMouse(threading.Thread):
    '''
    Creates a thread that can start and stop clicking.
    '''
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False
    
    def changeInterval(self, newDelay):
        self.delay = newDelay

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouseClicker.click(self.button)
                print("click: " + str(self.button))
                time.sleep(self.delay)
            time.sleep(0.1)

def autoClickerFunction(button: str):
    '''
    Use "left" as an argument to start the leftclick autoclicker and "right" for the rightclick autoclicker 
    '''
    std.loadSettings()
    intervalName = ''
    if button == 'left':
        clickThread = leftClickThread
        intervalName = 'leftDelay'
    elif button == 'right':
        clickThread = rightClickThread
        intervalName = 'rightDelay'
    else:
        print('Wrong button was provided. Use "left" or "right"!\n')
    clickThread.changeInterval(std.settings[intervalName])
    if clickThread.running:
        print(f'starting to {button}click!')
        clickThread.stop_clicking()
    else:
        clickThread.start_clicking()
        print(f'Stopped {button}clicking!')


leftClickThread = ClickMouse(std.settings["leftDelay"], Button.left)
rightClickThread = ClickMouse(std.settings["rightDelay"], Button.right)
leftClickThread.start()
rightClickThread.start()

print('finished loading ' + __name__)