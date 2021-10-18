import std
import stdExtensions.autoClicker

import pyperclip
from pynput.mouse import Button,Controller
import time
import threading

mouse = Controller() #init mouse object

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
    std.openExplorerAt(r'C:\Users\Valen\AppData\Roaming\.minecraft')

def functionW():
    std.openExplorerAt(r'C:\Users\Valen\AppData\Roaming\.minecraft\mods')

def functionE():
    std.openExplorerAt(r'C:\Users\Valen\OneDrive\Desktop\HotSwap Mods')

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
    std.openExplorerAt(r'C:\Users\Valen\Downloads')

def functionS():
    std.openExplorerAt('C:\\')

def functionD():
    std.openExplorerAt('D:\\')    

def functionF():
    std.openExplorerAt(r'C:\Users\Valen\OneDrive')

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
    std.openExplorerAt(r'C:\Users\Valen\OneDrive\Uni')

def functionX():
    std.openExplorerAt(r'C:\Users\Valen\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')

def functionC():
    std.openExplorerAt(r'C:\2nd-keyboard')

def functionV():
    std.openExplorerAt(r'C:\Users\Valen\OneDrive\Dokumente')

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
    #just presses the right mouse button and holds it down
    mouse.press(Button.right)

def functionNum5():
    #autoclicker for rightclick
    stdExtensions.autoClicker.autoClickerFunction('right')

def functionNum6():
    pass

def functionNum7():
    #just presses the left mouse button and holds it down
    mouse.press(Button.left)

def functionNum8():
    #autoclicker for leftclick
    stdExtensions.autoClicker.autoClickerFunction('left')
    
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

print('finished loading keyFunctions')