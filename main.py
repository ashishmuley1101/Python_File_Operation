
# Python File writable() Method

# The writable() method returns True if the file is writable, False if not.
# syntax : file.writeable()

with open("text1.txt", "a") as file2:
    print(file2.writable())

# Output : True --> file available for write return true otherwise false.
