import math
#this program add 2 numbers 
num1 = 1.5
num2 = 6.3

sum = num1 + num2
print(f"the sum of num1 {num1} and num2 {num2} is {sum}")

#add numbers entered by users
number1 = int(input("enter any number1 : "))
number2 = int(input("Enter any number2 : "))
print("The sum of number1 and number2 is {} ".format(number1 + number2))

#squareroot of numbers using **
number3 = 41
print("the square root of {} is {}".format(number3, round(41**0.5, 5)))

#using sqrt()
answer = 81
print("the squareroot of answer is {}".format(math.sqrt(answer)))


