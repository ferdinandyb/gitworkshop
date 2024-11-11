import argparse


def filereader(path):
    with open(path) as f:
        return f.readlines()
    return None


def csv_counter(lines):
    count = 0
    for l in lines:
        count += len(l.split(";"))
    return count


def csv_validator(lines):
    n = -1
    for l in lines:
        n_ = len(l.split(";"))
        if n != -1:
            assert n_ == n
        n = n_


def main(path):
    lines = filereader(path)
    csv_validator(lines)
    print(f"element count: {csv_counter(lines)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    main(args.path)
