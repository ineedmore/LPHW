from sys import argv

script, filename = argv

print(f"We're going to erase the file called: {filename}")
print(f"If you don't want to do that, press CTRL-C, ortherwise press Return")

input(" ?")

print(f"Opening the file: {filename}")

target = open(filename, 'w')

print(f"Truncating the file: {filename}")
target.truncate()

print("Now I'm going to ask you for 3 strings:")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write this to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we close it")
target.close()
