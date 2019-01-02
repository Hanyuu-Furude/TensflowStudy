import requests
import re
headers = \
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) \
        Gecko/20100101 Firefox/64.0'
    }
res = requests.get('https://www.zhihu.com/explore', headers=headers)
# print(res.text)
print(res.content)
print(res.text)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)

titles = re.findall(pattern, res.text)
# print(titles)
for i in titles:
    print(i.replace('\n', ''))
