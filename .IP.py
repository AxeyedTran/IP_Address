#=====DEV:Axeyedkha=====#
#!/usr/bin/python
#=====get source code must write author=====#
#=====Setting=====#
import os, sys, time
import requests
from time import sleep
#======Color======#
d = '\033[1;91m'
xl = '\033[1;92m'
v = '\033[1;93m'
xb = '\033[1;96m'
t = '\033[1;97m'
#=====Logo && Banner=====#
banner = '''
\033[1;96m   	██╗ ██████╗ 
\033[1;92m   	██║ ██╔══██╗   
\033[1;97m   	██║ ██████╔╝ 
\033[1;93m   	██║ ██╔═══╝ Find IP With API  
\033[1;96m  	██║ ██║    Dev: Axeyed Tran  
\033[1;92m   	╚═╝ ╚═╝    IP Address Finder
\033[1;97m         		Version: 1.1.0
\033[1;97m────────────────────────────────────────────────────────────────────
\033[1;96m      Facebook: Axeyed Tran
\033[1;92m      Github: AXEYEDKHA
\033[1;93m      Remember: Follow Me on Github
\033[1;97m────────────────────────────────────────────────────────────────────
\033[1;97m      ['''+xl+'''1'''+t+''']'''+xb+''' FIND IP
\033[1;97m      ['''+xl+'''2'''+t+''']'''+xb+''' YOUR IP
\033[1;97m      ['''+xl+'''3'''+t+''']'''+xb+''' EXIT
\033[1;97m────────────────────────────────────────────────────────────────────
'''
f = '\033[1;97m────────────────────────────────────────────────────────────────────'
banner2 = '''
\033[1;96m   	██╗ ██████╗ 
\033[1;92m   	██║ ██╔══██╗   
\033[1;97m   	██║ ██████╔╝ 
\033[1;93m   	██║ ██╔═══╝ Find IP With API  
\033[1;96m  	██║ ██║    Dev: Axeyed Tran  
\033[1;92m   	╚═╝ ╚═╝    IP Address Finder
\033[1;97m         		Version: 1.1.0
\033[1;97m────────────────────────────────────────────────────────────────────
\033[1;96m      Facebook: Axeyed Tran
\033[1;92m      Github: AXEYEDKHA
\033[1;93m      Remember: Follow Me on Github
\033[1;97m────────────────────────────────────────────────────────────────────
'''
#======write======#
def write(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.0001)
#=====Exit=====#
def exit():
	os.system('clear')
	print(banner2)
	print(v+'Thank You Used My Tool.')
	print(xb+'Axeyed Tran:'+xl+' BYE BYE !!')
	os.sys.exit()
#=====Tool_Main_Function=====#
def main():
    os.system("clear")
    print(banner)
    es = input(t+'['+xl+'?'+t+']'+xb+' Choose Option:'+v)
    if es == '1' or es == '01':
        os.system('clear')
        print(banner2)
        ip = input(t+'['+xl+'?'+t+']'+xb+' Type IP You Want Find:'+v)
        request = requests.get(f'http://ip-api.com/json/{ip}')
        json_api = request.json()
        if 'message' not in json_api:
            nati = json_api['country']
            sta = json_api['regionName']
            city = json_api['city']
            tg = json_api['timezone']
            ips = json_api['isp']
            rIP = json_api['query']
            os.system('clear')
            print(banner2)
            print('Result Here !\n')
            write(xb+'IP: '+rIP)
            write(xl+'National: '+nati)
            write(t+'State: '+sta)
            write(v+'City: '+city)
            write(xl+'Longitude: {}'.format(json_api['lon']))
            write(t+'Latitude: {}'.format(json_api['lat']))
            write(v+'Timezone: '+tg)
            write(xl+'Provedor: '+ips)
        else:
            print('\n\033[1;91mIP INVALID\n')
        print(f)
        print(t+'Do you want return menu? [y/n]')
        sair = input(xb+'[</>]:'+xl)
        if sair == 'n' or sair == 'N':
            exit()
        else:
            main()
    elif es == '2' or es == '02':
        os.system('clear')
        print(banner2)
        request = requests.get('http://ip-api.com/json/?')
        json_api = request.json()
        nati = json_api['country']
        sta = json_api['regionName']
        city = json_api['city']
        tg = json_api['timezone']
        ips = json_api['isp']
        rIP = json_api['query']
        os.system('clear')
        print(banner2)
        print('Result Here !\n')
        write(xb+'IP: '+rIP)
        write(xl+'National: '+nati)
        write(t+'State: '+sta)
        write(v+'City: '+city)
        write(xl+'Longitude: {}'.format(json_api['lon']))
        write(t+'Latitude: {}'.format(json_api['lat']))
        write(v+'Timezone: '+tg)
        write(xl+'Provedor: '+ips)
        print(f)
        print(t+'Do you want return menu? [y/n]')
        sair = input(xb+'[</>]:'+xl)
        if sair == 'n' or sair == 'N':
            exit()
        else:
            main()
    elif es == '3' or es == '03':
        exit()
    else:
        os.system('clear')
        print('\033[1;91m INVALID OPTION !')
        sleep(2)
        main()
#=====Main=====#
#====RUNTOOL====#
main()
#=====REMEMBER: FOLLOW ME IN GITHUB====#
#=====WARRNING====#
#=====Author: Axeyed Tran=====#
#=====get source code must write author=====#