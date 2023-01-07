
# Python File tell() Method

# The tell() method returns the current file position in a file stream.

# syntax : file.tell()


with open("text.txt", "r") as file2:
    print(file2.readline())
    print(file2.tell())


# Output :
# welcome to python^NULNULNUL
#20



