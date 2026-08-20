def parsing():
    
    file = open("textfile.txt","r")
    contents = file.read()
    file.close()

    words = contents.split()
    count = len(words)
    return count

def main():

    count_of_words = parsing()
    print(f"{count_of_words} words")

main()