def greet():
    return "Hi"

def main():

    name=input("Enter your name: ")
    result1=greet()
    print(f"{result1} {name}")

main()