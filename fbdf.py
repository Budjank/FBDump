import requests, json, os, sys

class warna:
    ungu = '\033[95m'
    biru = '\033[94m'
    hijau = '\033[92m'
    oren = '\033[93m'
    merah = '\033[91m'

def dump():
    print warna.hijau+"""
    ######{>>> FB Dump <<<}######
    #####    #          #   #####
    ####      #        #     ####
    ###        #      #       ###
    ##          #    #         ##
    #            #  #           #
    #############################
    """
    print warna.merah+"""
    [1] ID
    [2] Username
    [3] Email
    [4] Phone Number
    [5] Bio
    [6] Website
    [7] ID,Bio,Website
    [8] Username,Email,Phone Number
    """
    pilih=raw_input(warna.biru+"Pilih Cok : ")
    token=raw_input(warna.biru+"Input Token : "+warna.oren+"")
    r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
    a = json.loads(r.text)
    print ""
    for i in a['data']:
        x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
        y = json.loads(x.text)
        try :
            print warna.hijau+"<[=====   INFORMATION FROM FRIEND    =====]>"
            if pilih == "1":
                print warna.oren+"""
                [*] Name         : """+y['name']+"""
                [*] Id           : """+y['id']+"""
                """
            elif pilih == "2":
                print warna.oren+"""
                [*] Name         : """+y['name']+"""
                [*] Username     : """+y['username']+"""
                """
            elif pilih == "3":
                print warna.oren+"""
                [*] Name         : """+y['name']+"""
                [*] Email        : """+y['email']+"""
                """
            elif pilih == "4":
                print warna.oren+"""
                [*] Name         : """+y['name']+"""
                [*] Phone Number : """+y['mobile_phone']+"""
                """
            elif pilih == "5":
                print warna.oren+"""
                [*] Name         : """+y['name']+"""
                [*] Bio          : """+y['bio']+"""
                """
            elif pilih == "6":
                print warna.oren+"""
                [*] Name         : """+y['name']+"""
                [*] Website      : """+y['website']+"""
                """
            elif pilih == "7":
                print warna.oren+"""
                [*] Name         : """+y['name']+"""
                [*] Id           : """+y['id']+"""
                [*] Bio          : """+y['bio']+"""
                [*] Website      : """+y['website']+"""
                """
            elif pilih == "8":
                print warna.oren+"""
                [*] Name         : """+y['name']+"""
                [*] Username     : """+y['username']+"""
                [*] Email        : """+y['email']+"""
                [*] Phone Number : """+y['mobile_phone']+"""
                """
        except KeyError:
            pass
###########################
dump()
