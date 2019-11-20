import random

from python_charts import draw_chart, draw_multi_plot
from Data import ChartData

repetitions = 1000
# min_probability = 0.001
random.seed(12123123)


def coin_flip(p=0.5):
    return random.uniform(0, 1) <= p


def simulate(p=0.5, starting_a=50, starting_b=50):
    player_a = starting_a
    player_b = starting_b
    player_a_wins = 0
    course = []
    count = 0
    while player_a > 0 and player_b > 0:
        count += 1
        if coin_flip(p):
            player_a += 1
            player_b -= 1
            player_a_wins += 1
        else:
            player_a -= 1
            player_b += 1
        course.append(player_a_wins)
    return 0 if player_b == 0 else 1, count, course


def get_average_for_probability(p=0.5):
    player_a_wins = 0.0
    for x in range(repetitions):
        player_a_wins += simulate(p)[0]
    return player_a_wins / repetitions


def get_average_for_amount(player_a=50, total=100):
    player_a_wins = 0.0
    for x in range(repetitions):
        player_a_wins += simulate(0.5, player_a, total - player_a)[0]
    return player_a_wins / repetitions


def calculate_ruin(p, a, total):
    if p == 0:
        return 1
    if p == 1:
        return 0
    if p == 0.5:
        return a / total
    q_p = (1 - p) / p
    return (pow(q_p, a) - pow(q_p, total)) / (1 - pow(q_p, total))


def prepare_average_for_amount_data(divisions=10, total=100):
    delta = int(total / divisions)
    values = [(value + 1) * delta for value in range(divisions)]
    data = [get_average_for_amount(value, total) for value in values]
    optional_data = [1 - (value / total) for value in values]
    draw_chart(
        values,
        data,
        'Probability of Player A ruin by given starting budget',
        'a',
        'Q(a)',
        optional_data
    )


def prepare_average_for_probability_data(divisions=10):
    division = 1 / divisions
    probabilities = [value * division for value in range(divisions + 1)]
    data = [get_average_for_probability(p) for p in probabilities]
    data_optional = [calculate_ruin(p, 50, 100) for p in probabilities]
    draw_chart(
        format_number(probabilities),
        data,
        'Probability of Player A Losing a game by given p(a)',
        'p(a)',
        'Q(a)',
        data_optional
    )


def prepare_average_for_game_length(p=0.5):
    length_counter = {}
    a_wins = 0
    total_repetitions = repetitions
    for i in range(total_repetitions):
        value, length, course = simulate(p)
        a_wins += value
        if length not in length_counter:
            length_counter[length] = 0
        length_counter[length] += 1

    keys_sorted = sorted(length_counter.keys())
    values_sorted = [length_counter[key] / total_repetitions for key in keys_sorted]
    average = sum(keys_sorted) / len(keys_sorted)
    # keys_used = []
    # values_used = []
    # for key in keys_sorted:
    #     probability = length_counter[key] / total_repetitions
    #     if probability > min_probability:
    #         keys_used.append(key)
    #         values_used.append(probability)

    draw_chart(
        keys_sorted,
        values_sorted,
        'Probability of game having exact length using p(a) = {}, Average game length = {}'.format(p, average),
        'L',
        'P(L)'
    )


def prepare_course_of_game_data(trial, p=0.5, a=50, total=100):
    data = simulate(p, a, total)[2]
    x_data = range(len(data))
    return ChartData(x_data, data, 'trial {}'.format(trial))


def prepare_data_for_course_of_multiple_games(p=0.5, a=50, total=100, number_of_trials=3):
    data_gathered = [prepare_course_of_game_data(i, p, a, total) for i in range(number_of_trials)]
    draw_multi_plot(
        data_gathered,
        'number of toss',
        'player a wins',
        'player a wins trajectory for p(a) = {}, a = {}, a+b = {}'.format(p, a, total)
    )


def format_number(probabilities):
    probabilities = ["{:.2f}".format(p) for p in probabilities]
    return probabilities


def main():
    prepare_average_for_probability_data(10)
    prepare_average_for_amount_data(10, 100)
    prepare_average_for_game_length(0.2)
    prepare_average_for_game_length(0.5)
    prepare_average_for_game_length(0.8)
    prepare_data_for_course_of_multiple_games(0.2)
    prepare_data_for_course_of_multiple_games(0.5)
    prepare_data_for_course_of_multiple_games(0.8)


if __name__ == "__main__":
    main()
