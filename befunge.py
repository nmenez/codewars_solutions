import re
import random

def string2grid(bfstring):
	return [[e for e in row] for row in bfstring.split('\n')]

class Cursor(object):
	def __init__(self, grid):
		self.grid = grid
		self.row, self.col = 0, 0 
		self.stack =[]
		self.direction = '>'
		self.stringmode = False
		self.output = ''
		self.terminate = False
		self.consume_element(self.grid[0][0])

	def pos(self):
		return(self.row, self.col)

	def _move(self):
		if self.direction == '>':
			self.col += 1 
			if self.col == len(self.grid[self.row]):
				self.col = 0
		elif self.direction == '<':
			self.col -= 1
			if self.col == -1:
				self.col = len(self.grid[self.row]) - 1
		elif self.direction == 'v':
			self.row += 1	
			if self.row == len(self.grid):
			    self.row == 0
		elif self.direction == '^':
			self.row -= 1
			if self.row == -1:
				self.row = len(self.grid) -1


	def move(self):
		self._move()
		element = self.grid[self.row][self.col]
		#print(element, self.pos(), self.stack, self.output)
		self.consume_element(element)
	
	def consume_element(self, element):
		digitsre = re.compile('[0-9]')
		directionre = re.compile('[><v^?]')
		arithre = re.compile("[*+\-%/]")
		charre = re.compile('[a-zA-Z]')
		#if self.pos() == (0,16): import pdb; pdb.set_trace()

		if digitsre.match(element):
		    self.stack.append(element)


		elif directionre.match(element):
			if element == '?':
				self.direction = random.choice('<>v^')
			else:
				self.direction = element

		elif arithre.match(element):
			a = int(self.stack.pop())	
			b = int(self.stack.pop())
			e = str(eval('b %s a' % element ))
			self.stack.append(e)

		elif charre.match(element):
			if self.stringmode:
				self.stack.append(str(ord(element)))

			elif (element  == 'p') & (self.stringmode==False):
				y = int(self.stack.pop())
				x = int(self.stack.pop())
				v= self.stack.pop()
				#import pdb; pdb.set_trace()
				self.grid[y][x] = chr(int(v))

			elif (element == 'g') & (self.stringmode == False):
				#import pdb; pdb.set_trace()
				y = int(self.stack.pop())
				x = int(self.stack.pop())
				g = self.grid[y][x]
				self.stack.append(str(ord(g)))

			else:
				self.stack.append(element)

		elif element == '"':
			self.stringmode = not self.stringmode

		else:
			if self.stringmode:
				self.stack.append(str(ord(element)))
			else:
				if element == '`':
					a = int(self.stack.pop())	
					b = int(self.stack.pop())		
					if b > a:
						self.stack.append(1)
					else:
						self.stack.append(0)

				elif element == '!':
				    a = int(self.stack.pop())
				    if a == 0:
				    	self.stack.append(1)
				    else:
				    	self.stack.append(0)
				elif element == '_':
					a = int(self.stack.pop())
					
					if a == 0:
						self.direction = '>'
					else:
						self.direction = '<'

				elif element == '|':
					a = int(self.stack.pop())
					if a == 0:
						self.direction = 'v'
					else:
						self.direction = '^'
			


				elif element == ':':
					if len(self.stack) == 0:
						self.stack.append(0)
					else:
						last = self.stack[-1]
						self.stack.append(last)

				elif element == '\\':
					if len(self.stack) >= 2:
						a = self.stack.pop()
						b = self.stack.pop()
						self.stack.append(a)
						self.stack.append(b)
					else:
						a = self.stack.pop()
						self.stack.append(a)
						self.stack.append(0)

				elif element == '$':
					self.stack.pop()

				elif element == '.':
					a = self.stack.pop()
					#import pdb; pdb.set_trace()
					self.output += a

				elif element == ',':
					a = self.stack.pop()
					self.output += chr(int(a)) 

				elif element == '#':
					self._move()

			

				elif element == '@':
					self.terminate = True

	def run(self):
		while self.terminate is False:
			self.move()
		return self.output


def interpret(code):
	
	return Cursor(string2grid(code)).run()

import unittest

class testBefunge(unittest.TestCase):
	def test_count(self):
		code = '>987v>.v\nv456<  :\n>321 ^ _@'
		self.assertEqual(interpret(code), '123456789')

	def test_hello_world(self):
		code = '''>              v\nv  ,,,,,"Hello"<\n>48*,          v\nv,,,,,,"World!"<\n>25*,@'''
		self.assertEqual(interpret(code), 'Hello World!\n')

	def test_Quine(self):
		code ='01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@'
		self.assertEqual(interpret(code), '01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@')

	def test_sieve(self):
		code = '2>:3g" "-!v\  g30          <\n |!`"O":+1_:.:03p>03g+:"O"`|\n @               ^  p3\\" ":<\n2 234567890123456789012345678901234567890123456789012345678901234567890123456789'
		self.assertEqual(interpret(code), '2357111317192329313741434753596167717379')

if __name__ == '__main__':
	unittest.main()

