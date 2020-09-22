#TODO Figure out how to convert pixels to ASCII chars, accounting for when converted value is over len(charList)

from PIL import Image

charList = ['@','%','#','*','+','=','-',':','.',' ']

def resize(im, new_width = 100):
	im = Image.open(picture)
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
		convertedpixels.append(charList[pix // 25])
	print(convertedpixels)
	newpic = [convertedpixels[n:n + new_width] for n in range(0, len(covertedpixels), new_width)]

	return '\n'.join(newpic)

def run():
	pic = input("Enter the file name: ")
	to_ASCII(pic)

def printtotxt():
	pic = input("Enter the file name: ")
	output = to_ASCII(pic)
	t = open('output.txt', 'w')
	t.write(output)
	t.close

run()
printtotxt()
