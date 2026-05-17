#1
age=int(input())
salary=int(input())
if age>21 and salary>30000:
    print("true")
else:
    print("False")
#2
m1=int(input())
m2=int(input())
if m1>=35 and m2>=35:
    print("pass")
else:
    print("fail")
#3
a=int(input())
min=10
max=50
if a>min and a<max:
    print("number between min and max")
else:
    print("number is not between min and max")
#4
username="geethika"
password=123
user=input()
passw=int(input())
if user==username and password==passw:
    print("valid uesername and password")
else:
    print("not valid username and password")
#5
lowerlimit=25
upperlimit=40
temp=int(input())
if temp>lowerlimit and temp<upperlimit:
    print("SAFE")
else:
    print("NOT SAFE")
#6
a,b=map(int,input().split(" "))
if a%2==0 and b%2==0:
    print("EVEN")
else:
    print("NOT EVEN")
#7
a,b=map(int,input().split(" "))
if a>0 and b>0:
    print("POSITIVE")
else:
    print("NEGATIVE")
#8
age=int(input())
license=input("enter yes or no:")
if age>18 and license=="yes":
    print("eligible")
else:
    print("not eligible")
#9
days=int(input())
percentage=int(input())
if days<4 and percentage>=85:
    print("project progress meets deadline condition")
else:
    print("project progress does not meets deadline condition")
#10
marks,attendence=map(int,input().split(" "))
if marks>35 and attendence>75:
    print("eligible")
else:
    print("not eligible")
#11
role=input("enter the role:")
if role=="admin" or role=="manager":
    print("yes")
else:
    print("no")
#12
sub1,sub2,sub3=map(int,input().split(" "))
if sub1>=75 or  sub2>=75 or sub3>=75:
    print("distinction")
else:
    print("not distinction")
#13
day=input("enter the day:")
if day=="sunday" or day=="saturday":
    print("weekend")
else:
    print("weekdays")
#14
val=int(input())
val1=25
val2=35
if val==val1 or val==val2:
    print("yes")
else:
    print("no")
#15
salary=int(input())
exper=int(input())
if salary>40000 or exper>4:
    print("satisfied")
    
else:
    print("not satisfied")
#16
temperture=int(input())
if temperture<25:
    print("cold")
else:
             print("hot")
#17
user=input()
if user=="geethika" or user=="lahari" or user=="kavya":
    print("valid")
else:
    print("not valid")
#18
selop=int(input())
if selop==1 or selop==2 or selop==3 or selop==4:
    print("valid")
else:
    print("not valid")
#19
city=input()
if city=="anakapalli" or city=="vizag" or city=="tuni":
    print("allowed")
else:
    print("not allowed")
#20
num=int(input())
if num==1 or num==2 or num==3:
    print("yes")
else:
    print("no")
#21
user=input()
if not user=="admin":
    print("yes")
else:
    print("no")
#22
    print("positive")

#23
str=input()
if  not str=="":
    print("not empty")
else:
    print("empty")
#24
file=False
print(not file)
#25
active=False
print(not active)
#26
status="completed"
if not status=="completed":
    print("no")
else:
    print("yes")
#27
password=int(input())
if  not password==123:
    print("correct")
else:
    print("not correct")
#28
temp=int(input())
if  not temp>=50:
    print("not safe")
else:
    print("safe")
#29
num=int(input())
if not (num==1 or num==2 or num==3):
    print("allowed")
else:
    print("not allowed")
#30
passmark=int(input())
if  not passmark<=35:
    print("yes")
else:
    print("no")