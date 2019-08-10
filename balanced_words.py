def balanced_word(stri):
	dicti = {}
	y = []
	a = []
	e = []
	m = []
	o = len(stri)/2
	for i in range(97, 123):
		y.append(chr(i))
	for i in range(len(y)):
		dicti[y[i]] = i+1

	if len(stri)%2 == 0:
		x = list(stri[:o])
		p = list(stri[o:len(stri)])
	else:
		x = list(stri[:o])
		p = list(stri[o+1:len(stri)])
	print x,p
	for i in range(len(x)):
		a.append(dicti[x[i]])
	for i in range(len(p)):
		e.append(dicti[p[i]])
	if sum(a) == sum(e):
		print True
	else:
		print False

print(balanced_word("peeweep"))