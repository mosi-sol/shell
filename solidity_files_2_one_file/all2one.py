import glob
import re

# Get a list of all .sol files in the current directory
sol_files = glob.glob("*.sol")

# Open a new file to write the merged contents to
with open("00-clean.sol", "w") as merged_file:
    # Write the SPDX license identifier to the first line of the merged file
    merged_file.write("// SPDX-License-Identifier: MIT\n\n")

    # Iterate over each .sol file
    for file_name in sol_files:
        # Open the file and read its contents
        with open(file_name, "r") as current_file:
            lines = current_file.readlines()

        # Filter out lines with import statements, comments, SPDX lines, and comment blocks
        filtered_lines = []
        comment_block = False
        for line in lines:
            # Remove import statements
            if line.startswith("import"):
                continue
            # Remove single-line comments
            line = re.sub("//.*", "", line)
            # Remove multi-line comments
            if comment_block:
                if "*/" in line:
                    comment_block = False
                continue
            elif "/*" in line or line.startswith("/**"):
                comment_block = True
                continue
            # Remove SPDX lines
            if line.startswith("// SPDX-"):
                continue
            # Add the line to the filtered list
            filtered_lines.append(line)

        # Write the filtered lines to the merged file
        merged_file.writelines(filtered_lines)

        # Add a blank line after each file
        merged_file.write("\n")
