# The data we need to retrieve
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Module3_Python/Election_Analysis/Resources","election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join('Module3_Python/Election_Analysis/analysis', 'election_analysis.txt')

# Open the election results and read the file
with open(file_to_load) as election_data:
   
    # To Do: Read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print the header row. 
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file. 
    # for row in file_reader:
    #     print(row)
    
    # for row in file_reader:
    #     print (row[0])


# with open(file_to_save, 'w') as txt_file:
# #write three counties to the file.
#     txt_file.write("Counties in the Election\n------------------------ \nArapahoe\nDenver\nJefferson")


# 1. the total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage fo votes each candidates won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

