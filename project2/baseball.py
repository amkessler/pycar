# Imports

# First, let's get the ID of each player in the top 10-percentile
def calculate_top10(filename):
    # Open the salary csv

    # Read the opened csv file with csv.reader

    # Arrange in descending order of salary
    # Remember that lists are ordered!

    # Create a list of the top 10%

    # Round it!

    # We don't want decimal points (you can't have part of a player) so cast to an int

    # Now let's create our final list, of just the highest-paid players
    top_10_percentile_ids = []

    # We only need the player IDs right now.
    # Loop over the sorted salaries and extract the player ID, adding it to the
    # top_10_percentile_ids list.

    # Return the top_10_percentile_ids list
    return top_10_percentile_ids


# We are going to be working with dictionaries to make things easier
def create_salary_dict(filename, top_10_percentile_ids):
    # Open the csv
    salaries_object = open(filename, 'rb')

    # This time, let's use DictReader, which maps the header row's values to each item in each row.
    player_dict = csv.DictReader(salaries_object)

    # Create new list of only 2013 information
    # NOTE: You can't start a variable with a number, so 2013_salaries won't work
    salaries_2013 = {}

    for row in player_dict:
        # Using DictReader allows us to access rows by their column name!
       year = row["yearID"]
       if year == '2013':
           # Create a record for each player's ID and assign it the salary
           salaries_2013[row["playerID"]] = row["salary"]

    # Now we can reference the salary of any player whose ID we know.
    # But we only want those who were in the top 10% of all time.
    # Create a new dict to hold just the top players from 2013
    top_salaries_2013 = {}

    # Let's compare our player dict with the list of all-time
    # high salaries we made in the first function.
    # (You could combine this step with the DictReader step above.)
    for player in top_10_percentile_ids:
        # Check for the presence of a key that matches the playerID in salaries_2013
        if player in salaries_2013:
            top_salaries_2013[player] = { "salary": salaries_2013[player] }

    return top_salaries_2013


def add_player_stats(master_file, top_salaries_dict):
    # Open the master csv

    # Read the file

    # Skip the header row

    # Create a master data dictionary

    # Add a key to master_dict for each row in the master data csv file.
    # The key will be the player ID. The value will be a dictionary with
    # keys and values for each of the headers in the master file.

    # Next we'll loop over top_salaries_dict to find the player IDs in master_dict.
    #
    # Remember, in top_salaries_dict, the key is the player ID and the value is the salary.
    #
    # Note: when you loop over a dict, you only have access to the keys.
    #
    # To access the values, we need .iteritems()
    #
    # Typically, when iterating over a dict, the syntax is:
    #
    #   for key, value in my_dict.iteritems():
    #
    # Add names, birth state and birth country to the top_salaries_dict. This is effectively a join
    # between some of the data in the master file and some of the data in the salaries file.

    # Return modified top_salaries_dict
    return top_salaries_dict

# The location of the data files
salary_file = 'data/2014/Salaries.csv'
master_file = 'data/2014/Master.csv'

# Call calculate_top10, passing salary_file. Store the return value in a variable
top10 = calculate_top10(salary_file)
# Pretty-print the return value
pprint(top10)

# Call create_salary_dict, passing salary_file and the return value of our call to calculate_top10.
top_salaries_dict = create_salary_dict(salary_file, top10)
# Pretty-print the return value
pprint(top_salaries_dict)

# Call add_player_stats, passing master_file and the return value of our call to create_salary_dict.
salaries_plus_player_stats = add_player_stats(master_file, top_salaries_dict)
# Pretty-print the result
pprint(salaries_plus_player_stats)
