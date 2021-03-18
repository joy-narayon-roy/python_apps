import csv
import json
fileName=input('Enter File Name (Only CSV) :')
csvData = open((f"{fileName}"),'r')
data = list(csv.reader(csvData))

class Convert():
    def __init__(self):
        self.data = []
    def insert(self,data):
        data=list(data)
        i=0
        for item in data:
            print(i)
            if i==0:
                ''
            else:
                # TODO: write code...
                newList=dict(zip(data[0],data[i]))
                self.data.append(newList)
            i=i+1
            
        return self
    
jsonData = Convert()
jsonData.insert(data)
jsonFile=open('JsonData.json','w')
jsonFile.write(json.dumps(jsonData.data))
print('Done.\nFile Name : JsonData.json')