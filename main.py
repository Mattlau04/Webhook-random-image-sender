import os, sys, random, time, json
from dhooks import Webhook, File

with open('config.json', 'r') as handle:
    config = json.load(handle)

interval = (config["interval"])
hook = Webhook((config["webhook"]))
loop = (config["loop"])
if not os.path.exists('.\\images\\'):
    print ("Creating folder: images.")
    os.makedirs('.\\images\\')
    
def forever():
    print ("Sending images every " + str(interval) + " seconds.")
    while True:
        try:
            file = random.choice(getListOfFiles('.\\images\\'))
        except Exception:
            print ("There are no files in the images folder. Please add some.")
            time.sleep(5)
            sys.exit()
        print (file)
        file = File(str(file))
        hook.send(file=file)
        time.sleep(int(interval))

def notforever():
    print ("Sending " + str(loop) + " images every " + str(interval) + " seconds.")
    for x in range(int(loop)):
        try:
            file = random.choice(getListOfFiles('.\\images\\'))
        except Exception:
            print ("There are no files in the images folder. Please add some.")
            time.sleep(5)
            sys.exit()
        print (file)
        file = File(str(file))
        hook.send(file=file)
        time.sleep(int(interval))
		
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

if loop == "forever":
    forever()
else:
    notforever()
