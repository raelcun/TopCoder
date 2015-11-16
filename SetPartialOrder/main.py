# In math, we sometimes define a partial order on some objects. In this problem we will take a look at one
# possible way how to define a partial order on sets of integers.
#
# Consider two sets of integers: X and Y. These two sets can be related to each other in four possible ways:
#  - X is equal to Y if each element of X is also an element of Y and vice versa.
#  - X is less than Y if X is not equal to Y (see previous item) and each element of X is also an element of Y.
#  - X is greater than Y if Y is less than X.
#  - In all other cases X and Y are incomparable.
#
# In other words: X is less than Y if and only if X is a proper subset of Y. Two sets are incomparable if neither
# is a subset of the other.
#
# You are given two tuple (integer)s a and b. The elements of a form the set X. The elements of b form the set Y.
# Compare X to Y and return the correct one of the following four strings: "EQUAL", "LESS", "GREATER", or "INCOMPARABLE".

from functools import reduce

class SetPartialOrder:
	def compareSets(self, a, b):
		ainb = reduce(lambda acc, curr: acc and curr in b, a)
		bina = reduce(lambda acc, curr: acc and curr in a, b)
		if ainb and bina: return 'EQUAL'
		if ainb and not bina: return 'LESS'
		if bina and not ainb: return 'GREATER'
		return 'INCOMPARABLE'

print(SetPartialOrder().compareSets({1,2,3,5,8}, {8,5,1,3,2}))
print(SetPartialOrder().compareSets({2,3,5,7}, {1,2,3,4,5,6,7,8,9,10}))
print(SetPartialOrder().compareSets({2,4,6,8,10,12,14,16}, {2,4,8,16}))
print(SetPartialOrder().compareSets({42,23,17}, {15,23,31}))