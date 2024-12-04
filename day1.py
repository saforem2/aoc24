import numpy as np


def main(fp: str) -> tuple:
    x = np.loadtxt(fp)
    x0, x1 = x[:, 0], x[:, 1]
    x0.sort()
    x1.sort()
    dx = np.abs(x1 - x0)
    ans_p1 = dx.sum()
    print(f"part 1: {int(ans_p1)}")

    x0 = x0.astype(int)
    x1 = x1.astype(int)
    s = []
    for x in x0:
        matches = len(x1[x1 == x])
        s.append(x * matches)
    ans_p2 = sum(s)
    print(f"part 2: {ans_p2}")
    return ans_p1, ans_p2


if __name__ == "__main__":
    main("/Users/samforeman/Downloads/aoc_day1.txt")
