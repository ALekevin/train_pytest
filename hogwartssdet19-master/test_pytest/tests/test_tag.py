from test_pytest.api.tag import Tag


class TestTag:
    def setup_class(self):
        self.tag = Tag()

    def test_get(self):
        r = self.tag.get()
        #  直接断言外部状态码，并不明显，因为前后端很少用外部状态码做联调
        assert r.json().get('errcode') == 0

    def test_add(self, get_unique_name):
        new_tag = self.tag.add(get_unique_name).json()
        assert new_tag.get("errcode") == 0
        assert self.tag.is_in_taglist(new_tag.get("tagid"))

    def test_delete(self, get_unique_name):
        new_tag = self.tag.add(get_unique_name)
        assert self.tag.delete(new_tag.json().get("tagid")).json().get("errcode") == 0

    def test_update(self, get_unique_name):
        new_tag = self.tag.add(get_unique_name)
        assert self.tag.update(new_tag.json().get("tagid"), get_unique_name).json().get("errcode") == 0
