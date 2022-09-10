# To find a maximum number in the list
from functools import reduce
l = [3, 8, 455, 2, 5, 45]

a = reduce(max, l)
print(a)