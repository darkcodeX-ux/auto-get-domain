# SX ReverseIp, by Nopebee7
# Jangan recode atau di perjualbelikan. Hargai hak cipta

import re, time, random, sys, os, socket
from datetime import date
color = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m", "\033[37m", "\033[39m"]
try: import requests; s = requests.Session()
except: print("{w}Require {g}requests {w}module\n{y}pip install {g}requests".format(w=color[6], y=color[2], g=color[1]));exit()


# Default Var
output = "priv_grab.txt"
tmp = []
requests = requests.Session()

def logo():
    os.system(["clear", "cls"][os.name == 'nt'])
    Logo = '''
     ______  __      ______           __    ____ 
    / ___/ |/ /     / ____/________ _/ /_{y}by{b}/ __ \\
    \\__ \\|   /_____/ / __/ ___/ __ `/ __ \\/ / / /
   ___/ /   /_____/ /_/ / /  / /_/ / /_/ / /_/ /{w}ate
  /____/_/|_|     \\____/_/   \\__,_/_.___/_____/ {w}v1.0
  {y}nopebee7 {w}[{g}@{w}] {y}skullxploit\n'''.format(g=color[1], w=color[7], m=color[4], y=color[2], r=color[0], b=color[3])
    for Line in Logo.split('\n'):
        print(random.choice(color)+Line)
        time.sleep(0.00000001)


def opt():
    dari = raw_input(" {w}[{g}+{w}] {y}from date (Y-m-d) {w}> ".format(w=color[6], g=color[1], y=color[2]))
    if len(dari.split("-")) == 3:
    	dari = dari.split("-")
    else: 
    	print(" {w}[{b}-{w}] {y}Date Fromating Example {w}: {g}2021-3-1".format(g=color[1], w=color[7], y=color[2], b=color[3]))
    	exit()
    ke = raw_input(" {w}[{g}+{w}] {y}to date (Y-m-d) {w}> ".format(w=color[6], g=color[1], y=color[2]))
    if len(ke.split("-")) == 3:
    	ke = ke.split("-")
    else: 
    	print(" {w}[{b}-{w}] {y}Date Fromating Example {w}: {g}2021-3-1".format(g=color[1], w=color[7], y=color[2], b=color[3]))
    	exit()
    return dari, ke

def getSite (date, domain):
	global output, headers, tmp
	urlDefault = "https://domain-status.com/archives/{}/{}/registered/1".format(date, domain)
	r = requests.get(urlDefault)
	totPage = ["1"]
	if r.status_code == 200:
		if "page 1 on" in r.text:
			totPage = re.findall('page 1 on (.*?),', r.text)
		print("\n {w}[{g}+{w}] {y}Found {g}".format(w=color[7], g=color[1], y=color[2])+str(totPage[0])+" {y}page in {g}.".format(w=color[7], g=color[1], y=color[2])+domain+"\n")
		for i in range(1, int(totPage[0].encode("utf-8")) + 1):
			url = "https://domain-status.com/archives/{}/{}/registered/{}".format(date, domain, str(i))
			r = requests.get(url)
			listDomain = re.findall('<a href="https://domain-status.com/www/(.*?)">', r.text)
			res = []
			dup = []
			for site in listDomain:
				if site not in tmp:
					tmp.append(site)
					res.append(site)
					open(output, "a").write(site+"\n")
				else:
					dup.append(site)
			if dup == []:
				print(" \033[39m\033[42;1m -- "+str(len(res))+" SITES -- \033[0m ."+color[1]+domain+color[6]+" in page "+color[1]+str(i)+color[6]+"/"+color[1]+str(totPage[0]))
			else:
				print(" \033[39m\033[42;1m -- "+str(len(res))+" SITES -- \033[0m ."+color[1]+domain+color[6]+" in page "+color[1]+str(i)+color[6]+"/"+color[1]+str(totPage[0])+color[6]+" ("+color[0]+str(len(dup))+color[6]+" duplicate )")
	else:
		getSite(date, domain)

def main(sx):

	dari = date(int(sx[0][0]), int(sx[0][1]), int(sx[0][2]))
	ke = date(int(sx[1][0]), int(sx[1][1]), int(sx[1][2]) + 1)
	sx = [date.fromordinal(i) for i in range(dari.toordinal(), ke.toordinal())]
	i = 0

	while i < len(sx):
		tang = str(sx[i])
		tanggal = ""
		tang = tang.split("-")
		for t in tang:
			if len(t) < 4:
				if t.startswith("0"):
					tanggal += "-"+t.replace("0", "")
				else:
					tanggal += "-"+t
			else:
				tanggal += t
		i += 1
		print(" {w}[{b}+{w}] {y}Date {w}: {g}".format(g=color[1], w=color[7], y=color[2], b=color[3])+str(tanggal))
		def reg(date):
			try:
				r = requests.get("https://domain-status.com/archives/"+tanggal+"/")
				if r.status_code != 200:
					reg(tanggal)
				else:
					return r
			except:
				reg(tanggal)
		r = reg(tanggal)
		if "Sorry, there is no data currently available for the requested date" in r.text:
			print(" {w}[{b}-{w}] {y}Date {r}"+tanggal+" {y}Is Empty ".format(r=color[0], w=color[7], y=color[2], b=color[3]))
			continue
		else:
			dom = re.findall("<h3>.(.*?)</h3>", r.text)
			print(" {w}[{g}+{w}] {y}Found {g}".format(w=color[7], g=color[1], y=color[2])+str(len(dom))+" {y}domain {w}: {g}".format(w=color[7], g=color[1], y=color[2])+str(dom))
			for domain in dom:
				getSite(tanggal, domain)

if __name__ == "__main__":
	try:
		logo()
		sx = opt()
		main(sx)
	except KeyboardInterrupt:
		print("\n {w}[{r}-{w}] {b}Goodbye >//< ".format(w=color[6], r=color[0], b=color[3]))