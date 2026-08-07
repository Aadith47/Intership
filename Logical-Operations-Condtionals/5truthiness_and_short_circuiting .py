def length_in_pass(password):
   return len(password) < 8

def uppercase_in_pass(password):
   return any(char.isupper() for char in password)

def digit_in_pass(password):
   return any(char.isdigit() for char in password)

def main():

    password=input("Enter the passsword:")

    result1_in_pass = length_in_pass(password)
    result2_in_pass = uppercase_in_pass(password)
    result3_in_pass = digit_in_pass(password)

    if result1_in_pass:
        print("MUST CONTAIN 8 LONG")

    elif not result2_in_pass:
        print("MUST CONTAIN AN UPPERCASE LETTER")

    elif not result3_in_pass:
        print("MUST CONTAIN A DIGIT")

    else:
        print("STRONG PASSWORD")

main()
    
      
