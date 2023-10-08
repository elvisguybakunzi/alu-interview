# Rainwater Trapping

This project provides a Python function to calculate the amount of rainwater that can be trapped between walls represented as a list of non-negative integers.

## Table of Contents

- [Usage](#usage)
- [How It Works](#how-it-works)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Usage

To use the `rain` function, simply import it and pass a list of non-negative integers representing the heights of walls. The function will return the total amount of rainwater retained.

```python
from rainwater_trapping import rain

walls = [0, 1, 0, 2, 0, 3, 0, 4]
result = rain(walls)
print(result)  # Output: 6

```
