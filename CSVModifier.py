import csv

weather_file = 'Weather.csv'

def csv_reader(file_name):

    modified_data = []

    with open(file_name, 'r', newline='') as file:
        csv_dictionary = csv.DictReader(file)

        #Iterate through the newly converted dictionary.
        for row in csv_dictionary:
            #Iterate through the key/value pairs in each row.
            for key in row:
                #Multiply the values by 2.
                row[key] = float(row[key]) * 2
            #Add new content to the modified_data list
            modified_data.append(row)
    
    return modified_data

def csv_writer(file_name, data):
    """
    Writes a list of dictionaries to a new CSV file.
    """

    with open(file_name, 'w', newline='') as file:
        # Get the field names from the first dictionary
        fieldnames = data[0].keys()
        
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Write the header
        writer.writerows(data)  # Write the rows of data

modified_data = csv_reader(weather_file)

csv_writer("modified_weather_file.csv", modified_data)

with open("Weather.csv", mode='r') as file:
    print("\nOriginal Data:\n" + file.read())

with open("modified_weather_file.csv", mode='r') as file:
    print("\nUpdated Data:\n" + file.read())