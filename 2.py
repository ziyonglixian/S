import random
import threading
import requests
import os

# zchfrh 
cookie = os.environ["COOKIESS2"]
headers1 = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "cookie":cookie
}
url1 = "https://www.kaixinbainian.com/home.php?mod=task&do=apply&id=2"
res1 = requests.get(url=url1,allow_redirects=False,headers=headers1).text


def q():
    m = random.randint(0, 255)
    n = random.randint(0, 255)
    x = random.randint(0, 255)
    y = random.randint(0, 255)
    ip = str(m) + "." + str(n) + "." + str(x) + "." + str(y)
    url = 'https://www.kaixinbainian.com/?fromuid=1106458'
    headers = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        "X-forwarded-for":
        str(ip),
        "Client_ip":
        str(ip),
        "cookie":
        "yj0M_5ed6_saltkey=rx9ucDZ0; yj0M_5ed6_lastvisit=1596710921; yj0M_5ed6_lastact=1596714523%09home.php%09misc; yj0M_5ed6_sendmail=1"
    }
    requests.get(url=url, headers=headers).text
    headers3 = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "cookie":cookie
    }
    url3 = "https://www.kaixinbainian.com/home.php?mod=task&do=draw&id=2"
    res3 = requests.get(url=url3,allow_redirects=False, headers=headers3).text


for i in range(55):
    t = threading.Thread(target=q)
    t.start()
