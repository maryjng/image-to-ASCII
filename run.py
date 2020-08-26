from PIL import Image

#with Image.open("cat.jpg") as im:
#	im = im.convert("L")

ASCII_CHARS = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']
#255/11 for range

def resize(picture, OG_width):
	

def pixel_to_ASCII(picture):






def convLumi(picture):
	im = Image.open(picture)
	
	#get list of RGB tuples for each pixel
	pixels = list(im.getdata())
	
	#get dimensions of pic
	width, height = im.size
	
	pixelList = []
	for x in range(width):
		for y in range(length):
			pix = pixels[x, y]
			#convert to ASCII char
			lumi = (0.3 * pix[0]) + (0.59 * pix[1]) + (0.11 * pix[2])
			pixelList.append(lumi)
		
	print(pixelList)
