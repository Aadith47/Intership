def main():

    list_of_number=[1,4,2,8,4,2,6]

    list_of_unique=[]

    for i in (list_of_number):
        if i not in list_of_unique:
            list_of_unique.append(i)

    print(f"List after removing duplicate={list_of_unique}")

main()
