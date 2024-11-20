# Tuple

tuple1 = ('apple', 'banana', 'orange', 'mango', 'guava')
print("This is a tuple (tuple1): ",tuple1)

# Nested tuple

tuple2 = ([1, 4, 5], [15, 61, 33])
print("This is a nested tuple (tuple2): ",tuple2)

tuple3 = ([1, 3, [4, 9, 6, 8], [5, 7, 2]], [23, [20, 32, 63, 89], 30, [53, 52]])
print("This is a nested tuple in a nested tuple (tuple3): ",tuple3)

# Finding items in a tuple
x = input("Here are some examples of finding items in a tuple (Input to continue): ")
print()
print("1. The first element of tuple1 is",tuple1[0])
print("2. The last four elements of tuple1 are",tuple1[1:5])
print("3. The first tuple in tuple2 is",tuple2[0])
print("4. The second tuple in tuple2 is",tuple2[1])
print("5. The third element in the second tuple in tuple2 is",tuple2[1][2])
print("6. The fourth element in the first tuple in the second tuple in tuple3 is",tuple3[1][1][3])

# Sets

A = {'apple', 'banana', 'mango', 'pear'}

B = {'banana', 'mango', 'orange', 'pineapple'}

print("Set of sweet fruits (A): ",A)
print("Set of fruits that are yellow or orange (B): ",B)

# Union / Intersection

print("The fruits common between A and B are",A.intersection(B))
print("The union of A and B is",A.union(B))
