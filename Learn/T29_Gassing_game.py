from random import randint

correct=0
wrong=0
for x in range(0,5):
    randomNumber=randint(1,5)
    inputNumber=int(input("Enter number 1 to 5 : "))
    if randomNumber==inputNumber:
        print("It's match !")
        correct=correct+1
        print("Your input : ",inputNumber)
        print("Random Number : ",randomNumber)
        print("Correct : ",correct)
        print("Wrong : ",wrong)
    else:
        print("Not match !")
        wrong=wrong+1
        print("Your input : ",inputNumber)
        print("Random Number : ",randomNumber)
        print("Correct : ",correct)
        print("Wrong : ",wrong)

winPersent=(correct*100)/5
print("\nWin present : ",winPersent," %\n")