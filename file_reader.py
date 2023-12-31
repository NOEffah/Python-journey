# Reading Files

filename = 'pi_digits.txt'

# Reading Entire file into memory
with open(filename) as file_object:
    contents = file_object.read()
print(contents)

# Reading lines in a file
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Or
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# Determining number of characters in file or
pi_string = ''

for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# Read some part of the file
for line in lines:
    pi_string += line.strip()

print(pi_string[:20])
print(len(pi_string[:20]))

# Finding data in the file
# Continuing from the above pi_string that contains the contents of our file

# # birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first 30 decimals of pi!")
# else:
#     print("Sorry, Your birthday does not appear in the first 30 decimals of pi!")

# Replacing string in a file
file_name = "learning_python"

with open(file_name) as learning:
    learn_py = learning.readlines()

for line in learn_py:
    nlearn = line.replace('Python', 'Javascript')
    print(nlearn.strip())

# Writing to a file
# Creating the new file

creating_file = 'programming.txt'

with open(creating_file, 'w') as fileobject:  # Pass a 2nd argument to open for reading("r", default), writing("w")
    # ,appending, read and write("r+")
    # note that python only allows you to write strings into a file
    fileobject.write("I love programming.\n")
    fileobject.write("I love creating new games.\n")

with open(creating_file, 'a') as fileobject:
    fileobject.write("I also love finding meaning in large datasets.\n")
    fileobject.write("I love creating apps that can run in a browser.\n")

username = input("What is your name: ")

username_file = "guest.txt"

with open(username_file, 'w') as user_file:
    user_file.write(username)