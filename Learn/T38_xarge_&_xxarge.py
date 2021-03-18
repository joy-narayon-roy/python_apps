#xargument
def prnt(*details):
    print(details)
    
prnt(101,"Joy Roy",4.5)

def add(*numbers):
    sum =0 
    for x in numbers:
        sum=sum+x 
    return sum
print(add(5+5+10),"\n")

#xxargument

def student(**details):
    print("Id : ",details["id"])
    print("Name : ",details["name"])
    print("G.P.A : ",details["gpa"]," \n")
student(id=101,name="Narayon",gpa=4.5)
student(id=102,name="Joy",gpa=4.86)