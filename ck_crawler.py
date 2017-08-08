import requests
import sys


# headers = {
# 	"Cookie:ASP.NET_SessionId" : "5g0zw3vgkiltrc3hy5kcrxsp"
# 	"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) Chrome/59.0.3071.115 Safari/537.36"
# 	"Button1" : "登入"
# 	"txt_ac" : "王天郁",
# 	"txt_pwd" : "7464"
# }
# ses = requests.session()
# res = requests.post('http://172.28.12.15/login.aspx', headers = headers)
# print(res.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))

from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome()  # PhantomJs
driver.get('https://ck101.com/thread-2874564-88-1.html')  # 輸入範例網址，交給瀏覽器 
pageSource = (driver.page_source).encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)  # 取得網頁原始碼
driver.close()
soup = BeautifulSoup(pageSource, "html.parser")
dlist = soup.find("div", id="postlist").find_all("td",  class_ = "t_f")
for article in dlist:
	print(article.contents[0].strip())
	# article.string

# with open("ck.txt", "w") as ck:
# 	ck.write(soup)

# driver.close()  # 關閉瀏覽器

# res = requests.get("https://ck101.com/forum-237-1.html")
# print(res.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))

