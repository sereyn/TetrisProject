import qtido as qt
import tools

def merge(gB, b, x, y):
	gB2 = tools.clone2DList(gB)
	H, W = len(gB), len(gB[0])
	h, w = len(b), len(b[0])
	for i in range(w):
		for j in range(h):
			val = b[j][i]
			xx, yy = x+i, y+j
			xInRange = xx >= 0 and xx < W
			yInRange = yy >= 0 and yy < H
			if val == 1 and xInRange and yInRange:
				gB2[yy][xx] = val
	return gB2

def showGame(w, gB, size):
	H, W = len(gB), len(gB[0])
	for i in range(W):
		for j in range(H):
			qt.couleur(w, 0, 0, 0)
			if gB[j][i] == 1:
				qt.couleur(w, 1, 0, 0)
			x, y = size*i, size*j
			qt.rectangle(w, x, y, x+size, y+size)
