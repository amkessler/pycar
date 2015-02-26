# Import built-in python modules we'll want to access csv files and download files
import csv
import urllib

# We're going to download a csv file...
# What should we name it?
file_name = "banklist.csv"

# Use urllib.urlretrieve() to download the csv file from a url and save it to a directory
# The csv link can be found at https://www.fdic.gov/bank/individual/failed/banklist.html
target_file = urllib.urlretrieve("http://www.fdic.gov/bank/individual/failed/banklist.csv", file_name)

# Open the csv file
with open(file_name, "rb") as file:

    # Use python's csv reader to access the contents
    # and create an object that represents the data
    csv_data = csv.reader(file)

    # Loop through each row of the csv...
    for row in csv_data:
        # and print the row to the terminal
        print row
