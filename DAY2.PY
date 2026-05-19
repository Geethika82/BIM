#1 Check Employee promotion eligibility
age=int(input())
experience=int(input())
salary=int(input())
if age>25 and experience>5 and salary>50000:
    print("Eligible for Promotion")
else:
    print(" NOT Eligible")
#2 Check student distinction category
m=int(input())
s=int(input())
e=int(input())
if m>=75 and s>=75 and e>=75:
    print("distinction")
elif m>=35 and s>=35 and e>=35:
    print("pass")
else:
    print("fail")
#3 Check website login system
username=input()
password=int(input())
otp=int(input())
if username=="geethika" and password==123 and otp==5678:
    print("Login successfull")
else:
    print("Login failed")
#4 Check internet package category
speed=int(input())
datausage=int(input())
remaining_days=int(input())
if speed>350 and datausage>400 and remaining_days<=20:
    print("Premium plan")
elif speed>250 and datausage>300 :
    print("Standard Plan")
else:
    print("Basic plan")
#5 Check job eligibility
deg_av=input("enter yes or no:")
experience=int(input())
age=int(input())
if deg_av=="yes" and experience>=2 and age>=21:
    print("Eligible for Interview")
else:
    print("Not Eligible")
#6. Check whether both entered numbers are even
a=int(input())
b=int(input())
if a%2==0 and b%2==0:
    print("even")
else:
    print("odd")
#7Check whether both entered numbers are positive
a=int(input())
b=int(input())
if a>0 and b>0:
    print("positive")
else:
    print("negative")
#8 Check mobile unlock system
pin=int(input())
fingerprint=input("yes or no")
facedetection=input("yes or no")
if pin==9898 and fingerprint=="yes" and facedetection=="yes":
    print("Mobile Unlocked")
else:
    print("Mobile Locked")
#9 . Check hotel booking eligibility
rooms = int(input())
days = int(input())
budget = int(input())
if rooms >= 2 and days >= 3 and budget > 50000:
    print("Luxury Booking")
elif rooms >= 1 and budget > 20000:
    print("Standard Booking")
else:
    print("Budget Booking")
# 10. Check exam topper category
sub1 = int(input())
sub2 = int(input())
sub3 = int(input())
total = sub1 + sub2 + sub3
if total >= 270:
    print("Topper")
elif total >= 180:
    print("Average")
else:
    print("Needs Improvement")
# 11. Check gym membership category
age = int(input())
weight = int(input())
height = float(input())
if age > 18 and weight > 50 and height > 5.5:
    print("Fitness Category A")
elif age > 18 and weight > 40:
    print("Fitness Category B")
else:
    print("Basic Category")
# 11. Check gym membership category
age = int(input())
weight = int(input())
height = float(input())
if age > 18 and weight > 50 and height > 5.5:
    print("Fitness Category A")
elif age > 18 and weight > 40:
    print("Fitness Category B")
else:
    print("Basic Category")
# 12. Check traffic penalty system
helmet = input("yes or no ")
license = input("yes or no")
speed = int(input())
if helmet == "yes" and license == "yes" and speed < 80:
    print("No Fine")
elif speed > 100:
    print("Heavy Fine")
else:
    print("Normal Fine")
# 13. Check movie ticket pricing
age = int(input())
day = input()
member = input("yes or no ")
if age < 18 and member == "yes" and day == "Sunday":
    print("50% Discount")
elif member == "yes":
    print("25% Discount")
else:
    print("No Discount")
# 14. Check weather alert system
temperature = int(input())
wind = int(input())
rain = input()
if temperature > 40 and wind > 50 and rain == "no":
    print("Heat Alert")
elif rain == "yes" and wind > 60:
    print("Storm Alert")
else:
    print("Normal Weather")
# 15. Check online shopping offer
amount = int(input())
coupon = input("yes or no ")
member = input("yes or no ")
if amount > 10000 and coupon == "yes" and member == "yes":
    print("Maximum Discount")
elif amount > 5000 and coupon == "yes":
    print("Medium Discount")
else:
    print("No Discount")
# 16. Check server room access
idcard = input("yes or no")
fingerprint = input("Fyes or no ")
accesslevel = int(input())
if idcard == "yes" and fingerprint == "yes" and accesslevel > 5:
    print("Access Granted")
else:
    print("Access Restricted")
# 17. Check sports team selection
speed = int(input())
fitness = int(input())
discipline = int(input())
if speed > 80 and fitness > 80 and discipline > 80:
    print("Selected")
elif speed > 60 and fitness > 60:
    print("Waiting List")
else:
    print("Rejected")
# 18. Check laptop purchase recommendation
budget = int(input())
ram = int(input())
storage = int(input())
if budget > 100000 and ram >= 16 and storage >= 512:
    print("Gaming Laptop")
elif budget > 50000 and ram >= 8:
    print("Office Laptop")
else:
    print("Basic Laptop")
# 19. Check bank loan approval
salary = int(input())
creditscore = int(input())
experience = int(input())
if salary > 50000 and creditscore > 750 and experience > 3:
    print("Loan Approved")
elif salary > 30000 and creditscore > 650:
    print("Loan Under Review")
else:
    print("Loan Rejected")
# 20. Check smart home security system
door = input("yes or no")
camera = input("yes or no ")
alarm = input("yes or no")
if door == "yes" and camera == "yes" and alarm == "yes":
    print("Home Secure")
else:
    print("Security Warning")
