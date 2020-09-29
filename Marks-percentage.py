# Find-Total-Marks-Percentage
subject1 =int(input("Enter your marks subject1 : "))
subject2 =int(input("Enter your marks subject2 : "))
subject3 =int(input("Enter your marks subject3 : "))
subject4 =int(input("Enter your marks subject4 : "))
subject5 =int(input("Enter your marks subject5 : "))
subject6 =int(input("Enter your marks subject6 : "))
total=600
marks=subject1+subject2+subject3+subject4+subject5+subject6
p=(marks*100)/total
print("Total precentage = "+str(p))
if p<50:
    print("Fail")
else:
    print("pass")
