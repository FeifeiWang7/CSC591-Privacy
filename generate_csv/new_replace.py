import sys
import time
import json
import requests
import os
import urllib
from facepp import API, File
from is_human import is_human

API_KEY = "19e15e1bc1056ef1cf9ad76cff56b4a6"
API_SECRET = "XdoDpYtBr6DFWZPFfdPfZJiZa-TcpoWq"
api = API(API_KEY, API_SECRET)

def replace_url(inputFile,outputFile):
	fd = open(inputFile, 'r')
	wd = open(outputFile, 'w')
	wd.write(fd.readline())
	for line in fd:
		arr = line.split(',')
		if(len(arr)<11):
			wd.write(line)
			continue
		if arr[9] == "False":
			if arr[10].startswith('http', 0, 4):
				tmp = arr[10]
			  	wd.write(line.replace(arr[10],download(tmp)))
			else:
				wd.write(line)
		elif arr[9] == "True":
			wd.write(line.replace(arr[10],"default"))
		else:
			wd.write(line)
	fd.close()
	wd.close()

def download(url):
        image=urllib.URLopener()
        image.retrieve(url+"?sz=50","tmp/0.jpg")
        ret = api.detection.detect(img = File("tmp/0.jpg"))
	if ret == None:
		print "Still error"
		return url
        if 'face' in ret:
		if len(ret['face']) == 0:
			return "false"
                else:
			return "true"
	else:
		return "false"
	print "Error !!!!!!!"

if __name__ == '__main__':
	import sys
	replace_url(sys.argv[1],sys.argv[2])
