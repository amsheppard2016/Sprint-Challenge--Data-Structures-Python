class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.size = 0
        self.index = 0

    def append(self, item):
        if self.size < self.capacity:
            self.storage.append(item)
            self.size +=1
        else:
            self.storage[self.index] = item
            if self.index < self.capacity - 1:
                self.index += 1
            else:
                self.index = 0
       
                

    def get(self):
        return self.storage
