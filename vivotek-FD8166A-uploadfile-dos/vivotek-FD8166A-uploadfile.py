import requests

url = "http://192.168.1.107/cgi-bin/admin/update_lens.cgi?choose_lens=2;ls;34"
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