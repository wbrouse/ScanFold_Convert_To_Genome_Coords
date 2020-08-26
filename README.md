# ScanFold_Convert_To_Genome_Coords

This script will take three inputs, a .bp file from ScanFold, a starting genomic coordinate, and a chromosome number. This will convert transcript coordinates to genomic coordinates for easy comparison with annotation tracks from the UCSC genome browser

To run this script in the command line ensure script and bp file are in the working directory, call python, followed by script name, input file name, starting genomic coordinate, and chromosome written as 'chr#'.
This will output a new ScanFold bp track that is in genomic coordinates and can be uploaded to IGV for visualization against other annotated tracks
