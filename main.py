import requests as req
import time
from bs4 import BeautifulSoup as soup
import re
page = 0
download_list = []
rule1 = re.compile(r'\d{6}')
url='https://wnacg.com/search'
headers={
    'user-Agent' : 'Googlebot'
}
for page in range(1,74):
    params ={
    'q':'原神',
    'f':'_all',
    's':'create_time_DESC',
    'syn':'yse',
    'p' : page
}
    r1 = req.get(url=url,headers=headers,params=params)
    print(r1.url)
    if r1.status_code != 200:
        break
    soup1 = r1.text
    soup1 = soup(soup1,"html.parser")
    l1 = soup1.body.find_all(class_='title')
    print('即将获取第'+str(page)+'页的链接')
    for i in l1:
        soup2=soup(str(i),"html.parser")
        link = soup2.a.get('href')
        link = 'https://wnacg.com/download-index-aid-' + str(rule1.findall(link)[0]) + '.html'
        title = soup2.a.get_text('title')
        download_list.append([title,link])
        print()

    for download in download_list:
        r2 = req.get(download[1],headers=headers).text
        r2 = soup(r2,"html.parser")
        r2 = r2.body.find(class_="down_btn ads")
        r2 = soup(str(r2),"html.parser")
        link = 'https:'+r2.a.get('href')
        print (link)
        with open('url.txt',mode='a+',encoding='utf-8') as file:
            file.write(link+'\n')
    download_list = []
    
    
    '''r3 =req.get (link,headers=headers)
    content =r3.content
    print(r3.status_code)
    with open('E:\\download_file',mode='wb') as file:
        file.write(content)
    print(download[0]+'下载完成')'''