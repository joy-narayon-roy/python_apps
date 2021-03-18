import os 
pat="/storage/emulated/legacy"

'''
n=0
for x in dir(os):
    # TODO: write code...
    print(n,'-',x)
    n=n+1
'''    
print(os.name)
print(os.getcwd())
print(os.getcwdb())
#print(os.mkdir('Joy'))
print(os.listdir())
print(os.pardir)

print(os.path.abspath(__file__))
print(os.path.altsep)
print(os.path.basename(os.getcwd()))
print(os.path.commonpath(__file__))
print(os.path.defpath)
print(os.path.getatime('OS.py'))
print(os.path.getctime('OS.py'))
print(os.path.getmtime('OS.py'))
print(os.path.getsize('OS.py'))
print(os.path.isfile('OS.py'))
print(os.path.isdir('OS.py'))   
print(os.path.realpath('OS.py'))
print(os.path.relpath('OS.py'))
#print(os.path.samefile('f1','f2'))  
#print(len(os.scandir()))

#os.rename('Joy','My')
#os.mkdir('Aaa')
'''
items=list(os.walk('/sdcard/'))
for x in items:
    # TODO: write code...
    print(x)
'''    