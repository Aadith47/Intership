def even(num):
    
    result=num % 2 == 0
    return result

def main():

    num=int(input("Enter the number"))

    if even(num):
        print("Even")
 
    else:
        print("odd")

main()