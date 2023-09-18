from socket import *
import cv2
import pickle
import struct 
import threading
#setting the serverPort
serverPort = 9879
#we set the server socket up and the bind it to 0.0.0.0 along with the port number.
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('0.0.0.0',serverPort))
#we tell the server socket to listen for a connection
serverSocket.listen(1)
print('The server is ready to receive')
conn,addr=serverSocket.accept()

frame_lock = threading.Lock()
frame = None

# Function to receive frames
def receive_frames(conn):
    global frame
    data = b""
    payload_size = struct.calcsize("I") 

    while True:
        while len(data) < payload_size:
            data += conn.recv(4)
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("I", packed_msg_size)[0]
        while len(data) < msg_size:
            data += conn.recv(4)
        frame_data = data[:msg_size]
        data = data[msg_size:]

        with frame_lock:
            frame = pickle.loads(frame_data)

# Create a thread for receiving frames
receive_thread = threading.Thread(target=receive_frames, args=(conn,))
receive_thread.start()

# Initialize a window for displaying the video frames
cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Video', 800, 600)

while True:
    with frame_lock:
        if frame is not None:
            cv2.imshow('Video', frame)
            frame = None

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video window and close the connection when done
cv2.destroyAllWindows()
conn.close()
serverSocket.close()







