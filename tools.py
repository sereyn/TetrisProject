import qtido as qt

def print2DList(l):
	print(*l, sep="\n", end="\n\n")

def get2DGrid(w, h):
	l = []
	for i in range(h):
		temp = []
		for j in range(w):
			temp.append(0)
		l.append(temp)
	return l

def cloneList(l):
	l2 = []
	for i in range(len(l)):
		l2.append(l[i])
	return l2

def clone2DList(l):
	l2 = []
	for i in range(len(l)):
		l2.append(cloneList(l[i]))
	return l2

def clear(w):
	qt.couleur(w, 1, 1, 1)
	qt.rectangle(w, 0, 0, w.w, w.h)
