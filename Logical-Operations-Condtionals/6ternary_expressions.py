def even(num):
    return num % 2 == 0

def main():

    num=float(input("Enter the number:"))
    result=even(num)

    if result:
        print("Even")
 
    else:
        print("odd")

main()