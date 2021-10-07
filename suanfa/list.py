class Array:
    def __init__(self, capacity):
        self.data = ['x'] * capacity
        self.count = 0
        self.n = capacity

    def insert(self, location, value):
        if self.count == self.n:
            return False
        if location < 0 or location > self.count:
            return False
        for i in range(self.count, location, -1):
            self.data[i] = self.data[i - 1]
        self.data[location] = value
        self.count += 1
        return self.data

    def find(self, location):
        if location < 0 or location >= self.count:
            return -1
        return self.data[location]

    def delete(self, location):
        if location < 0 or location >= self.count:
            return False
        for i in range(location + 1, self.count):
            self.data[i - 1] = self.data[i]
        self.count -= 1
        return self.data


def test_demo():
    array = Array(5)
    print(array.insert(0, 1))
    print(array.insert(0, 2))
    print(array.insert(1, 3))
    print(array.insert(2, 4))
    print(array.insert(4, 5))
    print(array.delete(4))
    print(array.delete(3))
    print(array.delete(2))
    # 判断插入不成功
    assert not array.insert(0, 100)
    assert array.find(0) == 2
    assert array.find(2) == 4
    assert array.find(4) == 5
    assert array.find(10) == -1
    assert array.count == 5
    removed = array.delete(4)
    print(removed)
    assert removed
    assert array.find(4) == -1
    removed = array.delete(10)
    assert not removed
    # 2 3 4 1 5
    assert array.data == [2, 3, 4, 1, 5]


if __name__ == '__main__':
    test_demo()