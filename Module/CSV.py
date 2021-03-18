import csv

'''
x=0
for n in dir(csv):
    # TODO: write code...
    print(f"{x} - {n}")
    x=x+1
'''
file=open('BPL.csv','r')
reader = csv.reader(file)
print(dir(list(reader)))

'''
writer=csv.writer(file)
wr=[['01/12/2020',4,'Buy',20],['10/12/2020',4,'Buy',20],['18/12/2020',4,'Buy',20]]
writer.writerows(wr)
lis=[]
sum=0
for datas in reader:
    lis.append(datas)
'''

#print("Date       | USD | Type | Number")    
for row in reader:
    print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")

class jsonClass:
    def __init__(self,date,teamA,teamB,time):
        self.date=date 
        self.teamA=teamA
        self.teamB=teamB
        self.time=time
day1=jsonClass('24/12/20','MM','MB','12:30 PM')
print(day1.date)