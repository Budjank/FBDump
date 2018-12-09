import requests, json, os, sys

class warna:
    ungu = '\033[95m'
    biru = '\033[94m'
    hijau = '\033[92m'
    oren = '\033[93m'
    merah = '\033[91m'

def dump():
    token=raw_input(warna.biru+"Input Token : "+warna.oren+"")
    r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
    a = json.loads(r.text)
    print ""
    for i in a['data']:
        x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
        y = json.loads(x.text)
        try :
            print warna.hijau+"<[=====   INFORMATION FROM FRIEND    =====]>"
            print warna.oren+"""
            [*] Name         : """+y['name']+"""
            [*] Id           : """+y['id']+"""
            [*] Username     : """+y['username']+"""
            [*] Email        : """+y['email']+"""
            [*] Phone Number : """+y['mobile_phone']+"""
            """
        except KeyError:
            pass
###########################
dump()
