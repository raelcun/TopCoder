import math

class AB:
	def createString(self, N, K):
		if K > (N/2)*(N/2)+(0 if N%2==0 else N/2): return ""
		bCount = int(math.ceil(N/2))
		str = 'B' * bCount
		matches = 0
		while matches < K:
			right = K - matches
			if right > bCount: right = bCount
			insertAt = len(str) - right
			str = str[:insertAt] + 'A' + str[insertAt:]
			matches += right
		return str.rjust(N, 'B')

print('result:',AB().createString(3, 2))
print('result:',AB().createString(2, 0))
print('result:',AB().createString(5, 8))
print('result:',AB().createString(10, 12))