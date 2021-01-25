import requests
keyword = 'Python'
try:
    kv = {'wd':keyword}
    kt = {'wd': keyword}
    r1 = requests.get("https://www.baidu.com/s",params = kv)        #227
    r2 = requests.get('http://www.baidu.com/s', params=kt)          #589351
    print(r1.request.url)
    print(r2.request.url)
    r1.raise_for_status()
    r2.raise_for_status()
    print(len(r1.text))
    print(len(r2.text))
except:
    print("搜素失败")

