def bmi(w,h):
    return (w * 703) / (h ** 2)

def main():
    weight = float(input('Enter weight in pounds:'))
    feet = float(input('Enter feet portion of height'))
    inches = float(input('Enter inches portion of height'))

    total_inches = feet * 12 + inches
    my_bmi = bmi(weight, total_inches)
    print('Your BMI is ' + '{:3f}'. format(my_bmi))

    main()