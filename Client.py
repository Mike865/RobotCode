#importing the socket.
from socket import*
import cv2
import numpy as np
import sys
import pickle
import struct ### new code
cap=cv2.VideoCapture(1)

serverName = '192.168.0.119'
serverPort = 9879
#we create the client socket and then we connect the socket to the server (which is my other computer)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
while True:
    ret,frame=cap.read()
    data = pickle.dumps(frame) ### new code
    clientSocket.sendall(struct.pack("I", len(data))+data) ### new code