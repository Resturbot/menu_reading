import json

from PIL import Image
from pytesser.pytesser import *
import sys
import os, os.path

image_file_name = sys.argv[1]
im = Image.open(image_file_name)

# im = preprocess(im)
text = image_to_string(im)
text = image_file_to_string(image_file_name)
text = image_file_to_string(image_file_name, graceful_errors=True)

filename = sys.argv[1].split(".")[0]
filename = ''.join(e for e in filename if e.isalnum() or e == '-')
text_file_path = 'test.txt'

text_file = open(text_file_path, "w+")
text_file.write("%s" % text)
text_file.close()

food_items = []
prices = []

with open('test.txt') as f:
	for line in f:
		line = line.strip("\n")
		if any(char.isdigit() for char in line) and "-" in line:
			words = line.split("-")
			food_items.append(words[0])
			prices.append(int(words[1]))

data = dict(zip(food_items, prices))

def main():
	print json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
	return data

# with open('data.json', 'w') as outfile:
    # json.dump(data, outfile, sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == '__main__':
	main()

