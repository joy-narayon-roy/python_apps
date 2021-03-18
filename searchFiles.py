import os 
import re
#os.path.isdir
#os.path.splitext()
def printList(lists):
    # TODO: write code...
    nu=1
    for lis in lists:
        # TODO: write code...
        print(f"\n{nu}. {lis}")
        nu=nu+1 


def allFiles(lists):
    # TODO: write code...
    nu=1
    pattern = r"baba"
    mlis = []
    def isFile(nam):
        res = os.path.isfile(nam)
        if res:
            # TODO: write code...
            return 'file'
        else:
            return 'dir'
    for lis in lists:
        # TODO: write code...
        lis = lis.lower()
        mres = re.match(pattern,lis)
        if mres:
            # TODO: write code.. 
            mlis.append(lis)
        #print(f"\n{nu}. {lis} - {isFile(lis)}")
        nu=nu+1
    print(len(mlis))

os.chdir('../../../sdcard0/My Music/download/')
pwd=os.getcwd()
listFiles=os.listdir() 
print(pwd)
allFiles(listFiles)
