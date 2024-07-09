a = [34,35,69]

print(sum(a))
#this is sum

a = [34,35,69]
print(max(a))  # Output: 69

a = [0, 1, 2] # any(): Returns True if at least one element of the list is true. If the list is empty, returns False
print(any(a))  # Output: True

a = [0, 0, 0]# any(): Returns True if at least one element of the list is true. If the list is empty, returns False
print(any(a))  # Output: False

a = []
print(any(a))  # Output: False

a = [1, 2, 3]
print(all(a))  # Output: True

a = [1, 2, 0]
print(all(a))  # Output: False

a = []
print(all(a))  # Output: True

a = [34,35,69]
print(len(a))  # Output: 3

a = [34,35,69]
print(sorted(a))  # Output: [34, 35, 69]

import statistics
a = [34,35,69]
print(statistics.mean(a))  # Output: 46.0

import statistics
a = [34,35,69]
print(statistics.median(a))  # Output: 35

import math
a = [34,35,69]
print(math.prod(a))  # Output: 81210
#In this case, the list a contains the elements 34, 35, and 69. The math.prod() function multiplies these elements together to get the product, which is 81210.