################################################
#    
#   Importing Required liabraries
#
################################################

import sys
import os
import time
import schedule

################################################
#    
#   Function name : DirectoryScanner
#   Input : Name of directory
#   Description : Delete all empty files periodically
#   Date : 19/07/2026
#   Author : ASH
#
################################################

def DirectoryScanner(DirectoryPath):
    Border = "-"*40

    timestamp = time.ctime()
    LogfileName = "marvellous%s.log"%(timestamp)
    LogfileName = LogfileName.replace(" ","_")
    LogfileName = LogfileName.replace(":","_")

    ret = False

#Check whether directory exists
    ret = os.path.exists(DirectoryPath)
    if(ret == False):
        print("Marvellous Automation error : there is no such directory with name ",DirectoryPath)
        return
    
    ret = os.path.isdir(DirectoryPath)
    if(ret == False):
        print("Marvellous Automation error : it is not a directory with name",DirectoryPath)
        return

    print("log File gets created with name : ",LogfileName)

    fobj = open(LogfileName,"w")

    fobj.write(Border+"\n")
    fobj.write(" Marvellous Automation Script \n")
    fobj.write(Border+"\n")

    fobj.write("Files from the directory are : \n\n")
    fobj.write(Border+"\n\n")

    Totalfiles = 0
    emptyfiles = 0

    for FolderName,SubFolder,Filename in os.walk(DirectoryPath):
        for fname in Filename:
            Totalfiles = Totalfiles + 1

            fname = os.path.join(FolderName,fname)
            fobj.write(f"{fname} : {os.path.getsize(fname)}\n")

            if(os.path.getsize(fname) == 0):
                emptyfiles = emptyfiles + 1
                os.remove(fname)
    
    fobj.write(Border+"\n")
    fobj.write(f"Total files scanned : {Totalfiles}\n")
    fobj.write(f"Total empty files found and deleted :{emptyfiles}+\n")
            
    fobj.write(Border+"\n")
    fobj.write("log file gets created at : "+timestamp)
    fobj.write("\n"+Border+"\n")

    fobj.close()

################################################
#    
#   Function name : main
#   Input : Command line arguments
#   Description : it controls the script
#   Date : 19/07/2026
#   Author : ASH
#
################################################

def main():
    border ="-"*40
    
    print(border)
    print(" Marvellous Automation Script ")
    print(border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h"):
            print("This automation is used to travel the directory")
            print("for better usage , please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as")
            print("python Filename.py DirectoryName")
            print("Directory name should be absolute path")

        else:
            # DirectoryScanner = (sys.argv[1])
            schedule.every(5).seconds.do(DirectoryScanner,sys.argv[1])
            #DirectoryScanner(sys.argv[1])

            while True:
                schedule.run_pending()
                time.sleep(1)
    else:
        print("Invalid Numbers of arguments")
        print("Please use --h or --u for more info")

    print(border)
    print(" Thank you for using marvellous  ")
    print(border)

################################################
#    
#   Starter of the automation script
#
################################################
if __name__ == "__main__":
    main() 
