class DynamicArray:
    def _init_(self):
        self.__capacity = 1
        self.__size = 0
        self._array = [None] * self._capacity
        self._resize_factor = 2

    def size(self):
        return self.__size
    
    def isEmpty(self):
        return self.size() == 0

    def append(self, data):
        if self._size == self._capacity:
            self.resize(2 * self._capacity)
        self._array[self._size] = data
        self.__size += 1

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.__size):
            new_array[i] = self.__array[i]
        self.__array = new_array
        self.__capacity = new_capacity

    def _str_(self):
        arr = [None] * self.__size
        for i in range(self.__size):
            arr[i] = self.__array[i]
        return '<->'.join(map(str, arr))

    def prepend(self, data):
        if self._size == self._capacity:
            self.resize(2 * self._capacity)
        new_capacity = self.__capacity + 1
        new_array = [None] * new_capacity
        new_array[0] = data
        for i in range(self.__size):
            new_array[i+1] = self.__array[i]
        self.__array = new_array
        self.__capacity = new_capacity
        self.__size += 1

    def insertAt(self, index, data):
        if index < 0 or index > self.__size:
            raise Exception("Invalid index")
        if index == 0:
            self.prepend(data)
        elif index == self.size():
            self.append(data)
        else:
            if self._size == self._capacity:
                self.resize(2 * self._capacity)
            new_capacity = self.__capacity + 1
            new_array = [None] * new_capacity

            for i in range(index):
                new_array[i] = self.__array[i]
            
            new_array[index] = data

            for i in range(index, self.__size):
                new_array[i+1] = self.__array[i]

            self.__array = new_array
            self.__capacity = new_capacity
            self.__size += 1

    def removeAt(self, index):
        if index < 0 or index > self.__size:
            raise Exception("Invalid index")
        else:
            new_array = [None] * self.__size
            for i in range(index):
                new_array[i] = self.__array[i]
            for i in range(index+1, self.__size):
                new_array[i-1] = self.__array[i]
            self.__array = new_array
            self.__size -= 1
    
    def getMiddle(self):
        if self.__size % 2 == 0:
            index = self.__size // 2
        else:
            index = self.__size // 2 + 1
        return self.__array[index]
    
    def reverse(self):
        start = 0
        end = self.__size - 1
        while start < end:
            self._array[start], self.array[end] = self.array[end], self._array[start]
            start += 1
            end -= 1
    
    def getIndex(self, data):
        for i in range(self.__size):
            if self.__array[i] == data:
                return i
        return -1
    
    def rotateRight(self, k):
        if self.__size <= 1:
            return
        k %= self.__size
        self._reverse(0, self._size-1)
        self.__reverse(0, k-1)
        self._reverse(k, self._size-1)

    def __reverse(self, start, end):
        while start < end:
            self._array[start], self.array[end] = self.array[end], self._array[start]
            start += 1
            end -= 1

    def merge(self, another_array):
        merged_array = DynamicArray()
        for i in range(self.size):
            merged_array.append(self.__array[i])
        for i in range(len(another_array)):
            merged_array.append(another_array[i])
        return merged_array
    
    def interleave(self, another_array):
        interleaved_array = DynamicArray()
        min_length = min(self.__size, len(another_array))

        for i in range(min_length):
            interleaved_array.append(self[i])
            interleaved_array.append(another_array[i])
        for i in range(min_length, len(self)):
            interleaved_array.append(self[i])
        for i in range(min_length, len(another_array)):
            interleaved_array.append(another_array[i])

        return interleaved_array

    def splitAt(self, index):
        if index < 0 or index > self.size():
            raise ValueError("Index out of range")
        array1 = DynamicArray()
        array2 = DynamicArray()

        for i in range(index):
            array1.append(self._array[i])
        for i in range(index, self._size):
            array2.append(self._array[i])
        return array1, array2
    
    def resizeFactor(self, factor):
        if factor <= 0:
            raise ValueError("Resize factor must be greater than 0")
        self._resizeFactor = factor