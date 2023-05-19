import json

# Define the list of section titles
sections = ["Startup name", "Startup industry", "Executive Summary", "Problem and Solution", 
            "Market Analysis", "Target Market and Customer Segments", "Marketing and Sales Plan", 
            "Product or Service Description", "Business Model", "Team and Management Structure", 
            "Financial Plan and Projections", "Funding Needs and Use of Funds", "Milestones and Timeline", "Roadmap"]

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