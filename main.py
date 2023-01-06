
# Reading Files in Python using read() method

# The read() method to read its contents from the file.
# First we have to open the txt file using open() method.

# open a file
file1 = open("text.txt")  # by default file on read mode open("text.txt", "r")

# read the file
read_content = file1.read()
print(read_content)

# Closing a file will free up the resources that were tied with the file.
# It is done using the close() method in Python

# close the file
file1.close()
