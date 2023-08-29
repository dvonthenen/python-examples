my_list1 = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
my_set1 = set(my_list1)
print(my_set1)

my_len = len(my_set1)
print(f"len: {my_len}")

my_list2 = ['sausage', 'milk', 'sausage', 'toast', 'eggs']
my_set2 = set(my_list2)

my_combined = (my_set1 | my_set2)
print(my_combined)

my_combined = (my_set1 & my_set2)
print(my_combined)
