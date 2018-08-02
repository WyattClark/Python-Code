import os.path
import codecs

#save_path = 'C:\Users\wclar\OneDrive\Desktop\AvgNPOI'

name_of_file = input("What is the name of the file: ")

completeName = ('C:/Users/wclar/OneDrive/Desktop/AvgNPOI/' + name_of_file + '.txt')

file1 = open(completeName, "w")

toFile = input("Write what you want into the field")

file1.write(toFile)

file1.close()
