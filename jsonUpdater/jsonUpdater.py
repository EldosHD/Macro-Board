import json
import argparse

#read in json file
#if hotkey exists:
    #update with given argument
#else:
    #create with given argument


#list of arguments:
#required:      the program shoudlnt start when its called without args, so it doesnt get called accidentilly
    #name ==> creates label automaticly
    #type
    #required content for type

#optional:
    #--no-color
    #--merge: merges a given json file with the current one?
    #--fix: repairs the current hotkey file
    #--clean: removes unnessesary garbage code (like e.g. a function with name "aq" or lable "420")
    #--file: uses a given json file instead of hotKeys.json (e.g. for --fix)

