import argparse


def filereader(path):
    with open(path) as f:
        return f.readlines()
    return []


def csv_counter(lines, sep):
    count = 0
    for l in lines:
        count += len(l.split(sep))
    return count


def csv_validator(lines, sep):
    n = -1
    for l in lines:
        n_ = len(l.split(sep))
        if n != -1:
            assert n_ == n
        n = n_


def main(path, sep, verbose):
    lines = filereader(path)
    csv_validator(lines, sep)
    print(f"element count: {csv_counter(lines, sep)}")
    if verbose:
        print(f"number of lines: {len(lines)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("-s", "--separator", default=";")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()
    main(args.path, args.separator, args.verbose)
