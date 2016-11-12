import numpy as np

from PIL import Image
from pytesser.pytesser import *
import sys
import os, os.path

def preprocess(image):
	# image.show()
	image = np.array(image)
	for sublist in image:
		for entry in sublist:
			if sum(entry) < 750:
				for value in entry:
					value = 0;
	image = Image.fromarray(image)
	# image.show()
	return image

directory_path = '/converted-text/'

image_file_name = sys.argv[1]
im = Image.open(image_file_name)

im = preprocess(im)
text = image_to_string(im)
text = image_file_to_string(image_file_name)
text = image_file_to_string(image_file_name, graceful_errors=True)

filename = sys.argv[1].split(".")[0]
filename = ''.join(e for e in filename if e.isalnum() or e == '-')
text_file_path = filename + '.txt'

text_file = open(text_file_path, "w+")
text_file.write("%s" % text)
text_file.close()

print('done')