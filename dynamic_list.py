import unittest
class Dynamic_list:
    def __init__(self):
        self.max_length = 2
        self.count = 0
        self.data = [0] * self.max_length

    def size(self):
        return self.count

    def capacity(self):
        return self.max_length

    def is_empty(self):
        return self.size() == 0

    def at(self, index):
        if 0 <= index < self.count:
            return self.data[index]
        else:
            raise Error("out of bound")

    def push(self, item):
        if self.count >= self.max_length:
            self._resize_(self.max_length * 2)
        self.data[self.count] = item
        self.count += 1

    def insert(self, index, item):
        if 0<= index <= self.count:

            if self.count >= self.max_length:
                self._resize_(self.max_length * 2)
            for i in xrange(self.count, index, -1):
                self.data[i] = self.data[i-1]
            self.data[index] = item
            self.count += 1
        else:
            raise Error("insert out of bound")

    def prepend(self, item):
        self.insert(0,item)

    def pop(self):
        if self.count - 1 < 1/4.0 * self.max_length:
            self._resize_(int(1/2.0 * self.max_length))
        self.count -= 1
        return self.data[self.count]

    def delete(self,index):

        if index == self.count -1:
            self.pop()
        else:
            if self.count - 1 < 1/4.0 * self.max_length:
                self._resize_(int(1/2.0 * self.max_length))
            for i in xrange(index, self.count):
                self.data[i] = self.data[i+1]
            self.count -= 1

    def remove(self, item):
        for i in xrange(self.count):
            if self.data[i] == item:
                self.delete(i)
                return i

    def _resize_(self,new_capacity):
        print "resize:", new_capacity, self.max_length, self.count
        if new_capacity > self.count:
            temp = [0] * new_capacity
            for i,val in enumerate(self.data[:self.count]):
                temp[i] = val
            self.data = temp
            self.max_length = new_capacity
        else:
            raise Exception("capacity too small")
def test():
    test = [1,2,3,4,5,6]
    array = Dynamic_list()
    assert array.size() == 0
    assert array.is_empty() == True
    array.push(test[0])
    array.push(test[1])
    assert array.size() == 2
    array.push(test[3])
    array.push(test[4])
    print array.data
    array.insert(2,test[2])
    print array.data
    assert array.at(0) == test[0]
    assert array.at(1) == test[1]
    assert array.at(2) == test[2]
    assert array.at(3) == test[3]
    assert array.at(4) == test[4]

    assert array.pop() == test[4]
    assert array.size() == 4
    assert array.pop() == test[3]
    assert array.pop()
    assert array.pop()
    print array.size()
    print array.data




if __name__ == "__main__":
    test()
