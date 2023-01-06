
# Python File isatty() Method

# The isatty() method returns True if the file stream is interactive,
# example: connected to a terminal device.
# syntax : file.isatty()

with open("text1.txt", "r") as file2:
    print(file2.isatty())

# Output : False
