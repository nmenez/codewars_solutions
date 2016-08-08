# For a given chemical formula represented by a string, count the number of atoms of each element contained in the molecule and return an object.

# For example:

# water = 'H2O'
# parse_molecule(water)                 # return {H: 2, O: 1}

# magnesium_hydroxide = 'Mg(OH)2'
# parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}

# var fremy_salt = 'K4[ON(SO3)2]2'
# parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}
# As you can see, some formulas have brackets in them. The index outside the brackets tells you that you have to multiply count of each atom inside the bracket on this index. For example, in Fe(NO3)2 you have one iron atom, two nitrogen atoms and six oxygen atoms.

# Note that brackets may be round, square or curly and can also be nested. Index after the braces is optional.

import re
from collections import defaultdict
from itertools import chain

SquareRe = re.compile('\[.*\]\d*')
RoundRe = re.compile('\(.*\)\d*')
CurlyRe =re.compile('\{.*\}\d*')
NumberRe = re.compile('\d*$')
matchers = [SquareRe, RoundRe, CurlyRe]

def countAtoms(molecule, count=None, multiplier=1):
	Atom1 = re.compile('[A-Z]\d*')
	Atom2 = re.compile('[A-Z][a-z]\d*')
	Numbers = re.compile('\d+$')

	Atoms_pos = defaultdict(int)
	for atom in chain(Atom1.finditer(molecule), Atom2.finditer(molecule)):
		_start, _end =atom.span()
		Atoms_pos[_start] = molecule[_start:_end]

	if count is None:
		count = {}
	for pos, atom in Atoms_pos.items():
		match = Numbers.search(atom)
		if match is not None:
			_start, _end = match.span()
			count[atom[:_start]] += int(atom[_start:_end])*multiplier
		else:
			count[atom] += 1*multiplier
	return count
#print(countAtoms('SO3'))

def findSubmolecules(molecule,count,multiplier=1):
	#import pdb; pdb.set_trace()
	#print(indent, 'molecule', molecule, 'count', count)
	for matcher in matchers:
		m = matcher.search(molecule)
		if m is not None:
			_start, _end = m.span()
			submolecule = molecule[_start+1:_end-2]
			import pdb; pdb.set_trace()
			submolecule_multiplier = int(NumberRe.findall(molecule[_start:_end])[0])

			submolecule = findSubmolecules(submolecule, count, multiplier=multiplier*submolecule_multiplier)

			count = countAtoms(submolecule, count , multiplier*submolecule_multiplier)
			molecule = molecule.replace(molecule[_start:_end], '')
			

	return molecule

def parse_molecule(formula):
	count = defaultdict(int)		
	formula =findSubmolecules(formula, count)
	count = countAtoms(formula,count)
	return count

#print(parse_molecule('H2O'))
#print(parse_molecule('Mg(OH)2'))
#print(parse_molecule('K4[ON(SO3)2]2'))
parse_molecule('(C5H5)Fe(CO)2CH3')
