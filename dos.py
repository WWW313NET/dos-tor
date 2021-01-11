from scapy.all import *
ip = input("insert target ip: \n")
pkt=IP(dst=ip)/SYN()
try:
  while True:
     r=srl(pkt)
except:
   print("\nexit")
