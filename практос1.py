a=int(input("Введите первое число"))
b=int(input("Введите второе число"))
c= (input("Введите действие"))
if c== "+":
    print(a+b)
elif c=='-':
    print(a-b)
elif c== "*":
    print(a*b)
elif c== "/":
    if b==0:
        print ("Делить на 0 нельзя")
    else:
        print (a/b)
elif c== "//":
    print (a//b)
elif c== "%":
    print (a%b)
elif c== "**":
    print (a**b)
elif c== ">":
    print(a > b)
elif c== "<":
    print(a < b)
elif c== "==":
    print(a == b)
elif c== ">=":
    print(a >= b)
elif c== "<=":
    print(a <= b)
elif c== "!=":
    print(a != b)
elif c == "and":
        print(a > 0 and b > 0)
elif c == "or":
        print(a > 0 or b > 0)
elif c == "not":
        print(not (a == b))
else:
     print("Некоректное действие")
