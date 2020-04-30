import random


possibilities = ["U", "D", "_"]


def rhythm_bot():
    pattern = []
    for length in range(8):
        pattern += random.choices(possibilities)
    print(pattern)


rhythm_bot()
