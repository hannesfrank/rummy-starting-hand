# Rummy starting hand

Calculate the probability a set of cards of size N to include a matching set with at least 30 points. 

```sh
python startinghand.py
```

Probabilities of the standard deck without jokers:

| # cards | probability |
|-|-|
|   0 |  0.0 % |
|   1 |  0.0 % |
|   2 |  0.0 % |
|   3 |  0.1 % |
|   4 |  0.5 % |
|   5 |  1.2 % |
|   6 |  2.5 % |
|   7 |  4.0 % |
|   8 |  6.1 % |
|   9 |  8.6 % |
|  10 |  12.2 % |
|  11 |  15.5 % |
|  12 |  19.6 % |
|  13 |  24.4 % |
|  14 |  28.9 % |
|  15 |  34.8 % |
|  16 |  40.6 % |
|  17 |  45.0 % |
|  18 |  51.0 % |
|  19 |  56.4 % |
|  20 |  61.5 % |


You can also change the deck:

```py
import startinghand
from startinghand import COLORS, VALUES, DECK

# The default deck has 4 colors, 13 values and 2 cards of each:
# print(startinghand.COLORS)
# print(startinghand.VALUES)
# print(len(startinghand.DECK))

# Sample until Ctrl + C
startinghand.calculate_probability(
    num_cards=14,
    deck=DECK,
    colors=COLORS,
    values=VALUES)
```

**TODO:**

- [x] Format code
- [ ] Add support for jokers which should increase the probability.
