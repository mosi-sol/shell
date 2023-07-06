import json

# Load the smart contract ABI from file
with open('abi.json', 'r') as f:
    abi = json.load(f)

# Create new lists to hold the readable function and event ABIs
readable_functions = []
readable_events = []

# Iterate over each item in the ABI
for item in abi:
    if item['type'] == 'function':
        # Extract the information we need to make the function signature more readable
        name = item['name']
        inputs = ', '.join([param['type'] for param in item.get('inputs', [])])
        outputs = ', '.join([param['type'] for param in item.get('outputs', [])])
        visibility = item.get('visibility', 'public')
        state_mutability = item.get('stateMutability', '')
        if state_mutability == 'nonpayable':
            state_mutability = ''
        function_signature = f"function {name}({inputs}) {visibility} {state_mutability}"
        if outputs:
            function_signature += f" returns ({outputs})"
        readable_functions.append(function_signature)
    elif item['type'] == 'event':
        # Extract the information we need to make the event signature more readable
        name = item['name']
        inputs = ', '.join([param['type'] for param in item.get('inputs', [])])
        event_signature = f"event {name}({inputs})"
        readable_events.append(event_signature)

# Create a list to hold the readable ABI
readable_abi = readable_functions + readable_events

# Write the readable ABI to file
with open('abi-r.json', 'w') as f:
    json.dump(readable_abi, f, indent=4)
