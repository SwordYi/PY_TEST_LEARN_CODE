import requests

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/55.0.2883.87 Safari/537.36"}
test_url = "https://www.zhihu.com/"
r = requests.get(test_url, headers=headers)
print(r.status_code)
print(r.headers)
print(r.text)