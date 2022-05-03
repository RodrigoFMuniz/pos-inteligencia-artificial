from bs4 import BeautifulSoup

soup = BeautifulSoup(
    'https://beautiful-soup-4.readthedocs.io/en/latest/#quick-start', 'html-parser')

print(soup.prettify())
