import os 
os.system("systemctl restart tor")
os.system("proxychains4 python3 dos.py")
