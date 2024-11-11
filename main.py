import sys


def filereader(path):
    with open(path) as f:
        return f.readlines()
    return None


def csv_counter(lines):
    count = 0
    for l in lines:
        count += len(l.split(";"))
    return count


def main():
    lines = filereader(sys.argv[1])
    print(f"element count: {csv_counter(lines)}")


if __name__ == "__main__":
    main()
