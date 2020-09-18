from PIL import Image
import numpy as np

charList = ['`', '^', '"', ',', ':', ';', 'I', 'l', '!', 'i', '~', '+', '_', '-', '?', ']', '[', '}', '{', '1', ')', '(', '|', '\\', '/', 't', 'f', 'j', 'r', 'x', 'n', 'u', 'v', 'c', 'z', 'X', 'Y', 'U', 'J', 'C', 'L', 'Q', '0', 'O', 'Z', 'm', 'w', 'q', 'p', 'd', 'b', 'k', 'h', 'a', 'o', '*', '#', 'M', 'W', '&', '8', '%', 'B', '@', '$']


def resize(picture, new_width = 25):
	im = Image.open(picture)

	width, height = im.size
	ratio = width//height
	new_height = new_width//ratio

	im.resize((new_width, new_height))
	return im

def convGray(picture):
	with Image.open(picture) as im:
		im = im.convert("L")
	return im

def to_ASCII(picture):
	image = resize(picture)
	image = convGray(picture)

	pixels = list(image.getdata())

	width, height = image.size

	convertedpixels = []
	for pix in pixels:
		convertedpixels.append(charList[pix // 4])

	newpic = np.array(convertedpixels).reshape(width, height)

	print(newpic)

to_ASCII("images/angery.PNG")
