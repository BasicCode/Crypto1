#Python jpeg steganography parser and test

import binascii

file = "c:/Users/tommy/OneDrive/Documents/crypto1/shannon/100QMAT1.jpg"

def openFile(file):
	data = []
	with open(file, "rb") as f:
		for line in f:
			data.append(line)
	return data
	
def findAlpha(data):
	ret = []
	for line in data:
		for char in line:
			if char > 65:
				ret.append(chr(char))
	return ret

if __name__ == '__main__':
	#Print out all chars in a jpg
	data = openFile(file)
	print(findAlpha(data))