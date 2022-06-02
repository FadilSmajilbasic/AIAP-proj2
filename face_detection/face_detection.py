from time import sleep
import cv2
from cv2 import CascadeClassifier

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
capture = cv2.VideoCapture(0)

if (capture.isOpened()):
    while(True):
        returnCode, frame = capture.read()
        # Convert into grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detects objects of different sizes in the input image
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=4)
        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            # Add rectangle around face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Add ellipse/circle around face
            # cv2.ellipse(frame, center=(int(x+(w/2)), int(y+(h/2))), axes=(int(w/2), int(h/2)),
            #             angle=0, startAngle=90, endAngle=450, color=(0, 0, 255), thickness=1)

            # Add a point at the center of a face
            # cv2.circle(frame, (int(x+(w/2)), int(y+(h/2))),
            #            radius=3, color=(0, 0, 255), thickness=-1)

            # Add text to the image
            cv2.putText(frame, 'face', (x, y),
                        cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0))
        cv2.imshow('Video', frame)
        sleep(0.02)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
else:
    print('Could not open video device')
