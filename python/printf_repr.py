import sys
from tokenize import tokenize, STRING

def main(filenames):
    exit_status = 0
    for filename in filenames:
        with open(filename, "rb") as f:
            for token in tokenize(f.readline):
                # TODO fstring too
                if token.type == STRING:
                    # TODO strip whole prefix
                    value = token.string[1:-1]
                    if '"%s"' in value or "'%s'" in value:
                        print(f"{filename}:{token.start[0]}:{token.start[1]}: Consider using %r for repr")
                        exit_status = 99

    sys.exit(exit_status)

if __name__ == "__main__":
    main(sys.argv[1:])
