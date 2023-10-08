#!/usr/bin/python3

"""
rain.py
"""


def rain(walls):
    """
    Calculate how many square units of water will be retained after it rains.

    Args:
        walls (list): List of non-negative integers representing the heights of walls.

    Returns:
        int: Total amount of rainwater retained.
    """
    if len(walls) == 0:
        return 0

    left_max = [0] * len(walls)
    right_max = [0] * len(walls)

    left_max[0] = walls[0]
    for i in range(1, len(walls)):
        left_max[i] = max(left_max[i - 1], walls[i])

    right_max[-1] = walls[-1]
    for i in range(len(walls) - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    total_water = 0
    for i in range(len(walls)):
        water_height = min(left_max[i], right_max[i]) - walls[i]
        total_water += water_height

    return total_water


if __name__ == "__main__":
    walls = [0, 1, 0, 2, 0, 3, 0, 4]
    print(rain(walls))
    walls = [2, 0, 0, 4, 0, 0, 1, 0]
    print(rain(walls))
