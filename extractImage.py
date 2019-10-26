import sys
import argparse
import subprocess


def checkArgument():

    parser = argparse.ArgumentParser()
    parser.add_argument('--sourcefile', help="File location of archived file")
    parser.add_argument(
        '--dest',
        help="file system location where unarchived files will be written to.")
    return parser


def ExtractFiles(args):
    subprocess.call("./extractImages.sh " + args.sourcefile + " " + args.dest,
                    shell=True)


def main():

    argparser = checkArgument()
    args = argparser.parse_args()

    if (args.sourcefile == None or args.dest == None):
        argparser.error("\nToo few arguments.")
    else:
        ExtractFiles(args)


if __name__ == '__main__':
    main()