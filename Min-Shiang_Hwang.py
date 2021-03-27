import requests as req
from bs4 import BeautifulSoup


req = req.get("http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm")
req.encoding = "utf8"
if req.status_code == 200:

    soup = BeautifulSoup(req.text, "lxml")
    result1 = soup.find_all("span",lang='EN-US')

    fp = open("outHwang.text","w",encoding="utf8")
    for val in result1:
        text2 = val.text.replace('\n', '')
        print(text2)
        fp.write(text2+"\n")
    fp.close()
else:
    print("no page")