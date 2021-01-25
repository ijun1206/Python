'''
import requests
import os
url = "https://www.pexels.com/photo/4492524/download/"
root = "H://本地磁盘（D：）//Python//Projects//Project-1//爬取下载的文件"
#path = root + url.split('/')[-1]
try:
    r = requests.get(url)
    requests.urlretrieve(url,root)
    print("成功")
except:
    print("爬取失败")
'''

import requests
import os
#url="http://img0.dili360.com/ga/M00/48/F7/wKgBy1llvmCAAQOVADC36j6n9bw622.tub.jpg"
def httpimg(url):
    root='H://本地磁盘（D：）//Python//Projects//Project-1//爬取下载的文件//'
    path=root+url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r=requests.get(url)
            r.raise_for_status()
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
                print('文件保存成功')
        else:
            print('文件已存在')
    except:
        print('爬取失败')
if __name__=="__main__":
    url=input("url = ")
    print(httpimg(url))