from PIL import Image

charList = [' ', '.', "'", '`', '^', '"', ',', ':', ';', 'I', 'l', '!', 'i', '>', '<', '~', '+', '_', '-', '?', ']', '[', '}', '{', '1', ')', '(', '|', '\\', '/', 't', 'f', 'j', 'r', 'x', 'n', 'u', 'v', 'c', 'z', 'X', 'Y', 'U', 'J', 'C', 'L', 'Q', '0', 'O', 'Z', 'm', 'w', 'q', 'p', 'd', 'b', 'k', 'h', 'a', 'o', '*', '#', 'M', 'W', '&', '8', '%', 'B', '@', '$']

def resize(im, new_width = 100):
	im = Image.open(im)
	width, height = im.size
	ratio = width//height
	new_height = new_width*ratio
	newsize = (new_width, new_height)
	resized_im = im.resize(newsize)
	return resized_im

def convGray(im):
	return im.convert("L")

def to_ASCII(im):
	resized_im = resize(im)
	width, height = resized_im.size
	imagegray = convGray(resized_im)
	pixels = list(imagegray.getdata())

	convertedpixels = []
	for pix in pixels:
		convertedpixels.append(charList[(pix // 4) - 1])

	newpic = [convertedpixels[n:n + width] for n in range(0, len(convertedpixels), width)]
	return newpic

def run():
	pic = input("Enter the file name: ")
	endpic = to_ASCII(pic)
	f = open("output.txt", "w")
	for line in endpic:
		f.write("\n" + "".join(line))
	f.close

run()
