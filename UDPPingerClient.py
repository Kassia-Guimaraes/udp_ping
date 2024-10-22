import time
import sys
from socket import *

# Check command line arguments
if len(sys.argv) != 3:
    print("Usage: python UDPPingerClient <server ip address> <server port no>")
    sys.exit()

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)

# To set waiting time of one second for reponse from server
clientSocket.settimeout(5)

# Declare server's socket address
remoteAddr = (sys.argv[1], int(sys.argv[2]))

rounds_trip = []
ping_lost = []

n = 10

# Ping ten times
for i in range(n):

    sendTime = time.time()
    message = 'PING ' + str(i + 1) + " " + str(time.strftime("%H:%M:%S"))
    clientSocket.sendto(message.encode("utf-8"), remoteAddr)

    try:
        data, server = clientSocket.recvfrom(1024)
        recdTime = time.time()
        rtt = recdTime - sendTime
        rounds_trip.append(rtt)
        print("Message Received", data.decode("utf-8"))
        print(f"Round Trip Time, {rtt: .2f}")

    except timeout:
        ping_lost.append('PING ' + str(i + 1))
        print('\033[31mREQUEST TIMED OUT\033[0;0m')

print(f'\n\nMean of RTT:{sum(rounds_trip)/len(rounds_trip):.2f}\nMinimun of RTT: {min(rounds_trip):.2f}\nMaximun of RTT: {max(rounds_trip):.2f}\n')
print(f'Percent of Lost PINGs: {(len(ping_lost)/n)*100:.0f}%\n')

print("Closing the client socket...")
clientSocket.close()
