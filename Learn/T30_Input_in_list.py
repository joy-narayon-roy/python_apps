text = input("Enter any text : ")

numberLetter=0
numberWord=0
numberDegit=0

for x in text:
    x=x.lower()
    if x>="a" and x<="z":
        # TODO: write code...
        numberLetter=numberLetter+1
    elif x>=9:
        numberDegit=numberDegit+1
        
print("Number of Digit : ",numberDegit)
print("Number of Letter : ",numberLetter)
print("Number of Word : ",numberWord)