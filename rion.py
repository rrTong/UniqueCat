import sys

def checkUnique(caption):
	unique = False
	uniqueCat = False

	print('\n\n\n\n\n\n')

	with open('captions.txt') as f:
		if caption + " cat" in f.read():
			uniqueCat = True
	
	with open('captions.txt') as f:
		if caption in f.read():
			unique = True

	if uniqueCat or unique:
		if uniqueCat:
			print('\n ( \"' + caption + ' cat" already exists! ) ')
		else:
			print('\n ( \"' + caption + '" already exists! ) ')
		print('''
                  v

              |\-----/|
              | ° ω ° |
               \_____/
              ''')
	else:
		if caption.endswith(' cat'):
			print('\n ( u haven\'t used "' + caption + '" yet! ) ')
		else:
			print('\n ( u haven\'t used "' + caption + ' cat" yet! ) ')
		print('''
                  v

              |\-----/|
              | ᵘ ω ᵘ |
               \_____/
              ''')

	print('\n\n\n\n\n\n')

if __name__ == "__main__":
	caption = str(sys.argv[1])
	checkUnique(caption)
