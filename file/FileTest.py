# write
file = open("./data/testfile.txt","w")
file.write("Hello World\n")
file.write("This is our new text file\n")
file.write("and this is another line.\n")
file.write("Why? Because we can.\n")
file.close() 

# read
file = open("./data/testfile.txt", "r")
for line in file:
    print(line)
file.close()