msg = "What is your name?"
print(msg)

name = input().strip()
print(f"Hello, {name.title()}\n")

print("How are you doing?")
value = input()
if "good" in value.lower():
    print("I'm good too")
elif "ok" in value.lower():
    print("I'm ok too")
else:
    print(f"I'm {value} too")
print("\n")

# students
students = ["Jane", "John", "Bob"]
print(f"Here are the {len(students)} students enrolled:")
for student in students:
    print(student)
print("\n")

print(f"The first student is {students[0]}\n")

print(f"We just enrolled {name}")
students.append(name)

print(f"Here are the {len(students)} students enrolled now:")
for student in students:
    print(student)
print("\n")

graduated = students.pop(0)
print(f"{graduated} just graduated. Here is the list now:")
for student in students:
    print(student)
print("\n")

droppedOut = students.pop()
print(f"{droppedOut} just dropped out. Here is the list now:")
for student in students:
    print(student)
print("\n")

students.sort()
print("In order...")
for student in students:
    print(student)
print("\n")

print("Same order...")
for student in students:
    print(student)
print("\n")

students.sort(reverse=True)
print("Reverse the order...")
for student in students:
    print(student)
print("\n")

print("You could just print the list like this:")
print(students)

print("3 seniors transfer from another school")
students.insert(0, "james")
students.insert(0, "kathy")
students.insert(0, "frank")
print(students)

print("The middle 3 students are:")
print(students[1:4])
