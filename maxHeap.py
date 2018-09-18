class MaxHeap(object):
    def __init__(self):
        self.array = [0]
        self.count = 0

    def find_child(self, index):
        return index * 2

    def find_parent(self, index):
        if index == 0:
            return -1
        else:
            return index / 2

    def bubble_up(self, index):
        while index != 1:
            parent_index = self.find_parent(index)
            if self.array[parent_index] < self.array[index]:
                self.array[parent_index],self.array[index] = \
                self.array[index],self.array[parent_index]
            else:
                break
            index = parent_index

    def bubble_down(self, index):
        while self.find_child(index) <= self.count:
            child = self.find_child(index)
            max_child_index = child
            for i in xrange(2):
                if i + child < self.count:
                    if self.array[child+i] > self.array[max_child_index]:
                        max_child_index = child + i
            if self.array[index] < self.array[max_child_index]:
                self.array[index],self.array[max_child_index] = \
                self.array[max_child_index],self.array[index]
            else:
                break
            index = max_child_index

    def insert(self, item):
        self.array.append(item)
        self.count += 1
        self.bubble_up(self.count)

        return

    def getMax(self):
        return self.array[1]

    def get_size(self):
        return self.count

    def pop_max(self):
        max_item = self.getMax()
        self.remove(1)
        return max_item

    def remove(self, index):
        self.array[index] = self.array[self.count]
        self.count -= 1
        self.bubble_down(index)

def heapify(array):
    heap = MaxHeap()
    for i in array:
        heap.insert(i)
    return heap

def heapsort(array):
    heap = heapify(array)
    for i in xrange(len(array)-1,-1,-1):
        array[i] = heap.pop_max()
    return array


def test():
    heap = MaxHeap()
    for i in xrange(10):
        heap.insert(i)
    print heap.array
    # for i in xrange(10):
    #     print heap.pop_max()

    import random
    test_array = range(10)
    random.shuffle(test_array)
    print heapsort(test_array)

if __name__ == "__main__":
    test()



