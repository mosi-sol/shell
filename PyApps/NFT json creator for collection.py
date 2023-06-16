import json

# Ask user for NFT collection information
name = input("Enter the name of the NFT collection: ")
quantity = int(input("Enter the quantity of NFTs in the collection: "))
description = input("Enter a description of the NFT collection: ")
address = input("Enter the address of the contract for the NFT collection: ")

# Create list of NFTs with unique IDs
nfts = []
for i in range(quantity):
    nft_id = str(i)
    nft_dict = {
        "id": nft_id,
        "name": f"{name} #{nft_id}",
        "description": f"{description} (NFT #{nft_id})",
        "address": address+"/"+nft_id+".png"
    }
    nfts.append(nft_dict)

# Create dictionary with NFT collection information and list of NFTs
nft_dict = {
    "name": name,
    "quantity": quantity,
    "description": description,
    "address": address,
    "nfts": nfts
}

# Convert dictionary to JSON string with indentation
nft_json = json.dumps(nft_dict, indent=4)

# Write JSON string to file
with open("nft_collection.json", "w") as f:
    f.write(nft_json)