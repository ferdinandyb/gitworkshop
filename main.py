import sys


def filereader(path):
    with open(path) as f:
        return f.readlines()
    return None


def main():
    lines = filereader(sys.argv[1])
    print(lines)


if __name__ == "__main__":
    main()
