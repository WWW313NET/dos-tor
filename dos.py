from scapy.all import *
ip = input("insert target ip: \n")
pkt=(dst=ip)/SYN()
try:
  while True:
     r=srl(pkt)
except:
   print("\nexit")
