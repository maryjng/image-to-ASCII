from PIL import Image

with Image.open("cat.jpg") as im:
	im = im.convert("L")

pixels = list(im.getdata())

width, height = im.size

pixelList = []
for x in range(width):
	for y in range(length):
		pix = pixels[x, y]
		lumi = (0.3 * pixels[0]) + (0.59 * pixels[1]) + (0.11 * pixels[2])
		#convert to ASCII char
		pixelList.append(lumi)

#print pixelList
