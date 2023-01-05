import math
import os
import random
import re
import sys
import numpy as np

def formingMagicSquare(s):
    # Write your code here
    first = [[8,1,6], [3,5,7],[4,9,2]]
    second = [[6,1,8], [7,5,3],[2,9,4]]
    third = [[8,3,4], [1,5,9],[6,7,2]]
    fourth = [[4,9,2], [3,5,7],[8,1,6]]
    fifth = [[2,9,4], [7,5,3],[6,1,8]]
    sixth = [[4,3,8], [9,5,1],[2,7,6]]
    seventh = [[2,7,6], [9,5,1],[4,3,8]]
    eight =  [[6,7,2], [1,5,9],[8,3,4]]

    all_magic = [first, second, third, fourth, fifth, sixth, seventh, eight]
    max = sys.maxsize
    for magic in all_magic:
        sum = 0
        for i in range(0,3):
            for j in range(0,3):
                
                sum += abs(s[i][j] - magic[i][j])
        difference = sum
        if difference < max:
            max = difference
    return max

test1= [[4,8,2], [4,5,7],[6,1,6]]

print(formingMagicSquare(test1))