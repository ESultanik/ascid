import argparse
import sys

from .ascid import find_repeating_strings


def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser(description='ascid is the self-referential cycle identifier')

    parser.add_argument('FILE', nargs='?', type=argparse.FileType('r'), default=sys.stdin)

    args = parser.parse_args(argv[1:])

    try:
        s, offsets = find_repeating_strings(args.FILE.read())

        print("Found %i occurrences of the following string at offsets %s:" % (len(offsets), offsets))
        print(repr(s))
    except KeyboardInterrupt:
        pass
