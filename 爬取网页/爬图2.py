#导入模块
import requests
from bs4 import BeautifulSoup
from urllib import request
#找网址
url='http://pic.netbian.com/4kdongman/index_2.html'
res =requests.get(url)
res.encoding='gbk'
html=BeautifulSoup(res.text,'html.parser')
#检查 找到图片所在的列表，并找到列表的类名
parent=html.find('ul',class_='clearfix')
#找到列表中的图片
images=parent.find_all('img')


def PaTu():
    for each in images:
        #找到图片的网址
        img_url='http://pic.netbian.com'+each.attrs['src']
        #print(img_url)
        name=each.attrs['alt']
        #print(name)
        #将图片存到images文件夹中
        request.urlretrieve(img_url,f'爬图/{name}.jpg')


#创建本地保存文件夹，并下载保存图片
if __name__ == '__main__':
    PaTu()

