import json
import requests
import os
from types import *
def generateCSV():
    f=open("input.txt",'r')
    wr=open("output.csv",'a')
    API_KEY=os.environ.get("GOOGLE_API_KEY")
    param={
        "user_id":' ',
        "url":' ',
        "display_name":' ',
        "last_name": ' ',
        "first_name": ' ',
        "gender":' ',
        "image_url": ' ',
        "image_is_default":' ',
        "birthday":' ',
        "about_me":' ',
        "relationship":' ',
        'org1':' ',
        'org2':' ',
        'org3':' ',
        'isPlusUser':' ',
        'verified':' ',
        'circledByCount':' ',
        'place1':' ',
        'place2':' ',
        'place3':' ',
        'age_min':' ',
        'age_max': ' ',
        'language':' ',
        'emails':' ',
        'occupation':' ',
        'skills':' '
    }
    title=""
    for i in sorted(param.keys()):
        title=title+i+","
    wr.write(title+"\n")
    import pdb
    for line in f:
        param=param.fromkeys(param, ' ')
        userid=line[:-1]
        url = "https://www.googleapis.com/plus/v1/people/"+str(userid)+"?key="+API_KEY
        r = requests.get(url)
        if r.status_code == 200 :
            w=r.json()
            try:
                # print w
                if w.has_key('id'):
                    param['user_id']=w['id']
                if w.has_key('url'):
                    param['url']=w['url']
                if w.has_key('displayName'):
                    param['display_name']=w['displayName']
                if w.has_key('name'):
                    param["last_name"]=w["name"]["familyName"]
                    param["first_name"]=w["name"]["givenName"]
                if w.has_key('gender'):
                    param['gender']=w['gender']
                if w.has_key('image'):
                    param['image_url']=w['image']['url']
                    param["image_is_default"]=w['image']['isDefault']
                if w.has_key('birthday'):
                    param["birthday"]=w['birthday']
                if w.has_key('about_me'):
                    param["about_me"]=w['aboutMe']
                if w.has_key('relationshipStatus'):
                    param["relationship"]=w['relationshipStatus']
                if w.has_key('verified'):
                    param["verified"]=w['verified']
                if w.has_key('isPlusUser'):
                    param["isPlusUser"]=w['isPlusUser']
                if w.has_key('circledByCount'):
                    param["circledByCount"]=w['circledByCount']
                if w.has_key('organizations'):
                    num=min(len(w['organizations']),3)
                    keys=["org1","org2","org3"]
                    for i in range(num):
                        orgdict=w['organizations'][i]
                        if orgdict.has_key('name')==False:
                            continue
                        origin=orgdict['name']
                        origin=origin.replace(',','/');
                        origin=origin.replace('.','/')
                        param[keys[i]]=origin
                if w.has_key('placesLived'):
                    num=min(len(w['placesLived']),3)
                    keys=["place1","place2","place3"]
                    for i in range(num):
                        origin=w['placesLived'][i]['value']
                        origin=origin.replace(',','/');
                        origin=origin.replace('.','/')
                        param[keys[i]]=origin
                if w.has_key('ageRange'):
                    param["age_min"]=w['ageRange']['min']
                    param["age_max"]=w['ageRange']['max']
                if w.has_key('language'):
                    param['language']=w['language']
                if w.has_key('emails'):
                    param['emails']=w['emails']
                if w.has_key('occupation'):
                    occu=w['occupation']
                    occu=occu.replace(',','/')
                    occu=occu.replace('.','/')
                    param['occupation']=occu
                if w.has_key('skills'):
                    skill=w['skills']
                    skill=skill.replace(',','/')
                    skill=skill.replace('.','/')
                    param['skills']=skill
                # print param
                content=""
                for key in param.keys():
                    if type(param[key]) is UnicodeType:
                        param[key]=param[key].encode('utf8')
                for i in sorted(param.keys()):
                    content=content+str(param[i])+","
                wr.write(content+"\n")
            except Exception,e:
                # pdb.set_trace()
                print e
                print w
                continue
        else:
            print r

            
    f.close()
    wr.close()
if __name__ == '__main__':
    generateCSV()
