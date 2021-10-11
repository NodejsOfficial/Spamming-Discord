import requests
import threading
import time
import os
# import httpx

session = requests.Session()
session.cookies.set(
    "__cfduid", "d8e0f67afb0d8f59afedb12286703f1621619603403", domain=".discord.com")
session.cookies.set(
    "__dcfduid", "518d24ca0c2440e78562b2962a77e17e", domain="discord.com")

session.headers.update({
    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkxLjAuNDQ3Mi4xMDEgU2FmYXJpLzUzNy4zNiBFZGcvOTEuMC44NjQuNDgiLCJicm93c2VyX3ZlcnNpb24iOiI5MS4wLjQ0NzIuMTAxIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjg3NzgxLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='
})

tokens = open('token.txt', 'r').read().split('\n')

os.system("title Spam message - By Nodejs")
print("Starting Spam...")

def message():                
    while True:
        for token in tokens:
            r =  session.post(url=f'https://discord.com/api/v9/channels/ใส่IDห้อง/messages',headers={'authorization': token},json={"content":"ใส่ข้อความ"})
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print("Spamming Status :", +r.status_code)
                    break
                else:
                    break

for i in range(1000):
    time.sleep(1)
    threading.Thread(target=message).start()
