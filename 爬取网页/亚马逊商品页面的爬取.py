import requests
ur1 = "https://www.amazon.cn/dp/B0771D8G6L/ref=sr_1_2?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&dchild=1&keywords=%E8%AE%BA%E6%8C%81%E4%B9%85%E6%88%98&qid=1611236619&sr=8-2"
try:
    #kv ={ 'user-agent' : ' Mozilla/76.0 '}
    r=requests.get(ur1)
    #print("1")
    r.raise_for_status ()
    a=r.text[0:1000]
    b=r.text[1000:2000]
    print(a)
except:
    print("爬取失败")