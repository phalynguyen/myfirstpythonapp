operation = input('''Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: ")) 
#addition
if operation == "+":
    print('{0} + {1} = '.format(number_1, number_2))
    print(number_1 + number_2)
#subtraction
elif operation == "_":
    print('{} - {} =  '.format(number_1, number_2))
    print(number_1 * number_2)
#division
elif operation == "/":
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)
else:
    print("YOu have  not entered a valid operation")





