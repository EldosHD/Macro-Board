'''
The standard libary for the 2nd keyboard. There is a subfolder called "stdExtensions". All other functions that I (or others) wrote can be found there.
I am not including the other functions for one simple reason. I am not sure how big this program will grow. By not including all functions in one script the user can decide which features they need.
That way this script wont take up to much space. And less code means less points of failure.
'''
import json
import subprocess
import pynput


settings = {} # init settings

mouse = pynput.mouse.Controller()

keyboard = pynput.keyboard.Controller()


def loadSettings():
    '''
    Loads the settings from settings.json and puts it in a dictionary called settings.
    '''
    try:
        with open('settings.json') as jsonFile:
            global settings
            settings = json.load(jsonFile)
        jsonFile.close()
        print('finished loading Settings')
    except BaseException as err:
        print('\n\nERROR: Settings failed to load. Check settings.json. The following exception was raised:')
        print(str(err) + '\n')

def sendInChat(strToSend: str, mode='std'):
    '''
    Types a given string or sends it in the in game chat. Since different games uses different buttons for the game chat, there are multiple modes for this function.
    If you dont specify the mode it will default to "std" mode.
    Modes:

    +-----------+----------------------------------------------------------+
    |   Mode    |                     Description                          |
    +-----------+----------------------------------------------------------+
    | std       | Just types the given string.                             |
    | lol       | Opens the Chat by tapping Enter, types the given string  |
    |           | afterwards and presses Enter again to send the string.   |
    | minecraft | Same as "lol", but it opens the chat by tapping t.       |
    +-----------+----------------------------------------------------------+    
    '''
    if mode == 'std':
        keyboard.type(strToSend)
    elif mode == 'lol':
        keyboard.tap(pynput.keyboard.Key.enter)
        keyboard.type(strToSend)
        keyboard.tap(pynput.keyboard.Key.enter)
    elif mode == 'minecraft':
        keyboard.tap(pynput.keyboard.KeyCode(char='t'))
        keyboard.type(strToSend)
        keyboard.tap(pynput.keyboard.Key.enter)


def openExplorerAt(path:str):
    '''
    Open an explorer window at the given path. The path has to be absolute.
    '''
    subprocess.Popen(r'explorer /e, "' + path + '"')

def holdMouseButton(button: str):
    '''
    Presses but not releases the provided mousebutton.
    Use "left" for the left mousebutton and "right" for the right mousebutton.
    '''
    if button == 'left':
        mouse.press(pynput.mouse.Button.left)
    elif button == 'right':
        mouse.press(pynput.mouse.Button.right)
    else:
        print('ERROR: wrong button argument was provided.')
        print('Use "left" for the left mousebutton and "right" for the right mousebutton.')

loadSettings()

print('finished loading ' + __name__)