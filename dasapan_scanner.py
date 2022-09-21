import pyfiglet
import sys
import socket
from datetime import datetime
def portcheck():
    begin = input("enter the port search start")
    end = int(input("enter the limit for the port search"))
    if(end<0):
        end=input("enter valid input")
    try:
        for port in range(int(begin), (end)):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(0.5)
                print("scaning port -:", port)
                result = s.connect_ex((target, port))
                if (result == 0):
                    print("open port is found", format(port))
                    openports.append(int(format(port)))

                s.close()
            except KeyboardInterrupt:
                print("\n exiting")
                print("\n ", openports)
                sys.exit()

    except KeyboardInterrupt:
        print("\n exiting")
        sys.exit()
    except socket.error:
        print("\n socket error")
    print("open ports found are ")
    print(openports)

ascii_banner = pyfiglet.figlet_format("Dasapan Scanner")
print(ascii_banner)
openports=[]
i=0
target = input(str("target Ip:"))
print('_'*50)
print("scanning started at :"+str(datetime.now()))
print('*'*50)
portcheck()
ans=1
while(ans!=0):
    ans = int(input("\npress 0 to exit or any other key to search further"))
    if (ans == 0):
        print("open ports result")
        for i in openports:
            print(i)
        exit(0)
    else:
        portcheck()





