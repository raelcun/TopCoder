# Inefficient. Passes all basic tests, but fails system tests (probably due to speed)

class ABBA:
	def canObtainInefficient(self, initial, target):
		# print(initial,target)
		if initial == target:
			# print('returned true')
			return 'Possible'
		if len(initial) >= len(target):
			# print('returned false')
			return 'Impossible'

		if initial not in target and initial not in target[::-1]: return 'Impossible'

		# print('adding A to',initial)
		a = self.canObtain(initial + 'A', target)
		# print('reversing',initial,'and adding B')
		b = self.canObtain(initial[::-1] + 'B', target)
		if a == 'Possible' or b == 'Possible': return 'Possible'
		return 'Impossible'

	def canObtain(self, initial, target):
		while len(target) > len(initial):
			if target[-1] == 'A':
				target = target[:-1]
			else:
				target = target[:-1]
				target = target[::-1]

		return 'Possible' if target == initial else 'Impossible'

print(ABBA().canObtain('B','ABBA'))
print(ABBA().canObtain('ABB','ABB'))
print(ABBA().canObtain('A','BBAB'))
print(ABBA().canObtain('BBBBABABBBBBBA','BBBBABABBABBBBBBABABBBBBBBBABAABBBAA'))
print(ABBA().canObtain('A','BB'))