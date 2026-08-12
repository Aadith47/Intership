def main():
      
    list_of_number=[45, 2, 89, 12, 7]
    largest_num=list_of_number[0]
    smallest_num=list_of_number[0]

    for i in (list_of_number):
            if i > largest_num:
                largest_num = i

            if i < smallest_num:
                smallest_num = i

    print(f"The largest number is {largest_num}\nThe smallest number is {smallest_num}")

main()
    