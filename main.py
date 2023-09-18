import requests as req
from bs4 import BeautifulSoup as soup
import re
import colorama
url='https://wnacg.com/search'
headers={
    'user-Agent' : 'Googlebot'
}
name=''
rule1 = re.compile(r'aid-\d*')
def clean_filename(filename):
    # 使用正则表达式将无效字符替换为空字符串
    cleaned_filename = re.sub(r'[\/:*?"<>|]', '', filename)
    return cleaned_filename
def search_dojinshi(url,page,name):
    download_list = []
    if page == 1:
        params ={
        'q': name,
        'f': '_all',
        's': 'create_time_DESC',
        'syn': 'yse',
        }
    else:
        params ={
        'q': name,
        'f': '_all',
        's': 'create_time_DESC',
        'syn': 'yse',
        'p' : page
        }
    r1 = req.get(url=url,headers=headers,params=params)
    print(colorama.Fore.CYAN+r1.url)
    if r1.status_code == 200:
        soup1 = soup(r1.text,"html.parser")
        l1 = soup1.body.find_all(class_='title')
        for i in l1:
            soup2=soup(str(i),"html.parser")
            link = soup2.a.get('href')  
            wildcard = rule1.findall(link)[0][4::]
            link = 'https://wnacg.com/download-index-aid-' + str(wildcard) + '.html'
            download_list.append(link)
        print(download_list)
        return download_list

def get_download_link(url):
    r = req.get(url=url,headers=headers)
    soup2 = soup(r.text,"html.parser")
    soup2 = soup2.body.find(class_="down_btn ads")
    soup2 = soup(str(soup2),"html.parser")
    link = 'https:' + soup2.a.get('href')
    print (colorama.Fore.RED+link)
    return link

def downloader(name):
    for page in range(1,1000):
        try:
            links = search_dojinshi(url=url,page=page,name=name)
            for web_link in links:
                link = get_download_link(web_link)
                r3 =req.get (link,headers=headers)
                content =r3.content 
                if r3.status_code == 200:
                    print(clean_filename(link[69::]))
                    with open(clean_filename(link[69::])+'.zip',mode='wb') as file:
                        file.write(content)
                    print(colorama.Fore.GREEN+'下载完成')
                else:
                    print('下载失败，状态码:'+str(r3.status_code))
        except:
            continue
            print('出现错误')
        else:
            break

if __name__ == '__main__':
    name = input('请输入关键词:')
    downloader(name)
