file = open("textfile.txt","r")
contents = file.read()
file.close()

words = contents.split()
count = len(words)

print(f"{count} words")