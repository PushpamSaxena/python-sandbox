import subprocess
import sys
import datetime

numDays=5
listOfImagesToBeDeleted=[]

currDate = datetime.datetime.today()
print("Current system date is: ",currDate) 
#print(currDate) 

process = subprocess.Popen("docker images --format \"{{.ID}}: {{.CreatedAt}}\"", shell=True, stdout=subprocess.PIPE)
(output, err) = process.communicate()
process.wait()

if (process.returncode == 0):
    #print output

    # Split the output on blank spaces
    result = output.split("\n");
    #print result

    for eachEntry in result:
        if (eachEntry):
            #print eachEntry
            singleImage = eachEntry.split();
            #print singleImage[1]
            #print datetime.datetime.strptime(singleImage[1], '%Y-%m-%d') 
            #print currDate - datetime.datetime.strptime(singleImage[1], '%Y-%m-%d')
            timeDiff = currDate - datetime.datetime.strptime(singleImage[1], '%Y-%m-%d')
            #print timeDiff.total_seconds()
            if (timeDiff.total_seconds() > numDays*24*3600):
                #print singleImage[0].replace(":","") 
                listOfImagesToBeDeleted.append(singleImage[0].replace(":","")) 

else:
    print "Received error message from the command run - ", err
    sys.exit('Exiting the script')

print ','.join(listOfImagesToBeDeleted)
#print str(listOfImagesToBeDeleted)[1:-1]


commDeleteImages="docker image rm -f " + ' '.join(listOfImagesToBeDeleted)
print commDeleteImages
process = subprocess.Popen(commDeleteImages, shell=True, stdout=subprocess.PIPE)
(output, err) = process.communicate()
process.wait()


if (process.returncode == 0):
    print output


else:
    print "Received error message from the command run - ", err
    sys.exit('Exiting the script')
