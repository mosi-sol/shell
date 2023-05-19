# { "name": "John", "age": 30, "city": "New York" }

import json

def format_json(json_string):
    """Formats a JSON string with indentation."""
    parsed = json.loads(json_string)
    return json.dumps(parsed, indent=4)

# Ask the user to input a JSON string
json_string = input("Enter a JSON string: ")

# Format the JSON string
formatted_json = format_json(json_string)

# Print the formatted JSON string
print(formatted_json)