# Recently you learned about substitution ciphers. This problem is about such a cipher. All strings in
# this problem (both encrypted and decrypted ones) will consist of only uppercase English letters ('A'-'Z').
#
# When encrypting text using a substitution cipher we choose a substitution table: a permutation p of the
# alphabet. In other words, for each letter x in the alphabet we choose a letter p(x) that will be used to
# encode x. This encoding must be one-to-one: if x and y are two different letters, the letters p(x) and p(y)
# chosen to encode them must also be different.
#
# You decided to try it out: you chose some specific substitution table and used it to encrypt some strings.
# At some later point in time you found an encrypted string y. You believe it was encrypted using the substitution
# table you once had. Sadly, you do not remember the substitution table anymore. The only thing you remember about
# it is that when you used it to encrypt the string a you got the string b. Is this information sufficient to
# decrypt y?
#
# You are given the strings a, b, and y. If it is possible to decrypt the string y, return the original string x
# that was encrypted into y. (More precisely: If there is exactly one string x such that the same permutation table
# can be used to encrypt a into b and to encrypt x into y, return x.) Otherwise, return an empty string.

class SubstitutionCipher:
	def decode(self, a, b, y):
		# find mapping from a to b
		mapping = {}
		for index in range(0, len(a)):
			currentLetter = a[index]
			encodedLetter = b[index]
			if encodedLetter in mapping:
				if mapping[encodedLetter] != currentLetter: return ''
				continue
			mapping[encodedLetter] = currentLetter
		
		if len(mapping) == 25:
			alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
			mapping[list(alphabet - set(mapping.keys()))[0]] = list(alphabet - set(mapping.values()))[0]

		result = ''
		for index in range(0, len(y)):
			encodedLetter = y[index]
			if encodedLetter not in mapping: return ''
			result += mapping[encodedLetter]

		return result

print(SubstitutionCipher().decode('CAT', 'DOG', 'GOD'))
print(SubstitutionCipher().decode('BANANA', 'METETE', 'TEMP'))
print(SubstitutionCipher().decode('THEQUICKBROWNFOXJUMPSOVERTHELAZYHOG', 'UIFRVJDLCSPXOGPYKVNQTPWFSUIFMBAZIPH', 'DIDYOUNOTICESKIPPEDLETTER'))