import csv

phoneNumbers={
    629:"01533599629",
    456:"01533581456",
    794:"01626234794",
    839:"01745496839",
    191:"01765055191",
    643:"01882390643",
    735:"01936033735"
}
phoneNumberList=[
    phoneNumbers[629],
    phoneNumbers[456],
    phoneNumbers[794],
    phoneNumbers[839],
    phoneNumbers[191],
    phoneNumbers[643],
    phoneNumbers[735]
]

def manu():
    """docstring for manu"""
    # TODO: write code...
    command=int(input('What you want?\nRead => 1\nWrite => 2\nYou - '))
    if command==1:
        read()
    elif command==2:
        write()

#Read Start
def read():
    total=0
    file=open('Recharge.csv','r')
    print("\nPrint your Datas\n")
    reader=csv.reader(file)
    for item in reader:
        total=total+int(item[2])
        print(f"{item[0]} | {item[1]} | {item[2]}") 
    print(f'\nTotal - {total} tk')
    print('\nDone')
#Read End 

#Write Start    
def write():
    file=open('Recharge.csv','a')
    writer=csv.writer(file)
    date=input('\nDate : ')
    num=input('Phone : ')
    if num=="629" or num=="456" or num=="794" or num=="839" or num=="191"or num=="643" or num=="735":
        num=int(num)
        num=phoneNumbers[num]
    else:
        for item in phoneNumberList:
            if num==item:
                print('Match')
    amount=input('Amount : ')
    dat=[date,num,amount]
    writer.writerow(dat)
    print('\n',dat)
#Write End    
manu()
