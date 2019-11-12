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
			print('hou bag! "' + caption + ' cat" already exists!')
		else:
			print('hou no.. "' + caption + '" already exists!')
	else:
		print('u haven\'t used "' + caption + '" yet!')

if __name__ == "__main__":
	caption = str(sys.argv[1])
	checkUnique(caption)

