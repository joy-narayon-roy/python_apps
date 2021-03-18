num1=input("Enter 1st number : ")
num2=input("Enter 2nd number : ")
num1=int(num1)
num2=int(num2)

if num1>num2:
    print(f"{num1} is large number.")
elif num1==num2:
    print("Two number's are equal.")
else:
    print(f"{num2} is large number.")