import os
import re
import json

for file in os.listdir():
    if file.endswith('.sol'):
        abi_list = []

        # print out struct tuple first
        with open(file) as f:
            content = f.read()
            struct_tuple = re.search(r'struct[^}]*}', content).group()
            struct_tuple = struct_tuple.replace('struct', 'tuple').replace('{', '(').replace(';', ',').replace('}', ')').replace(', )', ')').replace('(', '(')
            print(struct_tuple)

        print()

        # now turn events and functions into ethers.js human readable ABI form
        name = file.replace('.sol', '').capitalize()
        print(f"static {name}ABI = [")
        abi_file = []
        with open(file) as f:
            content = f.read()
            for line in content.splitlines():
                if re.match(r'^\s*(event|function)', line):
                    line = re.sub(r'^\s*', '\t', line)
                    line = re.sub(r'{\s*$', '', line)
                    line = re.sub(r';\s*$', '', line)
                    print(f'"{line}",')
                    abi_file.append(line.strip())
        abi_list.append(abi_file)
        print("]\n")

        # create a dictionary with the ABI information
        abi_dict = {"abi": abi_list}

        # save the dictionary as a JSON file
        abi_file_name = f"{name}.json"
        with open(abi_file_name, "w") as f:
            json.dump(abi_dict, f, indent=4)