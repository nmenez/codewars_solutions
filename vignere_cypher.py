import operator
class VigenereAutokeyCipher:
	def __init__(self, key, abc):
		self.key = key
		self.abc = abc
		self.key_values = [self.abc.index(a) for a in key]

	def getvalue(self, letter):
		return self.abc.index(letter)

	def getletter(self, value):
		return self.abc[value]

	def _encodedecode(self, op, text):
		key = self.key
		#while len(key) < len(text):
		#	key += key
		coded = []
		for let, key_letter in zip(text, key):
			if let in self.abc:
				coded.append(self.getletter(op(self.getvalue(let), self.getvalue(key_letter)) % len(self.abc)))
			else:
				coded.append(let)

		return ''.join(coded)

	def encode(self, text):
		op = operator.add
		return self._encodedecode(op, text)

	def decode(self, text):
		op = operator.sub
		return self._encodedecode(op, text)
	


#key = 'PASSWORD';
#abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

#c = VigenereAutokeyCipher(key, abc);

import unittest
class testVigenere(unittest.TestCase):
	def test_1(self):
		alphabet = 'abcdefghijklmnopqrstuvwxyz'
		key = 'password'
		c = VigenereAutokeyCipher(key, alphabet)

		self.assertEqual(c.encode('codewars'), 'rovwsoiv')
		self.assertEqual(c.encode('CODEWARS'), 'CODEWARS')

		self.assertEqual(c.decode('laxxhsj'),  'waffles')
	
	def test_2(self):
		key = 'PASSWORD';
		abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

		c = VigenereAutokeyCipher(key, abc);
		self.assertEqual(c.encode('AAAAAAAAPASSWORDAAAAAAAA'), 'PASSWORDPASSWORDPASSWORD')
		#self.assertEqual(c.decode('PASSWORDPASSWORDPASSWORD'), 'AAAAAAAAPASSWORDAAAAAAAA')

if __name__ == "__main__":
	unittest.main()
