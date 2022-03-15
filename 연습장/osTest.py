import os

print(os.name)
print(os.getcwd())

for item in os.listdir():
    print(item)

with open("info2.txt", "w") as file:
    file.write("hello")
os.rename("info2.txt", "nex.txt")

os.remove("nex.txt")

os.system('chcp 65001')
os.system('ping google.com')