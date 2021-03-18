from collections import deque

#Stack :- LIFO
books=[]
books.append("Learn C")
books.append("Learn C++")
books.append("Learn Java")

print(books)
print(books[-1])

books.pop()
print(books)
print(books[-1])

#Queue :- FIFO
bank=["x","y","a"]
bank=deque(["Joy","Narayon","Roy"])
print(bank)
bank.popleft()
print(bank)