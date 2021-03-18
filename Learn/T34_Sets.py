num1={1,2,3,5,2,6}
print(num1)
num2=set([4,5,6])
num2.add(7)
print(num2)
num2.remove(4)
print(num2)
print(4 in num2)
print(7 in num2)

print("A u B = ",num1 | num2)
print(num1 & num2)
print(num1 - num2)