import requests

res = requests.get("https://github.com/favicon.ico")
print(res.text)
print(res.content)
with open('favicon.ico','wb') as favicon:
	favicon.write(res.content)
with open('favicon.ico') as exp:
	print(exp.read())