import zipfile
import time

folderPath = input("Path of the file: ")

folderPath = folderPath.strip()
zipf = zipfile.ZipFile(folderPath)
global result
result = 0
global tried
tried = 0
c=0
if not zipf:
    print("Its not a password protected zipped file. Can open successfully!!")

else:
    startime = time.time()    
    wordListFile = open('wordlist.txt',"r",errors='ignore')
    body = wordListFile.read().lower()
    words = body.split("\n")

    for i in range(len(words)):
        word = words[i]
        password = word.encode("utf8").strip()
        c=c+1
        print("Trying to decode password by {}".format(word))
        try:
            with zipfile.ZipFile(folderPath,"r") as zf:
                zf.extractall(pwd = password)
                print("Success! Password is: "+word)
                endTime = time.time()
                result = 1
            break
        except:
            pass
    if result ==0:
        print("Sorry. Password is not found. Count  = "+str(c)+ "Possible combinations tried in "+str(endTime))
    else:
        duration = endTime-startime
        print("Congratulations.Count: "+str(c)+" Password time : "+str(duration))        

