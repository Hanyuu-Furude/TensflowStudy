import requests

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


if __name__ == "__main__":
    print(translate("php is the best programming language"))
