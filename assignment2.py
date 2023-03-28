def add(x ,y):
    return x + y

def subtract(x ,y):
    return x - y

def divide (x ,y):
    return x/y


def multiply (x ,y):
    return x * y



def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
/ for division
* for multiplication
''')


x = float(input("Enter first number:"))
y = float(input("Enter second number:"))
operator = input("Enter operator")



if operator == '+':
     print('{} + {}' .format (x ,y))
     print(x+y)



elif operator == '-':
      print('{} - {}' .format (x ,y))
      print(x-y)


elif operator == '/':
     print('{} / {}' .format(x ,y))
     print(x/y)


elif operator == '*':
     print('{} * {}' .format(x ,y))
     print(x*y)

else:
    print("Invalid operator")

