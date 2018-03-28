#Legend: http://i.imgur.com/9Z0oJXe.png
def get(letter):
	if letter == "o":
		return [
			[1, 1, 0, 0],
			[1, 1, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
		]
	if letter == "i":
		return [[1, 1, 1, 1]]
	if letter == "j":
		return [[1, 0, 0],[1, 1, 1]]
	if letter == "l":
		return [[0, 0, 1],[1, 1, 1]]
	if letter == "s":
		return [[0, 1, 1],[1, 1, 0]]
	if letter == "z":
		return [[1, 1, 0],[0, 1, 1]]
	if letter == "t":
		return [[0, 1, 0],[1, 1, 1]]

def rotate(block):
	w, h = len(block[0]), len(block)
	newBlock = []
	for i in range(w*h):
		coords = [i%h, w-1-int(i/(w-1))]
		if i%h == 0:
			newBlock.append([])
		newBlock[int(i/(w-1))].append(block[coords[0]][coords[1]])
	return newBlock
