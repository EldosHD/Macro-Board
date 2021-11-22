import json
import argparse
from argparse import RawTextHelpFormatter
import pathlib
import logging as log
import sys
import textwrap

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


hotKeys = [] # init array for the jsonfile

possibleHotkeys = f'''R|The possible options are:
    explorerShortcut: Opens your file Explorer at a given position. (NOTE: Currently Widows only)
    copyToClipboard:  Copys a given string to your clipboard
    holdMouseButton:  Presses the given mouse button without releasing it
    autoClicker:      Starts clicking a given mouse button with a given intervall
    sendInChat:       Sends a given string in the in game chat. It supports different games'''

keyList = {'escape': '27', 'F1': '112', 'F2': '113', 'F3': '114', 'F4': '115', 'F5': '116', 'F6': '117', 'F7': '118', 'F8': '119', 'F9': '120', 'F10': '121', 'F11': '122', 'F12': '123', 'backslash': '220', '1': '49', '2': '50', '3': '51', '4': '52', '5': '53', '6': '54', '7': '55', '8': '56', '9': '57', '0': '48', 'leftbracket': '219', 'rightbracket': '221', 'backspace': '8', 'tab': '9', 'q': '81', 'w': '87', 'e': '69', 'r': '82', 't': '84', 'z': '90', 'u': '85', 'i': '73', 'o': '79', 'p': '80', 'semicolon': '186', 'equals': '187', 'enter': '13', 'capslock': '20', 'a': '65', 's': '83', 'd': '68', 'f': '70', 'g': '71', 'h': '72', 'j': '74', 'k': '75', 'l': '76', 'apo': '192', 'singlequote': '222', 'slash': '191', 'rShift': '16', 'y': '89', 'x': '88', 'c': '67', 'v': '86', 'b': '66', 'n': '78', 'm': '77', 'comma': '188', 'period': '190', 'minus': '189', 'rCtrl': '17', 'alt': '18', 'space': '32', 'insert': '45', 'home': '36', 'pageup': '33', 'delete': '46', 'end': '35', 'pagedown': '34', 'left': '37', 'up': '38', 'down': '40', 'right': '39', 'num0': '96', 'num1': '97', 'num2': '98', 'num3': '99', 'num4': '100', 'num5': '101', 'num6': '102', 'num7': '103', 'num8': '104', 'num9': '105', 'numDiv': '111', 'numMult': '106', 'numMinus': '109', 'numPlus': '107', 'numDelete': '110'}

hotKeyName = ''
hotKeyType = ''
hotKeyContent = ''

givenJsonFile = pathlib.PureWindowsPath('hotKeys.json')


parser = argparse.ArgumentParser(prog='PROG',description='Not working yet',epilog='This is a epilog. TODO: Write that')
#options that are always available
parentParser = argparse.ArgumentParser('The Parrent parser', add_help=False)
parentParser.add_argument('--file',type=pathlib.Path,default=givenJsonFile ,help='Not implemented yet')
parentParser.add_argument('--no-color', help='Not implemented yet', default=True, action='store_false')
parentParser.add_argument('--version', help='prints out the programs version number',action='version' ,version='%(prog)s 0.1')
parentParser.add_argument('-v','--verbosity',help='increases the verbosity',action='count',default=0)
parentParser.add_argument('-o','--output', help='creates the given file and dumps the updated input file in there')

subparsers = parser.add_subparsers(description='valid subcommands NOTE: only use one of these', dest='subCommand')
subparsers.required = True

#create
create = subparsers.add_parser('create',parents=[parentParser],help='creates a Hotkey (Note: If you provide a label that already exists it will override that hotkey)',description='NOTE: add description',formatter_class=SmartFormatter)

create.add_argument('name', help='use the name of a key. Use -l to list all possible keys')
create.add_argument('type', help=textwrap.dedent(possibleHotkeys))
create.add_argument('content', help='Not implemented yet')
create.add_argument('-l','--list', help='lists all the possible keys', default=False, action='store_true')

#merge
merge = subparsers.add_parser('merge', parents=[parentParser], help='merges the current hotkey file with a given one')
merge.add_argument('merge', type=pathlib.Path, help='Not implemented yet')
group = merge.add_mutually_exclusive_group()
group.add_argument('--force', default=False, action='store_true', help='overrites the old hotkey with the new one without asking (not implemented yet)')
group.add_argument('--keep', default=False, action='store_true', help='doesn´t overrite old hotkeys. Just adds the new ones (not implemented yet)')

#fix
fix = subparsers.add_parser('fix', help='COMING SOON',parents=[parentParser])
fix.add_argument('fix', help='Not implemented yet', action='store_true')
fix.add_argument('--ignore-names', help='not implemented yet', action='store_true')

#clean
clean = subparsers.add_parser('clean', parents=[parentParser], help='cleans the given json file of unnessesary/garbage code (like e.g. a function with name "aq" or lable "420") (Not Implemented Yet!)')
clean.add_argument('clean', help='Not implemented yet', action='store_true')



args = parser.parse_args()

def create():
    print(f'{color.RED}create not implemented yet{color.END}')
    if args.list == True:
        for key in keyList:
            print(f'Key: {key} -> Label: {keyList[key]}')

def merge():
    print('merge not implemented yet')

def fix():
    print('fix not implemented yet')

def clean():
    print('clean not implemented yet')


def main():
    global givenJsonFile    

    if args.file != 'hotKeys.json':
        givenJsonFile = args.file
    global hotKeys
    try:
        with open(givenJsonFile) as jsonFile:
            hotKeys = json.load(jsonFile)
        jsonFile.close()
        if args.verbosity >= 1:
            print(f'{color.GREEN}finished loading json file!{color.END}')
    except BaseException as err:
        print(f'\nThe given jsonFile ({givenJsonFile}) was not loaded correctly. By default this program looks for "hotKeys.json" in the current directory. You can specify another with --file [FILENAME]')
        sys.exit()

    if args.verbosity >= 2:
        print(f'Args: {args}')
        print(f'Json file: {str(hotKeys)}')

    if args.subCommand == 'create':
        create()
    elif args.subCommand == 'merge':
        merge()
    elif args.subCommand == 'fix':
        fix()
    elif args.subCommand == 'clean':
        clean()



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
    #aliases
    #ignore names: doesnt fix the name of the hotkey(e.g. if sb added a hotkey for key "q" but named it "minecraft" --> wont change name to "q")
    

# check if custom type applied --> no content needed

#print all msg with logging --> -v makes the log.info msg appear

#check if merge file and given file are identical