import cv2
import face_recognition
from picamera import PiCamera
from picamera.array import PiRGBArray

# Load the reference face image
reference_image = face_recognition.load_image_file('img.jpeg')  # Replace with your reference image
reference_face_encodings = face_recognition.face_encodings(reference_image)

# Initialize the PiCamera
camera = PiCamera()
camera.resolution = (640, 480)  # Set your desired resolution
raw_capture = PiRGBArray(camera, size=camera.resolution)

for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
    image = frame.array

    # Detect faces in the current frame
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare the face encoding of the detected face with the reference face encoding
        matches = face_recognition.compare_faces(reference_face_encodings, face_encoding, tolerance=0.6)

        # Draw a red bounding box for the recognized face and green for others
        if any(matches):
            cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
        else:
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

    # Display the resulting image with bounding boxes
    cv2.imshow("Face Recognition", image)

    # Clear the stream for the next frame
    raw_capture.truncate(0)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
camera.close()
cv2.destroyAllWindows()
