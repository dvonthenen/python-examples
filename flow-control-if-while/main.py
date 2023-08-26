msg = "What is your name?"
print(msg)

name = input().strip()
print(f"Hello, {name.title()}\n")

# students
students = {"jane": 15, "john": 14, "bob": 17, "kathy": 16}
print(f"Here are the {len(students)} students enrolled with their age:")
for student, age in students.items():
    print(f"{student}, age {age}")
print("\n")

print(f"We just enrolled {name}")
while True:
    age = int(input(f"what is {name.title()}'s age? "))
    if age == 0:
        print("Invalid value. Try again.")
    else:
        break

if name.lower() == "david":
    students[name]=age
else:
    students[name]=99

print(f"Here are the {len(students)} students enrolled now:")
for student, age in students.items():
    print(f"{student}, age {age}")
print("\n")

print("Kathy dropped out. Here is the list:")
del students["kathy"]
print(students)
