# Import built-in python modules we'll want to access csv files and import us module
# if you get an error run: pip install us or sudo pip install us
# Else contact @aboutaaron, @malev, @ryannagle
import csv
import us

# We're going to download a csv file...
# What should we name it?
file_name = "banklist.csv"

# loop over all US states
for state in us.states.STATES:
    # Open the csv file
    with open(file_name, "rb") as file:

        # Use python's csv reader to access the contents
        # and create an object that represents the data
        csv_data = csv.reader(file)
        headers = csv_data.next()
        # create csv based on state name
        filename = state.name + '_banks.csv'
        # create the file
        output_file = open(filename, 'wb')
        # create the writer with commas as delimiter
        writer = csv.writer(output_file, delimiter=',')
        # write the headers
        writer.writerow(headers)

        # Loop through each row of the csv...
        for row in csv_data:
            # assign state abbr
            this_state = row[2]
            # check if states match
            if this_state == state.abbr:
                # write the row
                writer.writerow(row)

        # close the file
        output_file.close()
