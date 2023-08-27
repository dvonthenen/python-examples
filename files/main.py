from pathlib import Path

# file = Path("people.txt") # test the exception
file = Path("people.txt")

try:
    contents = file.read_text()
except FileNotFoundError:
    print("Not a valid file!")
    quit()
else:
    print("Always do this!")
print("\n")

print(f"file contents:\n{contents}\n")

for line in contents.splitlines():
    print(f"line: {line.strip()}")
print("\n")

for line in contents.splitlines():
    if "human" in line.lower():
        new_line = line.replace("human", "dog").strip()
        print(new_line)
    else:
        print(line.strip())
print("\n")

