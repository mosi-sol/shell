import json

# Define the sections of the business plan
sections = ["Executive Summary", "Market Analysis", "Product or Service", "Marketing and Sales", "Operations", "Financials"]

# Create an empty dictionary to hold the user's responses
responses = {}

# Loop through each section and prompt the user for information
for section in sections:
    print("Please provide information for the", section, "section:")
    response = input()
    responses[section] = response

# Save the responses to a JSON file
with open("business_plan.json", "w") as fp:
    json.dump(responses, fp)