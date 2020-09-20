from PIL import Image
import numpy as np

charList = ['@','%','#','*','+','=','-',':','.',' ']

def open_picture(picture):
	im = Image.open(picture)
	return im

def resize(im, new_width = 100):
	width, height = im.size
	ratio = width//height
	new_height = new_width//ratio
	newsize = (new_width, new_height)
	resized_im = im.resize(newsize)
	return resized_im

def convGray(im):
	im = im.convert("L")
	return im

def to_ASCII(picture):
	im = open_picture(picture)
	resized_im = resize(im)
	width, height = resized_im.size
	imagegray = convGray(resized_im)
	pixels = list(imagegray.getdata())

	convertedpixels = []
	for pix in pixels:
		convertedpixels.append(charList[pix // 10])

	lineofpixels = []
	n = 0
	while width < len(convertedpixels):
		while n < width:
			lineofpixels.append(convertedpixels[n])
			n += 1
		print("".join(lineofpixels))
		n += n
		width += width

pic = input("Enter the file name: ")
to_ASCII(pic)
