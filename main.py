
# Python File truncate() Method

# The truncate() method resizes the file to the given number of bytes.

# syntax : file.truncate(size)
# size	Optional. The size of the file (in bytes) after the truncate. Default None,
# which means the current file stream position.

with open("text.txt", "a") as file2:
    file2.truncate(20)

with open("text.txt", "r") as file3:
    print(file3.read())

# Output : welcome to python^NULNULNUL


