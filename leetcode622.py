#--coding:utf-8--
# Author: Allen Lv
# Version: python 3.8

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue.append(value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        del self.queue[0]
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[0]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[-1]

    def isEmpty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False

    def isFull(self) -> bool:
        if len(self.queue) == self.size:
            return True
        return False

def doTest(action: list, param: list):
    n = len(action)
    if n != len(param):
        raise IndexError
    p = MyCircularQueue(3)
    for i in range(1, n):
        code = "print(p.{}({}))".format(action[i], pa[0] if (pa := param[i]) != [] else "")
        try:
            exec(code)
        except:
            print(code)
            a = input("-------stop------")

if __name__ == "__main__":
    action = ["MyCircularQueue","enQueue","enQueue",
        "enQueue","enQueue","Rear","isFull",
        "deQueue","enQueue", "__str__","Rear"]
    param = [[3],[1],[2],[3],[4],[],[],[],[4],[],[]]
    doTest(action, param)
    p = MyCircularQueue(3)
    p.enQueue(2)
    print(p.__str__())

