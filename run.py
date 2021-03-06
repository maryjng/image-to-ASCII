from PIL import Image

charList = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']

def resize(im, new_width = 100):
	im = Image.open(im)
	width, height = im.size
	wratio = new_width/float(width)
	new_height = int((float(height))*wratio)
	newsize = (new_width, new_height)
	resized_im = im.thumbnail(newsize)
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
		convertedpixels.append(charList[(pix // 25) - 1])

	newpic = [convertedpixels[n:n + width] for n in range(0, len(convertedpixels), width)]
	return newpic

def run():
	pic = input("Enter the file name: ")
	endpic = to_ASCII(pic)
	f = open("output.txt", "w")
	for line in endpic:
		f.write("\n" + "".join(line))
	f.close
	print("Done.")

run()
