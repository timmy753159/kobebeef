import requests as req
from bs4 import BeautifulSoup


req = req.get("http://210.70.80.21/~bs109021491/")
req.encoding = "utf8"
if req.status_code == 200:
    soup = BeautifulSoup(req.text, "lxml")
    result1 = soup.find_all("li")
    fp = open("outKKK.text","w",encoding="utf8")
    for val in result1:
        text2 = val.text.replace('\n', '')
        text3 = text2.replace('   ', '')
        print(text3)
        fp.write(text3+"\n")
    fp.close()
else:
    print("no page")