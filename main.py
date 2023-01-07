
# Python File seek() Method

# The seek() method sets the current file position in a file stream.
# The seek() method also returns the new position.

# syntax : file.seek(offset)
# offset :	Required. A number representing the position to set the current file stream position.


with open("text.txt", "r") as file2:

    # Change the current file position to 5, and return the rest of the line:
    file2.seek(5)
    print(file2.readline())  # O/p : me to python^NULNULNUL

    print(file2.seek(4))     # O/p : 4 --> return the file position







