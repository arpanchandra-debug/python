A=float(input("enter your 1st sub number"))
B=float(input("enter your 2nd sub number"))
C=float(input("enter your 3rd sub number"))
D=float(input("enter your 4th sub number"))
Y=(A+B+C+D)
P=(Y/400*100)
print(P)
if(P>90 and P<100):
    print('O')
elif(P>70 and P<90):
    print('E')
elif(P>50 and P<70):
    print('G')
elif(P>30 and P<50):
    print('B')
else:
    print("better luck next time")




a=int(input("enter the number you got in math:"))

if(a>0 and a<=50):
    print("it's ok\nyou got enough number")
elif(a>50 and a<=100):
    print("you got more number than you need")
if(a>0 and a<=25):
    print("you got C ")
elif(a>25 and a<=50):
    print("you got B ")
elif(a>50 and a<=100):
    print("you got A")
b=int(input("enter the number you got in physics:"))
if(b>0 and b<=50):
    print("its ok\nyou got enough number")
elif(b>50 and b<=100):
    print("you got more number than you need")
if(b>0 and b<=25):
    print("you got C ")
elif(b>25 and b<=50):
    print("you got B ")
elif(b>50 and b<=100):
    print("you got A")
c=int(input("enter the number you got in chemistry:"))
if(c>0 and c<=50):
    print("its ok\nyou got enough number")
elif(c>50 and c<=100):
    print("you got more number than you need ")
if(c>0 and c<=25):
    print("you got C ")
elif(c>25 and c<=50):
    print("you got B ")
elif(c>50 and c<=100):
    print("you got A")
d=int(input("enter the number you got in biology:"))
if(d>0 and d<= 50):
    print("you got enough number\nso its ok")
elif(d>50 and d<=100):
    print("you got more number than you need")
if(d>0 and d<=25):
    print("you got C ")
elif(d>25 and d<=50):
    print("you got B ")
elif(d>50 and d<=100):
    print("you got A")
e=int(input("enter the number you got in bengali:"))
if(e>0 and e<=50):
    print("its ok\nyou got enough number")
elif(e>50 and e<=100):
    print("you got more number than you need")
if(e>0 and e<=25):
    print("you got C ")
elif(e>25 and e<=50):
    print("you got B ")
elif(e>50 and e<=100):
    print("you got A")
f=int(input("enter the number you got in english:"))
if(f>0 and f<=50):
    print("its ok\nyou got enough number")
elif(f>50 and f<=100):
    print("you got more number than you need")
if(f>0 and f<=25):
    print("you got C ")
elif(f>25 and f<=50):
    print("you got B ")
elif(f>50 and f<=100):
    print("you got A")
g=(a+b+c+d+e+f)
print("your total marks are",g,"out of 600")
print((g/600)*100,"percent number")