# You have an infinite number of the following two polyominoes: AAAA and BB.
#
# You are given a string region, filled with characters '.' and 'X'. You need
# to cover (without overlapping) all the 'X' characters with the given polyominoes.
# Return a string that contains the same region with cells marked '.' left untouched,
# and cells marked 'X' changed to 'A' or 'B', according to the polyomino that covers
# the cell.
#
# If there is no solution, return the string "impossible" (quotes for clarity only).
# If there are multiple solutions, return the lexicographically smallest one.

class LinearPolyominoCovering:
	def findCovering(self, region):
		XInARow = 0
		result = ''
		for char in region:
			if char == 'X':
				XInARow += 1
				continue

			if XInARow % 2 == 1: return 'impossible'

			while XInARow >= 4:
				result += 'AAAA'
				XInARow -= 4

			while XInARow >= 2:
				result += 'BB'
				XInARow -= 2

			XInARow = 0
			result += '.'

		if XInARow % 2 == 1: return 'impossible'

		while XInARow >= 4:
			result += 'AAAA'
			XInARow -= 4

		while XInARow >= 2:
			result += 'BB'
			XInARow -= 2

		XInARow = 0

		return result




print(LinearPolyominoCovering().findCovering('XXXXXX'))
print(LinearPolyominoCovering().findCovering('XX.XX'))
print(LinearPolyominoCovering().findCovering('XXXX....XXX.....XX'))
print(LinearPolyominoCovering().findCovering('X'))
print(LinearPolyominoCovering().findCovering('XX.XXXXXXXXXX..XXXXXXXX...XXXXXX'))
print(LinearPolyominoCovering().findCovering(''))