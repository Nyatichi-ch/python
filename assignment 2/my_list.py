#creating an empty list
my_list = []

print(my_list)  # Output: []

#appending elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)  

print(my_list)  # Output: [10, 20, 30, 40]

#inserting an element at a specific index
my_list.insert(2, 15)
print(my_list)  # Output: [10, 20, 15, 30, 40]

#extending the list with another list
my_list.extend([50, 60, 70])
print(my_list)  # Output: [10, 20, 15, 30, 40, 50, 60, 70]

#removing an element by value
my_list.remove(70)
print(my_list)  # Output: [10, 20, 15, 30, 40, 50, 60]

#sorting the list in ascending order
my_list.sort()
print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60]

#finding and printing the index of an element
index_of_30 = my_list.index(30)
print(f"Index of 30: {index_of_30}")  # Output: Index of 30: 3