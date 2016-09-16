def makeminor(matrix, i):
	minor = []
	for row in matrix[1:]:
		minor.append([e for idx, e in enumerate(row) if idx != i])
	if len(minor) == 1:
		return minor
	return minor

def determinant(matrix):
	if len(matrix) == 1:
		return matrix[0][0]
	return sum([e*determinant(makeminor(matrix, i))*(-1)**i for i, e in enumerate(matrix[0])])


m1 = [[1,3],[2,5]]
m2 = [ [2,5,3], [1,-2,-1], [1, 3, 4]]
print(determinant([[1]]))
print(determinant(m1))
print(determinant(m2))