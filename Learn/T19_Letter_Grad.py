
num=int(input("Enter your number : "))

if num>=33 and num<=100:
    if num>=80 and num<=100:
        print("You got A+")
    if num>=70 and num<=79:
        print("You got A")
    if num>=60 and num<=69:
        print("You got A-")
    if num>=50 and num <=59:
        print("You got B")
    if num>=40 and num<=49:
        print("You got C")
    if num>=33 and num<=39:
        print("You got D")
elif num>=0 and num<33:
    print("You got F")
else:
    print("You are entered Invalid number.")