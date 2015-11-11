import sys
import time
import json
import requests
import os
from facepp import API, File
API_KEY = "19e15e1bc1056ef1cf9ad76cff56b4a6"
API_SECRET = "XdoDpYtBr6DFWZPFfdPfZJiZa-TcpoWq"
api = API(API_KEY, API_SECRET)
def is_human(path):
	true = 0;
	false = 0;
	for root, dirs, files in os.walk(path):
		for name in files:
			image = path+name
			if image.endswith("g"):
				ret = api.detection.detect(img = File(image))
				if 'face' in ret:
					if len(ret['face']) == 0:
						print image + " - false"
						false = false + 1
					else:
						print image + " - true"
						true = true + 1
	print "For " + path + ": true = " + str(true) + " false = " + str(false) + "\n"

is_human("human/")
is_human("animal/")
is_human("anime/")
