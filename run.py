from PIL import Image
from numpy import reshape

charList =  `^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$

def resize(picture, new_width = 25):
	width, height = picture.size
	ratio = width//height
	new_height = new_width//ratio

	return new_width, new_height


#resize original pic. takes new_width and calculates new_height using the pic's width/height ratio.

def convGray(picture):
	with Image.open(picture) as im:
		im = im.convert("L")


	# not needed prolly. numpy.reshape(pixels, (width, height))
	#graypixels list

def to_ASCII(picture):
	convGray(picture)

	pixels = list(im.getdata())

	width, height = im.size

	newpic = []
	for pix in graypixels:
		newpic.append(charList[pix // 4])

	numpy.reshape(newpic, (width, height))
	print(newpic)

# each pixel has a value from 0 - 255. Floor by 4 and assign to ASCII char.


convGray("sadcat.PNG")
