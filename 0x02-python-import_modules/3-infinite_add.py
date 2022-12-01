#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv) - 1
    arg_sum = 0

    if arg_count > 1:
        for x in range(1, arg_count + 1):
            arg_sum += int(sys.argv[x])
        print(arg_sum)
    elif arg_count == 1:
        print(int(sys.argv[1]))
    else:
        print(0)
