import numpy as np
from pathlib import Path


def is_safe(x):
    d = x[1:] - x[:-1]
    dabs_max = max(np.abs(d))
    dabs_min = min(np.abs(d))
    dmin = np.min(d)
    dmax = np.max(d)
    if dabs_min < 1 or dabs_max > 3 or (dmin < 0 and dmax > 0):
        return False
    return True


def dampen(x):
    for i in range(len(x)):
        x_ = np.delete(x, i)
        if is_safe(x_):
            return True
    return False


def load_data(fp: str) -> dict[int, np.ndarray]:
    data = {}
    with Path(fp).resolve().absolute().open("r") as f:
        for idx, line in enumerate(f):
            x = np.array([int(i) for i in line.rstrip("\n").split(" ")])
            data[idx] = x
    return data


def part_one(fp: str):
    data = load_data(fp)
    results = []
    for _, val in data.items():
        results.append(is_safe(val))
    print(f"{sum(results)=}")
    return results


def part_two(fp: str):
    data = load_data(fp)
    results = []
    for _, val in data.items():
        _safe = is_safe(val) or dampen(val)
        results.append(_safe)
    print(f"{sum(results)=}")
    return results


def main(fp: str):
    part_one(fp)
    part_two(fp)


if __name__ == "__main__":
    main("/Users/samforeman/Downloads/aoc_day2.txt")
