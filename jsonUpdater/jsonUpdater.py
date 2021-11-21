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

hotKeyName = ''
hotKeyType = ''
hotKeyContent = ''

givenJsonFile = pathlib.PureWindowsPath('hotKeys.json')


parser = argparse.ArgumentParser(description='Not working yet',epilog='This is a epilog. TODO: Write that')
#options that are always available
parentParser = argparse.ArgumentParser('The Parrent parser', add_help=False)
parentParser.add_argument('--file',type=pathlib.Path,default=givenJsonFile ,help='Not implemented yet')
parentParser.add_argument('--no-color', help='Not implemented yet', default=True, action='store_false')
parentParser.add_argument('--version', help='prints out the programs version number',action='version' ,version='%(prog)s 0.1')
parentParser.add_argument('-o','--output', help='creates the given file and dumps the updated input file in there')

subparsers = parser.add_subparsers(description='valid subcommands NOTE: only use one of these', dest='subCommand')
subparsers.required = True

#create
create = subparsers.add_parser('create',parents=[parentParser],help='creates a Hotkey (Note: If you provide a label that already exists it will override that hotkey)',description='NOTE: add description',formatter_class=SmartFormatter)

create.add_argument('name', help='Not implemented yet')
create.add_argument('type', help=textwrap.dedent(possibleHotkeys))
create.add_argument('content', help='Not implemented yet')
create.add_argument('-l','--list', help='lists all the possible hotkeys', default=False, action='store_true')

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

print(args)

def create():
    print('create not implemented yet')

def merge():
    print('merge not implemented yet')

def fix():
    print('fix not implemented yet')

def clean():
    print('clean not implemented yet')


def main():
    print(color.RED + 'TODO: Make path for both windows and linux' + color.END)
    global givenJsonFile    

    if args.file != 'hotKeys.json':
        givenJsonFile = args.file
    global hotKeys
    try:
        with open(givenJsonFile) as jsonFile:
            hotKeys = json.load(jsonFile)
        jsonFile.close()
        print('finished loading json file!')
    except BaseException as err:
        print(f'\nThe given jsonFile ({givenJsonFile}) was not loaded correctly. By default this program looks for "hotKeys.json" in the current directory. You can specify another with --file [FILENAME]')
        sys.exit()

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