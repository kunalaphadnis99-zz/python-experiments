list1 = [1, 2, 3]
list2 = [101, 102, 103, 104]  # doesn't matter if this is a tuple, set

print(list(zip(list1, list2)))  # ignores the extra elements beyond matching counts
