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

def countAtoms(molecule, count=defaultdict(int), multiplier=1):
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


def findSubmolecules(molecule,count=defaultdict(int), multiplier=1):
	brackets = {'(': ')', '[': ']', '{': '}'}
	match_str = '''\%s.*?\%s\d*'''	
	bracket_re = re.compile('[\[\(\{]')
	MultRe = re.compile('[\]\}\)]\d+$')
	while bracket_re.search(molecule) is not None:
		submolecule_open = bracket_re.search(molecule).group()
		m = re.compile(match_str % (submolecule_open, brackets[submolecule_open])).search(molecule)
		submolecule = re.compile('''\%s.*\%s''' % (submolecule_open, brackets[submolecule_open])).search(m.group()).group()[1:-1]
		m_multiplier = MultRe.search(m.group())
		if m_multiplier is  not None:
			s_multiplier = int(m_multiplier.group()[1:])
		else:
			s_multiplier = 1

		if bracket_re.search(submolecule) is None:
			count = countAtoms(submolecule, count=count, multiplier=multiplier*s_multiplier)
		else:
			submolecule = findSubmolecules(submolecule, count=count, multiplier=multiplier*s_multiplier)
		molecule = molecule.replace(m.group(),'')
	count = countAtoms(molecule, count=count, multiplier=multiplier)
	return molecule

def parse_molecule(formula):
	count = defaultdict(int)		
	formula =findSubmolecules(formula, count)
	return count

print(parse_molecule('H2O'))
print(parse_molecule('Mg(OH)2'))
print(parse_molecule('K4[ON(SO3)2]2'))
print(parse_molecule('(C5H5)Fe(CO)2CH3'))
print(parse_molecule('BCo3(CO2)3'))f
print(parse_molecule('Be4C5[BCo3(CO2)3]2'))
print(parse_molecule('As2{Be4C5[BCo3(CO2)3]2}4Cu5'))

