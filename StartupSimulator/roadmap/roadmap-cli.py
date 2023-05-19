import json

# Define the list of titles to ask
titles = ['years']

# Create an empty dictionary to store the information
roadmap = {}

# Ask the user for details about each title
for title in titles:
    while True:
        print(f"Please enter details for {title}:")
        details = input()
        try:
            details = int(details)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    roadmap[title] = details

# Calculate the number of quarters based on the number of years
years = roadmap['years']
quarters = years * 4
roadmap['quarters'] = quarters

# Ask the user for details for each quarter
quarter_details = []
for i in range(1, quarters+1):
    while True:
        print(f"Please enter details for quarter {i}:")
        details = input()
        try:
            details = int(details)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    quarter_details.append(details)

# Store the quarter details in the roadmap dictionary
roadmap['quarter_details'] = quarter_details

# Savethe information in a JSON file
with open('roadmap.json', 'w') as f:
    json.dump(roadmap, f)