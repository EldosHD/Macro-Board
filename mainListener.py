import std
import stdExtensions.autoClicker

import json
from pynput import keyboard, mouse
import subprocess
import pyperclip
import sys


keyList = ['functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionBackspace()', 'functionTab()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionEnter()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionRshift()', 'functionRctrl()', 'functionAlt()', 'functionPlaceholder()', 'functionCapslock()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionEscape()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionSpace()', 'functionPageup()', 'functionPagedown()', 'functionEnd()', 'functionHome()', 'functionLeft()', 'functionUp()', 'functionRight()', 'functionDown()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionInsert()', 'functionDelete()', 'functionPlaceholder()', 'function0()', 'function1()', 'function2()', 'function3()', 'function4()', 'function5()', 'function6()', 'function7()', 'function8()', 'function9()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionA()', 'functionB()', 'functionC()', 'functionD()', 'functionE()', 'functionF()', 'functionG()', 'functionH()', 'functionI()', 'functionJ()', 'functionK()', 'functionL()', 'functionM()', 'functionN()', 'functionO()', 'functionP()', 'functionQ()', 'functionR()', 'functionS()', 'functionT()', 'functionU()', 'functionV()', 'functionW()', 'functionX()', 'functionY()', 'functionZ()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionNum0()', 'functionNum1()', 'functionNum2()', 'functionNum3()', 'functionNum4()', 'functionNum5()', 'functionNum6()', 'functionNum7()', 'functionNum8()', 'functionNum9()', 'functionNummult()', 'functionNumplus()', 'functionPlaceholder()', 'functionNumminus()', 'functionNumdelete()', 'functionNumdiv()', 'functionF1()', 'functionF2()', 'functionF3()', 'functionF4()', 'functionF5()', 'functionF6()', 'functionF7()', 'functionF8()', 'functionF9()', 'functionF10()', 'functionF11()', 'functionF12()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionNumlock()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionSemicolon()', 'functionEquals()', 'functionComma()', 'functionMinus()', 'functionPeriod()', 'functionSlash()', 'functionApo()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionPlaceholder()', 'functionLeftbracket()', 'functionBackslash()', 'functionRightbracket()', 'functionSinglequote()']

# first path: "path to LuaMacros.exe" second path: path to secondKeyboard-luaMacros-script
try:
    lua = subprocess.Popen(r'"C:\Program Files (x86)\luaMacros\LuaMacros.exe" C:\Users\Valen\Github\Macro-Board\SECOND_KEYBOARD_script_for_LUA_MACROS.lua -r')
except:
    print('something went wrong with opening luaMacros!')

hotKeys = [] # init hotkey list

try:
    with open('hotKeys.json') as jsonFile:
        hotKeys = json.load(jsonFile)
    jsonFile.close()
    print('finished loading hotkeys')
except BaseException as err:
    print('\nERROR: Hotkeys failed to load. Check hotKeys.json. The following exception was raised:')
    print('\n' + str(err) + '\n')

def checkKey(key):
    hotkeyFound = False
    
    
    for dic in hotKeys:
        #checks if pressed key is an assigned hotkey
        
        #checks if label and type exsist
        if ('label' or 'type') not in dic:        
            print('WARNING: Hotkey with value: ' + str(dic) + ' was not assigned properly.\nIt needs a "label" and a "type".')
            continue

        if dic['label'] == str(key):

            #checks which type of hotkey the pressed key is
            if dic["type"] == 'explorerShortcut':
                std.openExplorerAt(dic['path'])
            elif dic['type'] == 'copyToClipboard':
                pyperclip.copy(dic['content'])
            elif dic['type'] == 'holdMouseButton':
                if dic['button'] == 'left':
                    std.holdMouseButton('left')
                elif dic['button'] == 'right':
                    std.holdMouseButton('right')
            elif dic['type'] == 'autoClicker':
                if dic['button'] == 'left':
                    stdExtensions.autoClicker.autoClickerFunction('left')
                elif dic['button'] == 'right':
                    stdExtensions.autoClicker.autoClickerFunction('right')
                else:
                    print('ERROR: wrong button argument was provided.')
                    print('Use "left" for the left mousebutton and "right" for the right mousebutton.')
            elif dic['type'] == 'sendInChat':
                std.sendInChat(dic['content'],dic['mode'])
            else:
                print('ERROR: Hotkey ' + dic['label'] + 'was not assigned a type')
            
            hotkeyFound = True
    if not hotkeyFound:
        print('ERROR: Hotkey not assigned. Did you add the hotkey to hotKeys.json?')
    

def on_press(key):
    if key == keyboard.Key.scroll_lock: 
        print('exiting...')
        lua.kill()
        stdExtensions.autoClicker.leftClickThread.exit()
        stdExtensions.autoClicker.rightClickThread.exit()
        return False
    elif key == keyboard.Key.f19:
        with open('keypressed.txt','r') as k:
            pressedKey = k.read()
            checkKey(int(pressedKey))

def on_release(key):
    pass

def main():
    # add debug mode (with argparser)
    print('starting listener...')
    listener = keyboard.Listener(on_press=on_press,on_release=on_release)
    listener.start()

if __name__ == '__main__':
    main()