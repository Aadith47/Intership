#Write a program that classifies a triangle as equilateral, isosceles, or scalene based on its three side lengths. Sample: Input: 5, 5, 5 → Output: Equilateral 

side1=float(input("Enter First side: "))
side2=float(input("Enter second side: "))
side3=float(input("Enter third side: "))

if side1 == side2 and side3 == side2:
    print("Triange is Equilateral")

elif side1 == side2 or side1 ==side3 or side2 == side3:
    print("isosceles")

else:
    print("Scalene")