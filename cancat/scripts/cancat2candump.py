# Command line entry point for cancat2candump

import sys
import argparse
import cancat.utils.convert


def main():
    argv = sys.argv[1:]

    parser = argparse.ArgumentParser(
            prog='cancat2candump',
            description='Utility to convert a CanCat session into a candump log')
    parser.add_argument('session', help='input CanCat session')
    parser.add_argument('output', help='output candump file')
    args = parser.parse_args(argv)

    cancat.utils.convert.cancat2candump(args.session, args.output)
