# Import your csv module
import csv

# Write a function that accepts one csv filename as an argument.
# The functions hould open the file, read its contents and filter out rows where
# the state abbreviation is MD, writing only those rows to an md_banks.csv file.
def find_md_banks(filename):
    # Open the file to read and create the reader object
    csv_file = open(file_name, 'rb')
    csv_data = csv.reader(csv_file)

    # Open the file to write and create the writer object
    output_file = open('md_banks.csv', 'wb')
    writer = csv.writer(output_file, delimiter=',')

    # Write our header row to the output csv
    header_row = csv_data.next()
    writer.writerow(header_row)

    # Loop through the rows in the original file and write only the banks
    # in Maryland to the output file.
    for row in csv_data:
        if row[2] == 'MD':
            writer.writerow(row)
        else:
           continue

    # Close the original csv file
    csv_file.close()
    # Close the md_banks.csv file
    output_file.close()

# Call the function, passing as an argument the name of the csv file to open.
output_rows_from('banklist.csv')
