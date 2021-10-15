from pynput import keyboard

def checkKey(key):
    #check all keys on the 2nd keyboard
    print(key)


def on_press(key):
    if key == keyboard.Key.scroll_lock: #checks if the key is the scroll lock
        return False
    elif key == keyboard.Key.f19:
        with open('keypressed.txt','rt') as k:
            pressedKey = k.read()
            checkKey(pressedKey)

def on_release(key):
    pass

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

