import requests as req
from bs4 import BeautifulSoup


req = req.get("http://dns2.asia.edu.tw/~jdwang/PaperList.htm")
req.encoding = "big5"
if req.status_code == 200:
    soup = BeautifulSoup(req.text, "lxml")
    result1 = soup.find_all("li")
    fp = open("outWong.text","w",encoding="big5")
    for val in result1:
        text2 = val.text.replace('\xa0', 'U')
        text2 = text2.replace('\n', '')
        print(text2)
        fp.write(text2+"\n")
    fp.close()
else:
    print("no page")