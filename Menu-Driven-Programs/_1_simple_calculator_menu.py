def sum_of_two(var1,var2):
    return var1 + var2 

def mul_of_two(var1,var2):
    return var1 * var2

def div_of_two(var1,var2):
    return var1 / var2

def sub_of_two(var1,var2):
    return var1 - var2

def main():

    while True:
        
        choice=input("Enter choice \n1.Addition\n2.Multiplication\n3.Division\n4.Substraction\n5.Exit\n")

        if choice=="5":
            print("Exiting.....")
            break

        var1=int(input("Enter the first number: "))
        var2=int(input("Enter the second number"))

        if choice== "1":
            result1=sum_of_two(var1,var2)
            print(f"{var1} + {var2} = {result1}")

        elif choice=="2":
            result2=mul_of_two(var1,var2)
            print(f"{var1} * {var2} = {result2}")

        elif choice=="3":
            result3=div_of_two(var1,var2)
            print(f"{var1} / {var2} = {result3}")

        elif choice=="4":
            result4=sub_of_two(var1,var2)
            print(f"{var1} - {var2} = {result4}")

main()

