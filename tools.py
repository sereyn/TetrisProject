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

def wait(w, fps, time):
	qt.attendre_pendant(w, 1000/fps)
	return time+1

def key(which):
	keys = ["left", "up", "right", "down"]
	nums = [16777234, 16777235, 16777236, 16777237]
	for i in range(len(keys)):
		if which == keys[i]:
			return nums[i]
	return 0

def press(which, keys):
	return key(which) in keys