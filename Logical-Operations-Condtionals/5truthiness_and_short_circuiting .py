def lenth_in_pass(password):
   result1 = len(password) < 8
   return result1

def uppercase_in_pass(password):
   result2 = any(char.isupper() for char in password)
   return result2

def digit_in_pass(password):
   result3 = any(char.isdigit() for char in password)
   return result3

def main():

    password=input("Enter the passsword:")

    if lenth_in_pass(password):
        print("MUST CONTAIN 8 LONG")

    elif not uppercase_in_pass(password):
        print("MUST CONTAIN AN UPPERCASE LETTER")

    elif not digit_in_pass(password):
        print("MUST CONTAIN A DIGIT")

    else:
        print("STRONG PASSWORD")

main()
    
      
