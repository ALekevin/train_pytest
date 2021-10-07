# 饿汉式单例
class IdMaker:
    _instance = None
    _id = -1

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_id(self):
        self._id += 1
        return self._id


def test_id_maker():
    # IdMaker 是单例类，只允许有一个实例

    id1 = IdMaker().get_id()

    id2 = IdMaker().get_id()

    id3 = IdMaker().get_id()

    print(id1, id2, id3)


if __name__ == "__main__":
    test_id_maker()

# 0 1 2
# 饱汉式单例
from threading import Lock


class IdMaker:
    _lock=Lock()
    _instance = None
    _id = -1

    def __new__(cls, *args, **kwargs):
        raise ImportError("Instantition is not allowed")

    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def get_id(self):
        self._id += 1
        return self._id


def test_id_maker():
    # IdMaker 是单例类，只允许有一个实例

    id1 = IdMaker.get_instance().get_id()

    id2 = IdMaker.get_instance().get_id()

    id3 = IdMaker.get_instance().get_id()

    print(id1, id2, id3)


if __name__ == "__main__":
    test_id_maker()
