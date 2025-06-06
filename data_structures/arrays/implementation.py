class DynamicArray:
    def __init__(self):
        self.capacity = 1  # initial capacity
        self.size = 0      # current number of elements
        self.array = self.make_array(self.capacity)

    def make_array(self, capacity):
        """Create a new array with given capacity"""
        return [None] * capacity

    def append(self, item):
        """Add item to the end of array, resize if needed"""
        if self.size == self.capacity:
            self.resize(2 * self.capacity)  # double capacity
        self.array[self.size] = item
        self.size += 1

    def resize(self, new_capacity):
        """Resize internal array to new_capacity"""
        new_array = self.make_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        else:
            raise IndexError('Index out of bounds')

    def __len__(self):
        return self.size

    def __str__(self):
        return str([self.array[i] for i in range(self.size)])


# Example usage
dyn_arr = DynamicArray()
for i in range(5):
    dyn_arr.append(i)
    print(f"Array: {dyn_arr}, Size: {len(dyn_arr)}, Capacity: {dyn_arr.capacity}")


######################################################################################################
# Static Array

class StaticArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity

    def set(self, index, value):
        if 0 <= index < self.capacity:
            self.array[index] = value
        else:
            raise IndexError("Index out of bounds")

    def get(self, index):
        if 0 <= index < self.capacity:
            return self.array[index]
        else:
            raise IndexError("Index out of bounds")

    def __str__(self):
        return str(self.array)

# Example usage
static_arr = StaticArray(5)
static_arr.set(0, 10)
static_arr.set(4, 50)
print(static_arr)  # Output: [10, None, None, None, 50]
print(static_arr.get(0))  # Output: 10
print(static_arr.get(4))  # Output: 50

# static_arr.set(5, 100)  # Raises IndexError: Index out of bounds
