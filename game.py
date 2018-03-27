class Blocks:
	#Legend: http://i.imgur.com/9Z0oJXe.png
	o = [
	[1, 1],
	[1, 1]]
	i = [
	[1, 1, 1, 1]]
	j = [
	[1, 0, 0],
	[1, 1, 1]]
	l = [
	[0, 0, 1],
	[1, 1, 1]]
	s = [
	[0, 1, 1],
	[1, 1, 0]]
	z = [
	[1, 1, 0],
	[0, 1, 1]]
	t = [
	[0, 1, 0],
	[1, 1, 1]]

	def rotate(trigoWay, block):
		w, h = len(block[0]), len(block)
		newBlock = []
		for i in range(w*h):
			if trigoWay:
				coords = [i%h, w-1-int(i/(w-1))]
			else:
				coords = [h-1-i%h, int(i/(w-1))]
			if i%h == 0:
				newBlock.append([])
			newBlock[int(i/(w-1))].append(block[coords[0]][coords[1]])
		return newBlock



