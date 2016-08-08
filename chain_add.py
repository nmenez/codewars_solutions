# We want to create a function that will add numbers together when called in succession.

# add(1)(2);
# // returns 3
# We also want to be able to continue to add numbers to our chain.
# add(1)(2)(3); // 6
# add(1)(2)(3)(4); // 10
# add(1)(2)(3)(4)(5); // 15
# and so on.

# A single call should return the number passed in.

# add(1) // 1
# and we should be able to store the result and reuse it.

# var addTwo = add(2);
# addTwo // 2
# addTwo + 5 // 7
# addTwo(3) // 5
# addTwo(3)(5) // 10
# We can assume any number being passed in will be valid javascript number.


def add(x):
	class int_add(int):
		def __call__(self, x=0):
			return int_add(self.numerator + x)
	return int_add(x)

 
import unittest

class Testadd(unittest.TestCase):
	def test1(self):
		self.assertEqual(add(1), 1)
		self.assertEqual(add(1)(2), 3)

	def test2(self):
		addTwo = add(2)
		self.assertEqual(addTwo + 5, 7)
		self.assertEqual(addTwo(3), 5)

if __name__ == "__main__":
	unittest.main()

