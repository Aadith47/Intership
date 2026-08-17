list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 6, 7, 8]

duplicate_items = []

for i in list1:
    if i in list2:
        duplicate_items.append(i)

print(duplicate_items)
