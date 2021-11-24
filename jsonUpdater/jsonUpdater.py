import json
import argparse
from os import name
import pathlib
import sys
import textwrap
import os.path

class SmartFormatter(argparse.HelpFormatter):

    def _split_lines(self, text, width):
        if text.startswith('R|'):
            return text[2:].splitlines()  
        # this is the RawTextHelpFormatter._split_lines
        return argparse.HelpFormatter._split_lines(self, text, width)

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


hotKeys = {} # init dict for the jsonfile

possibleHotkeys = f'''R|The possible options are:
    explorerShortcut: Opens your file Explorer at a given position. (NOTE: Currently Widows only)
    copyToClipboard:  Copys a given string to your clipboard
    holdMouseButton:  Presses the given mouse button without releasing it
    autoClicker:      Starts clicking a given mouse button with a given intervall
    sendInChat:       Sends a given string in the in game chat. It supports different games'''

possibleContent = f'''R|You can use the following contents:
    for explorerShortcut: specify a path to the directory you want your explorer to open at
    for copyToClipboard:  specify the string you want to copy to your clipboard
    for holdMouseButton:  specify the button you want to hold down [left | right]
    for autoClicker:      specify the button you want to autoclick [left | right]
    for sendInChat:       specify the string you want to send in your game chat. If you want to change the mode, use "--mode" (see below)
'''

possibleModes = '''R|Only required if you are using "sendInChat". It defaults to "std"
+-----------+----------------------------------------------------------+
|   Mode    |                     Description                          |
+-----------+----------------------------------------------------------+
| std       | Just types the given string.                             |
| lol       | Opens the Chat by tapping Enter, types the given string  |
|           | afterwards and presses Enter again to send the string.   |
| minecraft | Same as "lol", but it opens the chat by tapping t.       |
+-----------+----------------------------------------------------------+
'''


keyList = {'escape': '27', 'F1': '112', 'F2': '113', 'F3': '114', 'F4': '115', 'F5': '116', 'F6': '117', 'F7': '118', 'F8': '119', 'F9': '120', 'F10': '121', 'F11': '122', 'F12': '123', 'backslash': '220', '1': '49', '2': '50', '3': '51', '4': '52', '5': '53', '6': '54', '7': '55', '8': '56', '9': '57', '0': '48', 'leftbracket': '219', 'rightbracket': '221', 'backspace': '8', 'tab': '9', 'q': '81', 'w': '87', 'e': '69', 'r': '82', 't': '84', 'z': '90', 'u': '85', 'i': '73', 'o': '79', 'p': '80', 'semicolon': '186', 'equals': '187', 'enter': '13', 'capslock': '20', 'a': '65', 's': '83', 'd': '68', 'f': '70', 'g': '71', 'h': '72', 'j': '74', 'k': '75', 'l': '76', 'apo': '192', 'singlequote': '222', 'slash': '191', 'rShift': '16', 'y': '89', 'x': '88', 'c': '67', 'v': '86', 'b': '66', 'n': '78', 'm': '77', 'comma': '188', 'period': '190', 'minus': '189', 'rCtrl': '17', 'alt': '18', 'space': '32', 'insert': '45', 'home': '36', 'pageup': '33', 'delete': '46', 'end': '35', 'pagedown': '34', 'left': '37', 'up': '38', 'down': '40', 'right': '39', 'num0': '96', 'num1': '97', 'num2': '98', 'num3': '99', 'num4': '100', 'num5': '101', 'num6': '102', 'num7': '103', 'num8': '104', 'num9': '105', 'numDiv': '111', 'numMult': '106', 'numMinus': '109', 'numPlus': '107', 'numDelete': '110'}

givenJsonFile = pathlib.PureWindowsPath('hotKeys.json')


parser = argparse.ArgumentParser(prog='PROG',description='I am to lazy to write the actual script. I am still writing the CLI *sight*',epilog='This is a epilog. TODO: Write that')
#options that are always available
parentParser = argparse.ArgumentParser('The Parrent parser', add_help=False)
parentParser.add_argument('--no-color', help='stops the program from using ANSI color codes in the output', default=True, action='store_false')
parentParser.add_argument('-V','--version', help='prints out the programs version number',action='version' ,version='0.1')
parentParser.add_argument('-v','--verbosity',help='increases the verbosity. The current max level is 2. The default level is 0',action='count',default=0)

fileUseParser = argparse.ArgumentParser('The parser for create, merge, fix and clean', add_help=False)
fileUseParser.add_argument('-o','--output', help='creates the given file and dumps the updated input file in there')
fileUseParser.add_argument('--json-no-exit', help='wont exit, if the JSON file is not loaded correctly. Sets "givenJsonFile" to "ERROR"', action='store_true')
fileUseParser.add_argument('--file',type=pathlib.Path,default=givenJsonFile ,help='changes the used json file to a given one')

subparsers = parser.add_subparsers(description='valid subcommands NOTE: only use one of these', dest='subCommand')
subparsers.required = True

#create
create = subparsers.add_parser('create',parents=[parentParser, fileUseParser],help='creates a Hotkey (Note: If you provide a label that already exists it will override that hotkey)',description='NOTE: add description',formatter_class=SmartFormatter)

create.add_argument('name', help='use the name of a key. Use "PROG list" to list all possible keys')
create.add_argument('type', help=textwrap.dedent(possibleHotkeys))
create.add_argument('content', help=textwrap.dedent(possibleContent))
create.add_argument('--label', help='specify a label', default='noLabel')
create.add_argument('--force', help='force create the hotkey. Even if the type or label is not found')
create.add_argument('-m','--mode', help=textwrap.dedent(possibleModes), default='std')

#merge
merge = subparsers.add_parser('merge', parents=[parentParser,fileUseParser], help='merges the current hotkey file with a given one')
merge.add_argument('merge', type=pathlib.Path, help='Not implemented yet')
forceKeepGroup = merge.add_mutually_exclusive_group()
forceKeepGroup.add_argument('--force', default=False, action='store_true', help='overrites the old hotkey with the new one without asking (not implemented yet)')
forceKeepGroup.add_argument('--keep', default=False, action='store_true', help='doesn´t overrite old hotkeys. Just adds the new ones (not implemented yet)')

#fix
fix = subparsers.add_parser('fix', help='COMING SOON',parents=[parentParser, fileUseParser])
fix.add_argument('fix', help='Not implemented yet', action='store_true')
fix.add_argument('--ignore-names', help='not implemented yet', action='store_true')

#clean
clean = subparsers.add_parser('clean', parents=[parentParser, fileUseParser], help='cleans the given json file of unnessesary/garbage code (like e.g. a function with name "aq" or lable "420") (Not Implemented Yet!)')
clean.add_argument('clean', help='Not implemented yet', action='store_true')

#list
hotKeyList = subparsers.add_parser('list', parents=[parentParser],help='lists all the possible keys')
hotKeyList.add_argument('list', default=False, action='store_true', help='lists all the possible keys')

demo = subparsers.add_parser('demo', help='creates a demo json file', parents=[parentParser])
demo.add_argument('demo',default=False, action='store_true', help='creates a demo json file')
demo.add_argument('--remove', default=False, action='store_true', help='removes the json file, if it already exsists')


# print help when no args provided
if len(sys.argv) < 2:  
    parser.print_help()
    sys.exit()

args = parser.parse_args()
#--------------Functions------------

def loadJsonFile():
    global givenJsonFile
    global hotKeys

    # create new file if file doesnt exsists
    if os.path.isfile(givenJsonFile):
        #file exsists
        if args.verbosity >= 1:
            # file exsists
            print(f'{color.GREEN}The json file: "{givenJsonFile}" was found!{color.END}')
    else:
        # file does not exsist
        if args.verbosity >= 1:
            print(f'{color.RED}The json file: "{givenJsonFile}" was not found!{color.END}')
            print(f'{color.YELLOW}Creating json File: {givenJsonFile}{color.END}')
        f = open(givenJsonFile, 'w')
        f.close()
    

    try:
        with open(givenJsonFile) as jsonFile:
            hotKeys = json.load(jsonFile)
        jsonFile.close()
        if args.verbosity >= 1:
            print(f'{color.GREEN}finished loading json file!{color.END}')
    except BaseException as err:
        if args.json_no_exit == False:
            print(f'\n{color.RED}The given jsonFile ({givenJsonFile}) was not loaded correctly. By default this program looks for "hotKeys.json" in the current directory. You can specify another with --file [FILENAME]\nERROR: {err}{color.END}\n')
            sys.exit()
        else:
            givenJsonFile = "ERROR"

def createSubcommand():
    loadJsonFile()
    global givenJsonFile
    # create a label based on the name
    label = args.label
    newHotKey = {}
    if args.type == 'sendInChat':
        newHotKey = {'name':args.name, 'label':label,'type':args.type ,'content':args.content, 'mode':args.mode}
    elif args.type == 'explorerShortcut':
        newHotKey = {'name':args.name, 'label':label,'type':args.type ,'path':args.content}
    elif args.type =='holdMouseButton' or args.type == 'autoClicker':
        if args.content == 'left' or args.content == 'right':
            newHotKey = {'name':args.name, 'label':label,'type':args.type ,'button':args.content}
        else:
            print(f'{color.RED}You specified {args.content} as content. You have to use "left" or "right" as content{color.END}')
            sys.exit()
    else:
        newHotKey = {'name':args.name, 'label':label,'type':args.type ,'content':args.content}

    hotKeys.append(newHotKey)
    if args.verbosity >= 1:
        print(f'{color.YELLOW}writing to file!{color.END}')
    elif args.verbosity >= 2:
        print(f'{color.YELLOW}new hotKeys content: {hotKeys}{color.END}')

    with open(givenJsonFile, 'w') as jf:
        json.dump(hotKeys, jf)


def mergeSubcommand():
    print('merge not implemented yet')

def fixSubcommand():
    print('fix not implemented yet')

def cleanSubcommand():
    print('clean not implemented yet')

def listSubcommand():
    # List all keys
    for key in keyList:
        print(f'Key: {key} -> Label: {keyList[key]}')


def main():
    if args.no_color == False:
        color.PURPLE = ''
        color.CYAN = ''
        color.DARKCYAN = ''
        color.BLUE = ''
        color.GREEN = ''
        color.YELLOW = ''
        color.RED = ''
        color.BOLD = ''
        color.UNDERLINE = ''
        color.END = ''

    global givenJsonFile    

    try:
        if args.file != 'hotKeys.json':
            givenJsonFile = args.file
    except:
        pass

    if args.verbosity >= 2:
        print(f'{color.PURPLE}Args: {args}{color.END}')

    if args.subCommand == 'create':
        createSubcommand()
    elif args.subCommand == 'merge':
        mergeSubcommand()
    elif args.subCommand == 'fix':
        fixSubcommand()
    elif args.subCommand == 'clean':
        cleanSubcommand()
    elif args.subCommand == 'list':
        listSubcommand()



if __name__ == '__main__':
    main()



#read in json file
#if hotkey exists:
    #update with given argument
#else:
    #create with given argument


#arguments to implement
    #create
    #merge
    #fix
    #clean
    #no-color
    #quiet
    #verbosity
    #ignore names: doesnt fix the name of the hotkey(e.g. if sb added a hotkey for key "q" but named it "minecraft" --> wont change name to "q")
    

# check if custom type applied --> no content needed

#print all msg with logging --> -v makes the log.info msg appear

#check if merge file and given file are identical


#------------------------------
# bugs
# "PROG create" doesnt show the usage
#  the create feature doesnt create o label based on the name yet