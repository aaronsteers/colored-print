"""CLI execution."""

import argparse
from os import environ

from . import colored_print

def parse_args():
    parser = argparse.ArgumentParser(
        description='Process some integers.'
    )
    parser.add_argument(
        '--color',
        default='success',
        help='the format string for the text to print'
    )
    # parser.add_argument(
    #     '--format',
    #     default='text',
    #     help='either "json" or "text"'
    # )
    parser.add_argument(
        '--vars',
        help='one or more environment variable names to print along with their values',
        nargs="*"
    )
    parser.add_argument(
        '--text',
        help='the text to print'
    )
    parser.add_argument(
        '--sum', dest='accumulate', action='store_const',
        const=sum, default=max,
        help='sum the integers (default: find the max)'
    )
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    print_obj = colored_print.ColoredPrint()

    print_fn = print_obj.info
    if args["color"] == "success":
        print_fn = print_obj.success

    for env_var in args["vars"]:
        if env_var not in environ:
            raise ValueError(f"'{env_var}' was not present in environment variables.")
        
        print_fn(f"{emv_var}={environ[env_var]}\n")

    for text_str in args["text"]:
        print_fn(f"{text_str}\n")


if __name__ == "__main__":
    main()

