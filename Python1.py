
Aileenlincy
/
IBM-B1A3E-07
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
IBM-B1A3E-07/Python1.py
@Aileenlincy
Aileenlincy Create Python1.py
 1 contributor
91 lines (70 sloc)  1.82 KB
#list

n=int(input("enter the list range"))
l=[]
for i in range(n):
    s=input()
    l.append(s)
print(l)
print("remove function")
s=input("enter a element to remove")
l.remove(s)
print(l)
s1=input("enter an element to append")
l.append(s1)
print(l)
print("sort")
l.sort()
print(l)
print("after pop")
l.pop()
print(l)
print("after reverse")
print(l[ : : -1])


#calculator 

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")

#string 

s=input("enter a string")
print("concatenate")
s1=input("enter a string")
s+=s1
print(s)
print("reverse")
print(s[ : : -1])
print("slicing")
s3=int(input("enter the range under " + str(len(s))))
print(s[:s3])

#python uses simplified syntax with an emphasis on natural language 
#python is free to use and is supported by extremely large ecosystem of
#libraries and packages 


#frameworks:pyramid,turbogear,web2py,cherrypy,flask,sanic,django


#WSGI-Web Server Gateway Interface