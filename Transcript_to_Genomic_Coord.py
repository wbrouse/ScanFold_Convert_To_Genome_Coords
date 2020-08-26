#ScanFold transcript coordinates to genome coordinates
#This script will take three inputs, a .bp file from ScanFold, a starting genomic coordinate, and a chromosome number. This will convert transcript coordinates to genomic coordinates for easy comparison with annotation tracks from the UCSC genome browser

#To run this script in the command line ensure script and bp file are in the working directory, call python, followed by script name, input file name, starting genomic coordinate, and chromosome written as 'Chr#'.
#This will output a new ScanFold bp track that is in genomic coordinates and can be uploaded to IGV for visualization against other annotated tracks


import sys
import os

bpi = []				#Defining the column in the bp file that will be turned into a list
bpj = []
bpi2 = []
bpj2 = []
color = []


filename = sys.argv[1]				#bp file
Coordinate = (sys.argv[2])			#Genomic coordinate
Chr_Num = str(sys.argv[3])			#Chromosome number

with open(filename , 'r') as bpfile, open("genomic_coord.bp", "w") as genomic:						#Open the input bp file in read mode and open the new bp file in write mode
	color_head = bpfile.readlines()[0:7]															#Read the first 7 lines of the input bp file that do not need modified
	for line in color_head:
		genomic.write(line)																			#Write these first 7 lines to the new bp file
with open(filename , 'r') as bpfile, open("genomic_coord.bp", "a") as genomic:						#Open the input bp file in read mode again and open the new bp file with the added 7 lines in write mode
	lines = bpfile.readlines()[7:]																	#Read the lines of the input starting at line 8, which is the first line that needs modified
	for line in lines:
		data = line.split('\t')																		#Create new variable called data that contains all parts of the input file broken up at the tab
		Chr = (data[0].replace('UserInput', Chr_Num))												#Replace first peice of data in every line with the input Chromosome number
		bpi = (int(Coordinate)+int(data[1])-int(1))													#Add the input coordinate to the second peice of data, bp i, and subtract 1 to give new genomic coordinate as the starting postition
		bpi2= (int(Coordinate)+int(data[2])-int(1))
		bpj = (int(Coordinate)+int(data[3])-int(1))													#Add the input coordinate to the fourth peice of data, bp j, and subtract 1 to give new genomic coordinate as the ending postition
		bpj2 = (int(Coordinate)+int(data[4])-int(1))
		color = data[5]																				#Color value that does not need modified
		genomic.write(str(f"{Chr}\t{str(bpi)}\t{str(bpi2)}\t{str(bpj)}\t{str(bpj2)}\t{color}"))		#Use an f string literal to print all new coordinates and color column under the first 7 lines
os.rename('genomic_coord.bp', 'Genomic_' + filename)														#Rename outfile to the same as input with genomic added to the front to differentiate. This is necessary to load properly in IGV
