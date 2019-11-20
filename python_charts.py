from math import sqrt, pi, exp, pow

import matplotlib.pyplot as plt

mu = 0
sigma = 1


def normal_dist(x):
    sigma2 = pow(sigma, 2)
    const = 1 / (sqrt(2 * sigma2 * pi))
    e = exp((-1) * pow(x - mu, 2) / sigma2 / 2)
    return const * e


def draw_histogram(data, num_bins=50):
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(data, num_bins, density=True)
    # y = [normal_dist(x) for x in bins]
    # ax.plot(bins, y, '--')
    y = [((1 / (sqrt(2 * pi) * sigma)) * exp(-0.5 * (1 / sigma * (binn - mu)) ** 2)) for binn in bins]
    ax.plot(bins, y, '--')
    ax.set_xlabel('Values')
    ax.set_ylabel('Probability density')

    fig.tight_layout()
    plt.show()


def draw_chart(x_data, y_data, title='', x_label='', y_label='', optional_data=[]):
    x_positions = [x * 10 for x in range(len(x_data))]
    plt.figure(figsize=(15, 9))
    plt.bar(x_data, y_data, align='center')
    if len(optional_data) > 0:
        plt.plot(x_data, optional_data, color='skyblue', marker='.', markersize=10)
    plt.tick_params(axis='x', labelsize=7)
    # plt.xticks(x_positions, x_data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def draw_plot(x_data, y_data, title='', x_label='', y_label=''):
    fig, ax = plt.subplots()
    ax.plot(x_data, y_data)
    ax.set(xlabel=x_label, ylabel=y_label, title=title)
    ax.grid()
    plt.show()


def draw_multi_plot(data_set, x_label='', y_label='', title=''):
    fig, ax = plt.subplots()
    for data in data_set:
        ax.plot(data.x_data, data.y_data, label=data.label)
    ax.set(xlabel=x_label, ylabel=y_label, title=title)
    plt.legend()
    plt.show()
