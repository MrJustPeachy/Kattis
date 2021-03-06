'''
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

import math

sumOfSquares = sum([i ** 2 for i in range(1, 101)])
squareOfSums = math.pow(sum([i for i in range(1, 101)]), 2)

difference = squareOfSums - sumOfSquares

print(int(difference))