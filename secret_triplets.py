# There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.

# A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".

# As a simplification, you may assume that no letter occurs more than once in the secret string.

# You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string. In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.

secret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]


	def recoverSecret(triplets):
		out_string = ''
		letters = set(sum(triplets,[]))
		while len(out_string) <= len(letters)-1:
			positions = list(zip(*triplets))
			(next_letter, ) = set(positions[0]).difference(set(positions[1])).difference(positions[2])
			out_string += next_letter
			for triplet in triplets:
				if next_letter in triplet:
				    triplet.remove(next_letter)
				    triplet.append('')

		return out_string
print(recoverSecret(triplets))