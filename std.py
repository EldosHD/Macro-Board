import json
import subprocess

settings = {} # init settings

def loadSettings():
    '''
    Loads the settings from settings.json and puts it in the dictionary settings.
    '''
    try:
        with open('settings.json') as jsonFile:
            global settings
            settings = json.load(jsonFile)
        jsonFile.close()
        print('Settings loaded successfully')
    except BaseException as err:
        print('\n\nERROR: Settings failed to load. Check settings.json. The following exception was raised:')
        print(str(err) + '\n')


def openExplorerAt(path:str):
    '''
    Open an explorer window at the given path. The path has to be absolute.
    '''
    subprocess.Popen(r'explorer /e, "' + path + '"')

def holdMouseButton(button, mouse):
    '''
    Presses but not releases the provided mousebutton.
    '''
    mouse.press(button)

loadSettings()

print('finished loading std')