#declear needed variable
drugName = []
mySet = set()
results = []
data = []

#open file that contains data
f = open("itcont.txt" , "r")
#open file that needs to be write to
outputFile =  open("Output.txt", "w")


#data processing
for f in open("itcont.txt", "r"):
    data.append(f.replace("\n", "").split(","))

#add drug name into empty set
for i in range(len(data)):
    for j in range(len(data[i])):
        if j ==3 and i > 0:
            if data[i][j] not in drugName:
                mySet.add(data[i][j])
                    

#loops through myset,which contains the drug that was found
#then match the drug against the drug thats listed in data
for drugName in mySet:
    totalDrugPrice = 0
    totalAmountOfDrug = 0
    for i in range(len(data)):
      for j in range(len(data[i])):
        if j ==3 and i > 0:
            if drugName == data[i][j]:
                    totalAmountOfDrug += 1
                    totalDrugPrice += int(data[i][j+1])
    results.append(drugName)
    results.append(totalAmountOfDrug)
    results.append(totalDrugPrice)


#create outputFile Headder
outputFile.write("drug_name" + " " + "Quantity" + " " + "drugTotalCost" + "\n")


#use for counter
counter = 0

#loops through the results and write them into the empty file
for loopThroughWords in results:
    outputFile.write(str(loopThroughWords) + " ")
    counter += 1
    if(counter%3  == 0):
        outputFile.write("\n")

#close file after finished

outputFile.close()







