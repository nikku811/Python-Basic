# Initialize list
my_list = [10, 20, 30, 40, 50, 60, 70]

# 1. Slicing without start, stop, and step (returns the entire list)
print("Full slice:", my_list[:])

# 2. Slicing with start (from index 2 to the end)
print("Slice with start=2:", my_list[2:])

# 3. Slicing with stop (from beginning to index 4)
print("Slice with stop=4:", my_list[:4])

# 4. Slicing with step (every second element)
print("Slice with step=2:", my_list[0:7:2])

# 5. Slicing with negative step (reversing the list)
print("Slice with -ve step:", my_list[-3:-8:-1])