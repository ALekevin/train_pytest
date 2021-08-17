from test_pytest.api.base_api import BaseApi

"""
1. 测试接口放到类中，可以让其它方法进行复用
2. 便于统一处理，重复逻辑可以提取复用
3. 建议把必填参数放到函数的参数中，非必填放到 kwargs 中
4. 把base url封装到父类中
"""


class Tag(BaseApi):

    def add(self, tagname, **kwargs):
        """
        添加标签
        :param tagname: 标签名
        :param kwargs: (tagid：默认会自动生成）
        :return:
        """
        data = {
            "tagname": tagname,
        }
        # 把其它非必填参数更新到数据中
        data.update(kwargs)
        r = self.send("POST", f"tag/create?access_token={self.token}", json=data)
        return r

    def delete(self, tagid):
        """
        删除 tag
        :type tagid: 标签id
        :return:
        """
        r = self.send("GET", f"tag/delete?access_token={self.token}&tagid={tagid}")
        return r

    def update(self, tagid, tagname):
        """
        tag 更新
        :param tagid:
        :param tagname:
        :return:
        """
        data = {
            "tagid": tagid,
            "tagname": tagname
        }
        r = self.send("POST", f"tag/update?access_token={self.token}", json=data)
        return r

    def get(self):
        """
        获取所有 tag
        :return:
        """
        r = self.send("GET", f"tag/list?access_token={self.token}")
        # 返回 r ，而不是 r.json()
        return r

    def is_in_taglist(self, tag_id):
        """
        判断 tag_id 是否在 taglist 中
        :param tag_id:
        :return:
        """
        tag_list = self.get().json().get("taglist")
        for tag in tag_list:
            if tag_id == tag.get("tagid"):
                return True
        return False
