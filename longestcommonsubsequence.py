def lcs(X,Y, LCS=''):
	if (X=='') or (Y==''):
		return ''
		
	if X[-1] == Y[-1]:
		return lcs(X[:-1], Y[:-1], X[-1]) + X[-1]
	else:
		LCS1 = lcs(X, Y[: -1])
		LCS2 = lcs(X[:-1],  Y)
		if len(LCS1) >= len(LCS2):
			return LCS1
		else:
			return LCS2
		
print(lcs('BANANA', 'ATANA'))	
print(lcs('abcdef','abc'))
print(lcs( "132535365" , "123456789" ))
print(lcs( "abcdef" , "acf" ))