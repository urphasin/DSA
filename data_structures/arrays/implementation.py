class DynamicArray:
    def __init__(this): # type: ignore
        this.capacity = 1  # initial capacity
        this.size = 0      # current number of elements
        this.array = this.make_array(this.capacity)

    def make_array(this, capacity): # type: ignore
        """Create a new array with given capacity"""
        return [None] * capacity

    def append(this, item): # type: ignore
        """Add item to the end of array, resize if needed"""
        if this.size == this.capacity:
            this.resize(2 * this.capacity)  # double capacity
        this.array[this.size] = item
        this.size += 1

    def resize(this, new_capacity): # type: ignore
        """Resize internal array to new_capacity"""
        new_array = this.make_array(new_capacity)
        for i in range(this.size):
            new_array[i] = this.array[i]
        this.array = new_array
        this.capacity = new_capacity

    def __getitem__(this, index): # type: ignore
        if 0 <= index < this.size:
            return this.array[index]
        else:
            raise IndexError('Index out of bounds')

    def __len__(this): # type: ignore
        return this.size

    def __str__(this): # type: ignore
        return str([this.array[i] for i in range(this.size)])


# Example usage
dyn_arr = DynamicArray()
for i in range(5):
    dyn_arr.append(i)
    print(f"Array: {dyn_arr}, Size: {len(dyn_arr)}, Capacity: {dyn_arr.capacity}")


######################################################################################################
# Static Array

class StaticArray:
    def __init__(this, capacity): # type: ignore
        this.capacity = capacity
        this.array = [None] * capacity

    def set(this, index, value): # type: ignore
        if 0 <= index < this.capacity:
            this.array[index] = value
        else:
            raise IndexError("Index out of bounds")

    def get(this, index): # type: ignore
        if 0 <= index < this.capacity:
            return this.array[index]
        else:
            raise IndexError("Index out of bounds")

    def __str__(this): # type: ignore
        return str(this.array)

# Example usage
static_arr = StaticArray(5)
static_arr.set(0, 10)
static_arr.set(4, 50)
print(static_arr)  # Output: [10, None, None, None, 50]
print(static_arr.get(0))  # Output: 10
print(static_arr.get(4))  # Output: 50

# static_arr.set(5, 100)  # Raises IndexError: Index out of bounds
