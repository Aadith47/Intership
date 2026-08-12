def main():

    list1=[1,2,3,4,5]
    n=int(input("Enter the number of rotation: "))
    list2 = list1[n:] + list1[:n]
    print(list2)

main()
