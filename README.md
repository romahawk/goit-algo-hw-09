# Optimal Coin Change Algorithms

## Introduction
This project implements two algorithms for determining the optimal way to give change to a customer: a Greedy algorithm and a Dynamic Programming algorithm. These algorithms are used in a cash register system to find the best way to give change using the least number of coins.

## Algorithms Implemented

### 1. Greedy Algorithm
The Greedy algorithm chooses the largest possible coin first, then the next largest, and so on, until the required amount is given. This approach is simple and fast but does not always produce the optimal solution for all coin sets.

#### Example:
For an amount of 113 using coins [50, 25, 10, 5, 2, 1], the result is:
{50: 2, 10: 1, 2: 1, 1: 1}


### 2. Dynamic Programming Algorithm
The Dynamic Programming algorithm finds the optimal solution by considering all possible combinations of coins to find the minimum number of coins needed to make the given amount. This approach guarantees the best solution but may be slower and more memory-intensive.

#### Example:
For an amount of 113 using coins [50, 25, 10, 5, 2, 1], the result is:
{50: 2, 10: 1, 2: 1, 1: 1}


## Comparison

### Greedy Algorithm
- **Time Complexity**: O(n)
- **Performance**: Fast and simple, suitable for cases where coin denominations allow optimal change.
- **Limitations**: May not always produce the optimal solution.

### Dynamic Programming Algorithm
- **Time Complexity**: O(n * amount)
- **Performance**: Provides the optimal solution for any coin set.
- **Limitations**: Can be slower and more memory-intensive for large amounts.

## Conclusion
- The Greedy algorithm is useful for quick and straightforward change calculation in systems with suitable coin denominations.
- The Dynamic Programming algorithm guarantees the optimal solution for any coin set, making it suitable for more complex scenarios where the Greedy approach fails.

## Usage
To run the algorithms, use the provided Python functions:
```python
def find_coins_greedy(amount):
    # Implementation of the Greedy algorithm

def find_min_coins(amount):
    # Implementation of the Dynamic Programming algorithm
Execute the functions with the desired amount to get the optimal coin distribution.
