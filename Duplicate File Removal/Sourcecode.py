import os
import sys
import time
import datetime
import hashlib

def calculatechecksum(filename):
    fobj = open(filename,"rb")

    hobj = hashlib.md5()
    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName):
    Ret = False
    Ret = os.path.exists(DirectoryName)

    if Ret == False:
        print("Path is invalid")
        return
    
    Ret = os.path.isdir(DirectoryName)

    if Ret == False:
        print("Its not a directory")
        return
    
    Duplicate = {}

    for FolderName,SubFolder,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)

            Checksum = calculatechecksum(fname)

            print(f"{fname} : {Checksum}")
            
            if Checksum in Duplicate:
                same = same + 1
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]

    return Duplicate

def DeleteDuplicate(DirectoryName):

    MyDict = FindDuplicate(DirectoryName)

    if MyDict is None:
        return

    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))

    return Result

def main():
    Data = DeleteDuplicate("test")

    print(Data)

if __name__== "__main__":
    main()





