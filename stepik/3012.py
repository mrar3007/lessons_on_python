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
'''
class Buffer:
    def __init__(self):
        self.count = 1
        self.sum = 0
        self.arr = []
        self.buf = []

    def add(self, *a):
        for i in a:
            self.arr.append(i)
        n = len(self.arr) // 5
        self.buf += self.arr[:n * 5]
        while n != 0:
            for i in range(5):
                self.sum += self.buf[i]
                del self.arr[0]
            del self.buf[:5]
            print(self.count, ': ', self.sum)
            self.sum = 0
            self.count += 1
            n -= 1

    def get_current_part(self):
        print(self.arr)

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]
'''

