#!/usr/bin/env python3

import re
import os
import sys
import argparse

parser = argparse.ArgumentParser(description='Strips special characters and keeps only alphabetical letters.')
parser.add_argument('-s', help='string containing special characters', dest='string', type=str)
parser.add_argument('-f', help='file containing special characters', dest='file')
args = parser.parse_args()

cwd = os.getcwd()
stringInput = args.string
fileInput = args.file

def main():
    print('''
   _____      _      _____ _                              __   ___  
  / ____|    | |    / ____| |                            /_ | / _ \ 
 | |  __  ___| |_  | |    | |__   __ _ _ __ ___  __   __  | || | | |
 | | |_ |/ _ \ __| | |    | '_ \ / _` | '__/ __| \ \ / /  | || | | |
 | |__| |  __/ |_  | |____| | | | (_| | |  \__ \  \ V /   | || |_| |
  \_____|\___|\__|  \_____|_| |_|\__,_|_|  |___/   \_/    |_(_)___/ 
    ''')
    if stringInput:
        stringToChar(stringInput)
    elif fileInput:
        fileToChar(fileInput)

def stringToChar(input):
    output = " ".join(re.findall("[a-zA-Z]+", input))
    print(output)
    sys.exit(0)

def fileToChar(input):
    f = open(cwd + "/" + input, "r")
    content = str(f.read())
    output = " ".join(re.findall("[a-zA-Z]+", content))
    f.close()
    print(output)
    sys.exit(0)

main()