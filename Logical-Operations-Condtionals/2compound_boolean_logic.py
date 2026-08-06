def leap_year_calc(year):
    result=(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    return result

def main():
    year = int(input("Enter the year: "))

    if leap_year_calc(year):
     print("Leap year")

    else:
     print("Not leap year")

main()