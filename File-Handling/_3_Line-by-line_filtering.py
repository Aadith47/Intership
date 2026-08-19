file = open("textfile.txt","r")
contents = file.read()
file.close()

count = 0
search_element = input("Enter the word to searched:")

words = contents.split()

for word in words:
    if word == search_element:
        count += 1

print(f"The word {search_element} is repeating {count} times")