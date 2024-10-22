import random
import sys
import time
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
    # Generate random number in the range of 0 to 10 (perda de pacotes)
    rand = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    message = message.decode("utf-8")  # convert bytes to string
    # Capitalize the message from the client
    message = message.upper()

    if rand < 3:
        print(f"\033[31mThe Message {message} is lost.\033[0;0m")
        continue  # The message is lost

    if 4 <= rand <= 6:
        delay = random.uniform(1, 4)
        print(f"\033[36mIntroducing a delay of {
              delay:.2f} seconds for the {message}\033[0;0m")
        time.sleep(delay)

    # the server responds
    serverSocket.sendto(message.encode("utf-8"), address)
    print(f"Message sent {message}")