# 普通队列
class Queue:
    def __init__(self, capacity):
        self.n = capacity
        self.items = [-1] * capacity
        self.head = 0
        self.tail = 0

    def enqueue(self, data):
        if self.tail == self.n:
            return False
        self.items[self.tail] = data
        self.tail += 1
        return True

    def dequeue(self):
        if self.head == self.tail:
            return False
        value = self.items[self.head]
        self.head += 1
        return value


def test_queue():
    a = Queue(10)
    a.enqueue("10")
    a.enqueue("20")
    deque_item = a.dequeue()
    assert deque_item == "10"
    a.enqueue("30")
    assert a.items[a.head] == "20"
    assert a.items[a.tail - 1] == "30"


if __name__ == "__main__":
    test_queue()

#优化队列
class Queue:
    def __init__(self, capacity):
        self.n = capacity
        self.items = [-1] * capacity
        self.head = 0
        self.tail = 0

    def enqueue(self, data):
        if self.tail == self.n:
            if self.head == 0:
                return False
            for i in range(self.head, self.tail):
                self.items[i - self.head] = self.items[i]
            self.tail -= self.head
            self.head = 0
        self.items[self.tail] = data
        self.tail += 1
        return True

    def dequeue(self):
        if self.head == self.tail:
            return False
        value = self.items[self.head]
        self.head += 1
        return value


def test_queue():
    a = Queue(3)
    a.enqueue("10")
    a.enqueue("20")
    a.enqueue("30")
    result = a.enqueue("40")
    assert not result
    deque_item = a.dequeue()
    assert deque_item == "10"
    a.enqueue("30")
    assert a.items[0] == "20"
    assert a.items[2] == "30"


if __name__ == "__main__":
    test_queue()

# 循环队列
class Queue:
    def __init__(self, capacity):
        self.n = capacity
        self.items = [-1] * capacity
        self.head = 0
        self.tail = 0

    def enqueue(self, data):
        if (self.tail + 1) % self.n == self.head:
            return False
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n
        return True

    def dequeue(self):
        if self.head == self.tail:
            return None
        value = self.items[self.head]
        self.head = (self.head + 1) % self.n
        return value


def test_queue():
    a = Queue(3)
    a.enqueue("10")
    a.enqueue("20")
    result = a.enqueue("30")
    assert not result
    a.dequeue()
    a.enqueue("30")
    assert a.items[2] == "30"
    result = a.enqueue("10")
    assert not result


if __name__ == "__main__":
    test_queue()
# 链式队列

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    def enqueue(self,item):
        if self.tail is None:
            new_node=self.node(item)
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=self.node(item)
            self.tail=self.tail.next

    def dequeue(self):
        if self.head is None:
            return None
        else:
            value=self.head.data
            self.head=self.head.next
        return value

    class node:
        def __init__(self,data):
            self.data=data
            self.next=None

def test_queue():
    a = Queue()
    a.enqueue("10")
    a.enqueue("20")
    a.enqueue("30")
    deque_item = a.dequeue()
    assert deque_item == "10"
    assert a.head.data == "20"
    assert a.head.next.data == "30"


if __name__ == "__main__":
    test_queue()
