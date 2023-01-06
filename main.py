
# Python File flush() Method

# The flush() method cleans out the internal buffer.
# syntax : file.flush()

with open("text.txt", "w") as file2:
    file2.write("Now the file has one more line!")
    file2.flush()
    file2.write("\n...and another one!")
