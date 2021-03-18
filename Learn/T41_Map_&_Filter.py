#Map start
num=[1,2,3,4,5]
def square(x):
    """docstring for square"""
    # TODO: write code...
    return x*x 
result=list(map(square,num))
print("Before : ",num)
print("After : ",result)
# Map End 
#Filter start
resul=list(filter(lambda x:x%2==0,num))
print("Even number : ",resul)