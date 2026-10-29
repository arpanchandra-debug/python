import time
a=int(input("enter which number u want table:"))

for i in range(20):
    if(i==1):
        break
    print(a,"x",i+1,"=",a*(i+1))


t=time.process_time()
print("the time is taken=>",t)