def main():

    fruits=["apple","orange","blueberry"]
    fruit=(input("Enter a fruit: "))
    fruits.append(fruit)
    new_fruits=fruits.pop(1)
    print(f"removed fruit={new_fruits}")
    print(f"Fruits={fruits}")

main()