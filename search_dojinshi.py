import requests as req
from bs4 import BeautifulSoup as soup
import re
url='https://wnacg.com/search'
headers={
    'user-Agent' : 'Googlebot'
}
rule1 = re.compile(r'\d{6}')
def search_dojinshi(url,page,name):
    download_list = []
    params ={
    'q': name,
    'f': '_all',
    's': 'create_time_DESC',
    'syn': 'yse',
    'p' : page
}
    r1 = req.get(url=url,headers=headers,params=params)
    print(r1.url)
    if r1.status_code == 200:
        soup1 = soup(r1.text,"html.parser")
        l1 = soup1.body.find_all(class_='title')
        for i in l1:
            soup2=soup(str(i),"html.parser")
            link = soup2.a.get('href')
            link = 'https://wnacg.com/download-index-aid-' + str(rule1.findall(link)[0]) + '.html'
            download_list.append(link)
            print(soup2.a.get_text('title'))
        return download_list

if __name__ == '__main__':
    l1 = search_dojinshi(url=url,page=1)
    print(l1)