import sys
import requests
from bs4 import BeautifulSoup

# request header
url = 'https://ck101.com/thread-2874564-88-1.html'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# Get the page using request
response = requests.get(url, headers=headers)
pageSource = response.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)

# Use beautifulsoup to search for article title
soup = BeautifulSoup(pageSource, "html.parser")
dlist = soup.find("div", id="postlist").find_all("td",  class_ = "t_f")
for article in dlist:	
	print(article.contents[0].strip())
