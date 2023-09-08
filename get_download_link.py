import requests as req
from bs4 import BeautifulSoup as soup
headers={
    'user-Agent' : 'Googlebot'
}
def get_donwload_link(url):
    r = req.get(url=url,headers=headers)
    soup2 = soup(r.text,"html.parser")
    soup2 = soup2.body.find(class_="down_btn ads")
    soup2 = soup(str(soup2),"html.parser")
    link = 'https:' + soup2.a.get('href')
    print (link)
    return link

if __name__ == '__main__':
    get_donwload_link('https://wnacg.com/download-index-aid-219344.html')