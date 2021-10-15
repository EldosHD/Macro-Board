from pynput import keyboard
import keyFunctions

keyList = {}


with open('keyList.txt','rt') as l:
        keyArray = [line.replace('\n','') for line in l.readlines()]

for element in keyArray:
    keyList[element] = 'function' + element.lower().capitalize() + '()'


def checkKey(key):
    #check all keys on the 2nd keyboard
    eval('keyFunctions.' + keyList[key])


def on_press(key):
    if key == keyboard.Key.scroll_lock: #checks if the key is the scroll lock
        return False
    elif key == keyboard.Key.f19:
        with open('keypressed.txt','rt') as k:
            pressedKey = k.read()
            checkKey(pressedKey)

def on_release(key):
    pass

print(settings)

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

