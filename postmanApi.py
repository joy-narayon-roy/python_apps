import json
import requests
class Contact:
    name=""
    phone=""
    email=""
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email
        
def addUrl():
    return input("Enter your URL : ")
    
def runing():
    print("What you want ? Enter the Number : ")
    n=int(input("1 => Get\n2 => Post\n3 => Put\n4 => Delete\nYou want - "))
    if n==1:
        get()
    elif n==2:
        post()
    elif n==3:
        put()
    elif n==4:
        delete()
def get():
    url = addUrl()
    print(requests.get(url).json())
def post():
    url=addUrl()
    data=Contact(input("Enter your name : "),input("Enter your phone : "),input("Enter your email : "))
    #data=data.__dict__
    data = json.dumps(data.__dict__)
    requests.post(url,data)
def put():
    url=addUrl()
    data=Contact(input("Enter your name : "),input("Enter your phone : "),input("Enter your email : "))
    data=data.__dict__
    requests.post(url,data)
def delete():
    url=addUrl()
    requests.delete(url)
runing()


#data = json.dumps(data.__dict__)