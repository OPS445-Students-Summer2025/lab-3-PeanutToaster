#!/usr/bin/env python3

#return_text_value() function

#Author: Ricky Tang 104448246

# Date Created: 2025/05/27

def return_text_value():
    name = 'Terry'
    greeting = 'Good Morning ' + name
    return (greeting)
text = return_text_value()
print(text)

#return_number_value() function

def return_number_value():
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3
number = return_number_value()
print(number)
print(number + 5)
print(return_number_value() + 10)
print('my number is ' + str(number))
print('my number is ' + str(return_number_value()))

#Main Program

if __name__ == '__main__':
    print('python code')
    text = return_text_value()
    print(text)
    number = return_number_value()
    print(str(number))