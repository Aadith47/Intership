def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num -2)

def main():

    num=int(input("Enter the number: "))
    fibonacci_number=fibonacci(num)
    print(f"The nth fibonacci number of {num} is {fibonacci_number}")
    
main()