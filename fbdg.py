import requests, json, os, sys

class warna:
    ungu = '\033[95m'
    biru = '\033[94m'
    hijau = '\033[92m'
    oren = '\033[93m'
    merah = '\033[91m'

def dump():
    token=raw_input(warna.biru+"Input Token : "+warna.oren+"")
    r = requests.get('https://graph.facebook.com/me/groups?access_token='+token).text
    a = json.loads(r)
    print ""*40
    for i in a['data']:
        print warna.hijau+"<[=====   INFORMATION FROM GROUPS    =====]>"
        print warna.oren+"""
        [*] Name         : """+i['name']+"""
        [*] Id           : """+i['id']+"""
        [*] Privacy      : """+i['privacy']+"""
        """
        m=requests.get('https://graph.facebook.com/'+i['id']+'/members?fields=id&limit=9999999&access_token='+token).text
        n = json.loads(m)
        h = []
        try:
            for j in n['data']:
                print """
                ID """+n['id']+"""
                """
                h.append(n['id'])
        except:
            pass
###########################
dump()
