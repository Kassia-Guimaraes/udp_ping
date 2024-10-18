import random
import sys
from socket import *

# Check command line arguments
if len(sys.argv) != 2:
    print("Usage: python UDPPingerServer <server port no>")
    sys.exit()

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', int(sys.argv[1])))

while True:
	# Generate random number in the range of 0 to 10
	rand = random.randint(0, 10)
	# Receive the client packet along with the address it is coming from
	message, address = serverSocket.recvfrom(1024)
	message = message.decode("utf-8") # convert bytes to string
	# Capitalize the message from the client
	message = message.upper()
	#the server responds
	serverSocket.sendto(message.encode("utf-8"), address)