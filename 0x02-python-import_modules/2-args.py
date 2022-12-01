#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    index = 1
    args_count = len(argv)-1

    if args_count == 1:
        print("{} argument:".format(args_count))
        print("{}: {}".format(index, argv[args_count]))
    elif args_count == 0:
        print("{} arguments.".format(args_count))
    else:
        print("{} arguments:".format(args_count))
        while index <= args_count:
            print("{}: {}".format(index, argv[index]))
            index += 1
