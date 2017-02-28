from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.instagram.com/tridhac/'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

containers = containers = page_soup.findAll("div", {"class": "_jjzlb"})


for i in range(0, len(containers)):
    container = containers[i]

    print(container.img['src'])
    print("\n")
