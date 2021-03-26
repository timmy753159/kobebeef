import requests as req
from bs4 import BeautifulSoup


req = req.get("http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm")
req.encoding = "utf8"
if req.status_code == 200:
    soup = BeautifulSoup(req.text, "lxml")
    result1 = soup.find_all("li")

    fp = open("outHwang.text","w",encoding="big5")
    for val in result1:
        text2 = val.text.replace('\n', '')
        text3 = text2.replace('   ', '')
        print(text3)
        fp.write(text3+"\n")
    fp.close()
else:
    print("no page")