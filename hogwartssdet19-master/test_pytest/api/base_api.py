import requests


# 把常量放到类变量中

class BaseApi:
    CORPID = "wwe653983e4c732493"
    CORPSECRET = "T72_Vgw9TaNS-FLDU2gJlw6AteerMXsuMval9kGNZbc"
    BASE_URL = "https://qyapi.weixin.qq.com/cgi-bin/"

    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        """
        获取 token
        :return:
        """
        url = self.BASE_URL + f"/gettoken?corpid={self.CORPID}&corpsecret={self.CORPSECRET}"
        r = requests.get(url)
        return r.json().get("access_token")

    def send(self, method, url, **kwargs):
        """
        封装发送请求
        :param method: 请求方式
        :param url: 路由地址
        :param kwargs: 其它参数
        :return:
        """
        # post 和 get 底层实现，requests.get == requests.request("GET",)
        url = self.BASE_URL + url
        return requests.request(method, url, **kwargs)
