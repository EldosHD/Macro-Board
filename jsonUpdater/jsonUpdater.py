import json
import argparse
import pathlib
import logging as log
import sys

hotKeys = [] # init array for the jsonfile

possibleHotkeys = ['explorerShortcut','copyToClipboard','holdMouseButton','autoClicker','sendInChat']

hotKeyName = ''
hotKeyType = ''
hotKeyContent = ''

givenJsonFile = pathlib.PureWindowsPath('hotKeys.json')


parser = argparse.ArgumentParser(description='Not working yet')
#options that are always available
parentParser = argparse.ArgumentParser('The Parrent parser', add_help=False)
parentParser.add_argument('--file',type=pathlib.Path,default=givenJsonFile ,help='Not implemented yet')
parentParser.add_argument('--no-color', help='Not implemented yet', default=True, action='store_false')
parentParser.add_argument('--version', help='prints out the programs version number',action='version' ,version='%(prog)s 0.1')

subparsers = parser.add_subparsers(description='valid subcommands NOTE: only use one of these', dest='subCommand')
subparsers.required = True

#create
create = subparsers.add_parser('create',parents=[parentParser], help='creates a Hotkey (Note: If you provide a label that already exists it will override that hotkey)',description='NOTE: add description')

create.add_argument('name', help='Not implemented yet')
create.add_argument('type', help='Not implemented yet',choices=possibleHotkeys)
create.add_argument('content', help='Not implemented yet')
create.add_argument('-o','--output', help='creates the given file and dumps the updated input file in there')
create.add_argument('-l','--list', help='lists all the possible hotkeys')

#merge
merge = subparsers.add_parser('merge', parents=[parentParser], help='merges the current hotkey file with a given one')
merge.add_argument('merge', type=pathlib.Path, help='Not implemented yet')

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
    print('create a hotkey')

def merge():
    print('not implemented yet')

def fix():
    print('COMING SOON')

def clean():
    print('not implemented yet')


def main():
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