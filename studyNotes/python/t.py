import win32clipboard as w
import win32con
import requests
import sys


def translate(queryString: str)->str:
    form = {
        "from": "en",
        "to": "zh",
        "query": queryString,
        "source": "txt"
    }
    res = requests.post("https://fanyi.baidu.com/transapi", form)
    try:
        resjson = res.json()
        return resjson["data"][0]["dst"]
    except Exception:
        return None


def gettext():
    w.OpenClipboard()
    t = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return t


def settext(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()


if __name__ == "__main__":
    argv = sys.argv
    s = ''
    for i in range(1, len(argv)):
        # print(i)
        s = s+argv[i]
    res = translate(s)
    print('[res]===================')
    print(res)
    print('[已复制到剪切板]===================')
    # res = res.encode('gbk')
    settext(res)
