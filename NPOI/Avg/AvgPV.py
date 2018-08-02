import sys;

Text_File_Name = input("Enter the name of the text file you want to create:")
Number_of_Observations=int(input("Enter the number of observations to be calculated: "))

List_of_Observations=[]

for i in range(0,Number_of_Observations):
    Obervation=int(input("Enter Observation PV Number %s: " % (i+1)))
    List_of_Observations.append(Obervation)
avg=sum(List_of_Observations)/Number_of_Observations
print("Average of Observations in the list",round(avg,2))

Text_Doc = open('C:/Users/wclar/OneDrive/Desktop/AvgNPOI/' + Text_File_Name + '.txt', 'w')
for item in List_of_Observations:
  Text_Doc.write(" PV Number %s\n" % item)

Text_Doc.write("Avg. Value = %s" %avg)
Text_Doc.close()
