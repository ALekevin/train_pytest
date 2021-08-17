import requests


def test_post_httpbin():
    proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}
    url = 'https://httpbin.testing-studio.com/post'
    data = {
        "name": "zhangshan",
        "age": 21
    }
    ret = requests.post(url=url, data=data, proxies=proxies, verify=False)
    print(ret.text)
