import requests
def httpid(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return (r.text)
    except:
        print("爬取失败")
if __name__ == "__main__":
    a = input("要查询的IP: ")
    url = 'https://m.ip138.com/iplookup.asp?ip=' + a
    print(httpid(url))