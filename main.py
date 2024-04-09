# Find Min and Max values in a list of tuples in Python

my_list = [(100, 1),  (100, 2), (100, 3)]

# ✅ get the Min tuple in list of tuples
min_tuple = min(my_list, key=lambda tup: tup[1])

print(min_tuple)  # 👉️ (100, 1)

# ------------------------------------------------------

# ✅ get the Max tuple in a list of tuples

max_tuple = max(my_list, key=lambda tup: tup[1])

print(max_tuple)  # 👉️ (100, 3)