'''class MoneyBox:
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity
    def can_add(self, v):
        return True if self.count + v <= self.capacity else False
    def add(self, v):
        self.count += v if self.can_add(v) == True

obj = MoneyBox(10)
obj.add(5)
obj.add(3)
obj.add(2)
obj.add(12)
'''


