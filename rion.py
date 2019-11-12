import sys

def checkUnique(caption):
	unique = False
	uniqueCat = False

	with open('captions.txt') as f:
		if caption + " cat" in f.read():
			uniqueCat = True
	
	with open('captions.txt') as f:
		if caption in f.read():
			unique = True

	if uniqueCat or unique:
		if uniqueCat:
			print("\"" + caption + ' cat" already exists!')
		else:
			print("\"" + caption + '" already exists!')
	else:
		if caption.endswith(' cat'):
			print('u haven\'t used "' + caption + '" yet!')
		else:
			print('u haven\'t used "' + caption + ' cat" yet!')

if __name__ == "__main__":
	caption = str(sys.argv[1])
	checkUnique(caption)
