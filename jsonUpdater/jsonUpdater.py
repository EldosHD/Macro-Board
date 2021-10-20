import json
import argparse
import pathlib
import logging as log

log.info('test')

hotKeys = [] # init array for the jsonfile

hotKeyName = ''
hotKeyType = ''
hotKeyContent = ''

givenJsonFile = 'hotKeys.json'


parser = argparse.ArgumentParser(description='Not working yet')
#options that are always available
parentParser = argparse.ArgumentParser('The Parrent parser', add_help=False)
parentParser.add_argument('--file', help='Not implemented yet',type=pathlib.Path)
parentParser.add_argument('--no-color', help='Not implemented yet', default=True, action='store_false')
parentParser.add_argument('--version', help='prints out the programs version number',action='version' ,version='%(prog)s 0.1')

subparsers = parser.add_subparsers(description='valid subcommands NOTE: only use one of these', dest='subCommand')
subparsers.required = True

#create
create = subparsers.add_parser('create',aliases=['cr'] , parents=[parentParser], help='creates a Hotkey (Note: If you provide a label that already exists it will override that hotkey)',description='NOTE: add description')

create.add_argument('name', help='Not implemented yet')
create.add_argument('type', help='Not implemented yet')
create.add_argument('content', help='Not implemented yet')
create.add_argument('-o','--output', help='creates the given file and dumps the updated input file in there')

#merge
merge = subparsers.add_parser('merge', aliases=['mg'], parents=[parentParser], help='merges the current hotkey file with a given one')
merge.add_argument('merge', type=argparse.FileType('r'), help='Not implemented yet')

#fix
fix = subparsers.add_parser('fix', help='COMING SOON',parents=[parentParser])
fix.add_argument('fix', help='Not implemented yet', action='store_true')
fix.add_argument('--ignore-names', help='not implemented yet', action='store_true')

#clean
clean = subparsers.add_parser('clean', parents=[parentParser],aliases=['cl'] , help='cleans the given json file of unnessesary/garbage code (like e.g. a function with name "aq" or lable "420")')
clean.add_argument('clean', help='Not implemented yet', action='store_true')



args = parser.parse_args()

print(args)


def fix():
    print('COMING SOON')

def merge():
    print('not implemented yet')

def clean():
    print('not implemented yet')

def create():
    print('create a hotkey')

def main():
    if args.file.name != 'hotKeys.json':
        givenJsonFile = args.file.name
    global hotKeys
    try:
        with open(givenJsonFile) as jsonFile:
            hotKeys = json.load(jsonFile)
        jsonFile.close()
        print('finished loading json file!')
    except BaseException as err:
        print(f'\nThe given jsonFile ({givenJsonFile}) was not loaded correctly. By default this program looks for "hotKeys.json" in the current directory. You can specify anothe with --file [FILENAME]')

    print(f'Json file: {str(hotKeys)}')


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