# Importing the required libraries
import cv2
# Opening the camera
cap = cv2.VideoCapture(0)
# Checking if the camera is opened
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()
# Reading the camera feed
while True:
    # Reading the frame
    ret, frame = cap.read()
    # Checking if the frame is read
    if not ret:
        print("Error: Could not read frame.")
        break
    # Displaying the frame
    cv2.imshow("Camera Feed", frame)
    # Checking if the user has pressed the 'Esc' key
    k = cv2.waitKey(1)
    if k%256 == 27:
        print("Escape hit, closing...")
        break