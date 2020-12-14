from scapy.all import *
ip = input("insert target ip: \n")
try:
  while True:
     sendp(ip)
except:
   print("\nexit")
