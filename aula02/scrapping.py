import requests
from bs4 import BeautifulSoup

page = requests.get('http://slacksite.com/other/ftp.html')
soup = BeautifulSoup(page.text, 'html-parser')

print(soup.prettify())
