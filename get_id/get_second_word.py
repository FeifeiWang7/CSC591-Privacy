import json
import requests
import os
import re
def google():
        fileW = open("French", "w")
	with open('tmp', 'r') as fileR:
		for line in fileR:
			splitted = line.split('\t')
			fileW.write(splitted[1])	
google()
