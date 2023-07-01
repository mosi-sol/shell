import base64

while True:
    # Ask user for message
    message = input("Enter message (or type 'exit' to quit): ")

    # Check if user wants to exit
    if message.lower() == "exit":
        print("Exiting program...")
        break

    # Ask user if they want to encode or decode
    while True:
        action = input("Do you want to encode or decode the message? (E/D): ")
        if action.upper() == "E":
            encoded_message = base64.b64encode(message.encode('utf-8'))
            print("Encoded message:", encoded_message)
            break
        elif action.upper() == "D":
            decoded_message = base64.b64decode(message.encode('utf-8')).decode('utf-8')
            print("Decoded message:", decoded_message)
            break
        else:
            print("Invalid input. Please enter 'E' to encode or 'D' to decode.")