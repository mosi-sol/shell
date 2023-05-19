import json

# Define the list of pitch deck section titles
pitch_deck_titles = [
    "Cover page",
    "Problem",
    "Solution",
    "Market size",
    "Business model",
    "Marketing and sales strategy",
    "Management team",
    "Financial projections",
    "Funding requirements",
    "Competition",
    "Milestones",
    "Appendix"
]

# Define a dictionary to store the user input for each section
pitch_deck_info = {}

# Loop through each section and ask the user to provide information
for title in pitch_deck_titles:
    print(f"Please provide information for the '{title}' section:")
    pitch_deck_info[title] = input()

# Save the pitch deck information to a JSON file
with open("pitch_deck_info.json", "w") as f:
    json.dump(pitch_deck_info, f)