import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray

# Initialize the PiCamera
camera = PiCamera()
camera.resolution = (640, 480)  # Set your desired resolution
raw_capture = PiRGBArray(camera, size=camera.resolution)

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier('/home/drone/Desktop/haarcascade_frontalface_default.xml')

for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
    image = frame.array
    
    # Convert the image to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    
    # Draw bounding boxes around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Display the resulting image with bounding boxes
    cv2.imshow("Face Detection", image)
    
    # Clear the stream for the next frame
    raw_capture.truncate(0)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
camera.close()
cv2.destroyAllWindows()
