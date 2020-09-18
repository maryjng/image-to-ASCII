from PIL import Image
import numpy as np

charList = ['`', '^', '"', ',', ':', ';', 'I', 'l', '!', 'i', '~', '+', '_', '-', '?', ']', '[', '}', '{', '1', ')', '(', '|', '\\', '/', 't', 'f', 'j', 'r', 'x', 'n', 'u', 'v', 'c', 'z', 'X', 'Y', 'U', 'J', 'C', 'L', 'Q', '0', 'O', 'Z', 'm', 'w', 'q', 'p', 'd', 'b', 'k', 'h', 'a', 'o', '*', '#', 'M', 'W', '&', '8', '%', 'B', '@', '$']

def open_picture(picture):
	im = Image.open(picture)
	return im

def resize(im, new_width = 40):
	width, height = im.size
	ratio = width//height
	new_height = new_width//ratio

	im.resize((new_width, new_height))
	return im

def convGray(im):
	im = im.convert("L")
	return im

def to_ASCII(picture):
	im = open_picture(picture)
	resized_im = resize(im)
	imagegray = convGray(resized_im)

	pixels = list(imagegray.getdata())

	width, height = resized_im.size

	convertedpixels = []
	for pix in pixels:
		convertedpixels.append(charList[pix // 65])

	newpic = []
	for x in convertedpixels:

	#just need to print the list of pixels out in proper dimension

	# print(newpic)

pic = input("Enter the file name: ")
to_ASCII(pic)
