import cv2

# Load pre-trained Haar Cascade classifier for hand detection
hand_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'aGest.xml')

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture each frame from webcam
    ret, frame = cap.read()
    
    if not ret:
        break

    # Convert to grayscale for better hand detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect hands
    hands = hand_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
    
    # Draw rectangles around the detected hands
    for (x, y, w, h) in hands:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with hands detected
    cv2.imshow('Hand Detection', frame)
    
    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
