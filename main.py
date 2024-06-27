import csv

# Load and read the CSV file
file_path = 'username.csv'
data = []

with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file, delimiter=';')
    for row in csv_reader:
        data.append(row)

# Display the contents of the CSV file
for row in data:
    print(row)
