# -*- coding: UTF-8 -*-
# Copyright (c) 2018, Xycart
# License: MIT License

# pylint:disable=C0103
# pylint:disable=C0303

from __future__ import unicode_literals

import sys, os     # standard modules
import errno
import argparse

from Pads2Xls import *

def runpyExcel2PadsMain():
    parser = argparse.ArgumentParser()
    # Create Arguments
    parser.add_argument(
        '--output',
        '-o',
        dest='output',
        help='The path for the output csv BOM file')
    parser.add_argument(
        '--input',
        '-i',
        dest='input',
        help='The path to the input schematic or netlist file')
    parser.add_argument(
        '--update', '-u', dest='update', help='Update the pricing')
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Show the verbose output to the terminal')

    args = parser.parse_args()

    prjname = args.input.split('/')[-1].split('.')[0].replace('pads-', '')
    print('Input file/directory is: {0}'.format(args.input))
    
    full_name = args.input + '.sch'
    xls_name  = args.output + prjname + '_BOM.xlsx'

    pads2xls=Pads2Xls()
    pads2xls.GenerateXls(full_name, xls_name, args.verbose)

    if args.verbose:
        print('Done')
        print('-' * 40)
        
        print('-' * 40)

# -i Examples/padslogic_test1.sch -o Examples/ -v
if __name__ == '__main__':
    runpyExcel2PadsMain()
