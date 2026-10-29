A=float(input("enter 1st number: "))
B=float(input("enter 2nd number: "))
C=input("what you want to do? (+,-,*,/): ")
if(C=='+'):
    print(A+B)
elif(C=='-'):
    print(A-B)
elif(C=='*'):
    print(A*B)
elif(C=='/'):
    print(A/B)
else:
    print("invalid syntax")
