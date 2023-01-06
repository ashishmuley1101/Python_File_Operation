
# Exception Handling in Files using try and catch block

# If an exception occurs when we are performing some operation with the file, the code exits without closing the file.
# A safer way is to use a try...finally block.

try:
    # open a file
    file1 = open("text.txt")  # by default file on read mode open("text.txt", "r")

    # read the file
    read_content = file1.read()
    print(read_content)

# Closing a file will free up the resources that were tied with the file.
# It is done using the close() method in Python

finally:  # finally block close the file if exception occur.
    # close the file
    file1.close()
