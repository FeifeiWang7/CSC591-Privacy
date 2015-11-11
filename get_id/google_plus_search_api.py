import json
import requests
import os
API_KEY=os.environ.get("GOOGLE_API_KEY")
def google():
    for root, dirs, files in os.walk("names/"):
        for name in files:
            print name
            fileR = open("names/"+name, "r")
            fileW = open("ids/"+name, "w")
            while 1:
                line = fileR.readline()
	        if not line:
	            break
                url = "https://www.googleapis.com/plus/v1/people?query="+line+"&key="+API_KEY
                r = requests.get(url)
                if r.status_code == 200 :
	            if 'items' in r.json():
	                for person in r.json()['items']:
		            fileW.write(person['id'].encode('utf-8') + "\t" + person['displayName'].encode('utf-8') + "\n")
                    else:
                        print r
	    fileR.close()
	    fileW.close()
google()
