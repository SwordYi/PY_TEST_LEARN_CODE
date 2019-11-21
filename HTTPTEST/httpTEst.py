import requests

test_url = "http://www.163.com"
response = requests.get(test_url)

print(response.url)
print(response.status_code)
text = response.text
cookies = response.cookies
content = response.content

headers = response.headers
print(headers)
for key in headers.keys():
    print(key + ":" + headers[key])

h = {"User-Agent":"Android/H60-L01/4.4.2/"} # 实测无法返回手机版的网页，除非修改网址的www为3g才能返回
r2 = requests.get(test_url, headers = h)
print(r2.status_code)
h2 = r2.headers
print(h2)
# print(r2.text)

c = {"JSESSIONID":"C75939DF005560D83B20F43A5588FA44"}
c2 = "JSESSIONID=C75939DF005560D83B20F43A5588FA44"
test_url = "https://mail.163.com/js6/main.jsp?sid=cBEmTuriIKYLqygQwriilmEFHkLcLLHz&df=email163#module=mbox.ListModule%7C%7B%22fid%22%3A18%2C%22order%22%3A%22date%22%2C%22desc%22%3Atrue%7D"
r3 = requests.get(test_url, cookies = c )
r3 = requests.get(test_url, headers = {"cookie":c2})
print(r3.status_code)
print(r3.headers)
print(r3.text)


c = "JSESSIONID=6272E7C3762FA26619780AF615A75A0B"
test_url = "http://mail.163.com/js6/main.jsp"
p = {"sid":"xCsXkCUUCJYwVBCjouUUtnRzyRTfyHOs","df":"163nav _ icon#module=welcome.WelcomeModule%7C%7B%7D"}
response = requests.get(test_url ,headers = {"cookie":c}, params = p )
print (response.status_code)
print (response.headers)
print (response.text)