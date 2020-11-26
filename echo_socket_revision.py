import socket
import sys


#Let's try to connect a client socket to a server process. The following code is an
#example of TCP client socket that makes a connection to server socket:

def main():

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as e:
        print("Failed To Create A Socket")
        print("Reason : ", str(e))
        sys.exit()

    print("Socket Created Successfully")

    targetHost = input("Please enter target host name to connect: ")
    targetPort = input("Please enter target port : ")

    try:
        s.connect((targetHost, int(targetPort)))
        print("Socket connected to host " + targetHost + " on port " + targetPort)
        s.shutdown(2)


    except socket.error as e:
        print("Failed connection to host " + targetHost + " on port " + targetPort)
        print("Reason", str(e))
        sys.exit()


if __name__ == "__main__":
    main()