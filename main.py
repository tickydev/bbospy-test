import requests
import os

rps = 250
time = 1000

L7 = "L7"
L4 = "L4"



os.system("clear")
print("\033[1;32;40m #-&&-------------&&--#\n")
print("\033[1;32;40m #---&&---------&&----#\n")
print("\033[1;32;40m #-----&&-----&&------#\n")
print("\033[1;32;40m #-------&&-&&--------#\n")
print("\033[1;32;40m #---------&----------#\n")
print("\033[1;32;40m #-------&&-&&--------#\n")
print("\033[1;32;40m #-----&&-----&&------#\n")
print("\033[1;32;40m #---&&---------&&----#\n")
print("\033[1;32;40m #-&&-------------&&--#\n")
print("\033[1;32;40m #----DERAW-SCRIPT----#\n")

mode = input(" L4 / L7 : ")
if mode = L7:
  url = input(" Enter url : ")
  for rps range(time):
    sender = requests.get(url)
    print("Response code: ", sender.status_code")

elif mode = L4:
  ip = input(" Enter ip : ")
  port = input(" Enter port : ")
  exit()



