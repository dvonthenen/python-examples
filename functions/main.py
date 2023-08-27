def get_a_name():
    while True:
        name = input("What is your name? ").strip()
        if name == "":
            print("Invalid name. Try again.")
        else:
            print(f"Hello, {name.title()}\n")
            return name
            
def get_an_age(name):
    while True:
        age = int(input(f"what is {name.title()}'s age? "))
        if age == 0:
            print("Invalid value. Try again.")
        else:
            return age

def how_are_you_feeling():
    while True:
        mood = input("How are you feeling? [good] ").strip()
        if mood == "":
            return default_feeling()
        return default_feeling(mood)
        
def default_feeling(mood="good"):
    print(f"I'm feeling {mood}")
    return mood

# students
students = {"jane": 15, "john": 14, "bob": 17, "kathy": 16}
print(f"Here are the {len(students)} students enrolled with their age:")
for student, age in students.items():
    print(f"{student}, age {age}")
print("\n")

name = get_a_name()
print(f"We just enrolled {name}")

if name.lower() == "david":
    students[name] = get_an_age(name)
else:
    students[name] = 99
print("\n")

mood=how_are_you_feeling()
print(f"Real {mood}\n")

print(f"Here are the {len(students)} students enrolled now:")
for student, age in students.items():
    print(f"{student}, age {age}")
print("\n")

print("Kathy dropped out. Here is the list:")
del students["kathy"]
print(students)
