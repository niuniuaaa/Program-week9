from collections import deque


class Stack:
    '''实现栈结构，先进后出'''

    def __init__(self):
        self.items = deque()

    def push(self, val):
        return self.items.append(val)

    def pop(self):
        return self.items.pop()

    def top(self):  # 返回栈顶值，双端队列右边作为栈顶
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0


class MyQueue:
    '''使用栈实现队列操作'''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.s2.empty():  # 只要栈s2不为空直接返回栈s2中元素
            return self.s2.pop()
        while not self.s1.empty():  # 将栈s1的元素转到s2中
            val = self.s1.pop()
            self.s2.push(val)
        return self.s2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.s2.empty():
            return self.s2.top()
        while not self.s1.empty():
            val = self.s1.pop()
            self.s2.push(val)
        return self.s2.top()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.s1.empty() and self.s2.empty()


def test():  # 我自己写的本地测试代码，可以不要
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.pop())
    print(q.pop())
    print(q.pop())


test()