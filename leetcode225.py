class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue1.insert(0, x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        for _ in range(len(self.queue1) - 1):
            self.queue2.insert(0, self.queue1.pop())
        res = self.queue1.pop()
        self.queue1 = self.queue2
        self.queue2 = []
        return res

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        self.queue2 = self.queue1[:]
        for i in range(len(self.queue1) - 1):
            self.queue1.pop()
        res = self.queue1[-1]
        self.queue1 = self.queue2
        self.queue2 = []
        return res

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.queue1) == 0:
            return True
        return False



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.top()
param_3 = obj.pop()
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)