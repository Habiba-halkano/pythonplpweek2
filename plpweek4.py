file = open("data.txt", "r")
print(file.read())

newfile = open("data1.txt", "w")
newfile.write("this is now a modified file, notice the change")

file = input("Enter file name:")
try:
    file = open(file)
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Wow!, the system is still okay")