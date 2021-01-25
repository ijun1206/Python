'''
@Date    : 2021-01-25 22:18
@Author  : WangChanJuan
@Email   : 1284522005@qq.com
@Link    :
@Description: 定向爬虫实列-2020中国大学排名
'''

import  requests
from bs4 import BeautifulSoup
import bs4
import re
def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("未获得HTML文本信息")
        return ""

def fillUnivList(ulist,html):
    html1 = re.sub('<!--.*?>', "", html).replace('\n', "")  # 正则表达式去掉注释、换行
    soup = BeautifulSoup(html1,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            tds1 = tr('a')
            #if len(tds) > 2:
            ulist.append([tds[0].string, tds1[0].string, tds[2].string, tds[4].string])


def printUnivList(ulist,num):
    tplt = "{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}"  # {1:{4}^10} 1表示位置，{4}表示用第4个参数来填充，^表示居中，10表示占10个位置
    print(tplt.format("排名", "学校名称", "所属省市", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        if u[2] is None:
           u[2] = 'None'
        print("{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^20}".format(u[0].strip(), u[1].strip(), u[2].strip(), u[3].strip(), chr(12288)))

def main():
    unifo = []
    url = 'http://www.shanghairanking.cn/rankings/bcur/2020'
    html = getHTMLText(url)
    fillUnivList(unifo,html)
    printUnivList(unifo,40)     #40个大学

if __name__ == '__main__':
    main()

