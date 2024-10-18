import random
import sys
from socket import *

# Check command line arguments
if len(sys.argv) != 2:
    print("Usage: python UDPPingerServer <server port no>")
    sys.exit()

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('', int(sys.argv[1])))
print(f"Server is ready to receive on port {sys.argv[1]}")

while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    
    # Simulate packet loss (e.g., if rand < 4, simulate dropping the packet)
    if rand < 4:
        print("Packet lost (simulated).")
        continue  # Skip sending the response to simulate the loss

    # Decode the message from bytes to string
    message = message.decode("utf-8")
    
    # Capitalize the message from the client
    responseMessage = message.upper()
    
    # Print message for debugging purposes
    print(f"Received message: {message} from {address}")
    print(f"Sending capitalized message: {responseMessage}")
    
    # Send the response back to the client
    serverSocket.sendto(responseMessage.encode("utf-8"), address)
