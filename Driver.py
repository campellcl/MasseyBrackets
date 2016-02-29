"""
Driver.py
    Driver for Massey Bracketology Program. Takes 1 command line argument:
        1. The name of the file to read.
@Author: Chris Campell
@Version: 1.0
@Date: 2/28/2016
"""
import sys
import traceback
import json
from pprint import pprint

def read_file():
    pass


def main(cmd_args):
    print(cmd_args)
    #input_file = None
    try:
        # input_file = open(cmd_args[1], "a")
        with open(cmd_args) as input_file:
            data = json.load(input_file)
        pprint(data)
    except Exception as error:
        traceback.print_tb(error.__traceback__)
        raise Exception





if __name__ == '__main__':
    main(sys.argv)