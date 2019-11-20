import random
from math import log, sqrt, pow
from statistics import stdev

from python_charts import draw_histogram


def get_random():
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    while sqrt(get_exp((x, y))) >= 1 or x + y == 0.0:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
    return x, y


def get_exp(point):
    return pow(point[0], 2) + pow(point[1], 2)


def get_new_r():
    v = get_random()
    return get_exp(v)


def get_points():
    v = get_random()
    r2 = get_exp(v)
    return get_y(v[0], r2), get_y(v[1], r2)


def get_y(v, r2):
    x = log(r2) * (-2.0)
    y = sqrt(x / r2)
    return v * y


def normalize(values):
    average = sum(values) / len(values)
    variance = sqrt(
        sum(
            [pow(val - average, 2) for val in values]
        )
    )
    return [(val - average) / variance for val in values]


def main():
    total_repetitions = 1000000
    data = [get_points() for point in range(total_repetitions)]
    data_merged = [item for y_tuple in data for item in y_tuple]
    draw_histogram(data_merged)


if __name__ == "__main__":
    main()
