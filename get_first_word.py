import json
import requests
import os
wordlist = []
def google():
        fileW = open("American", "w")
	with open('tmp', 'r') as fileR:
		for line in fileR:
			#wordlist.append(line.split(None, 1)[0]) 
			fileW.write(line.split(None, 1)[0]+'\n')
google()
