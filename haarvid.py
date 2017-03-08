import numpy as np
import cv2

# Importing the pre-trained classifiers of OpenCV for face and eyes as XML files. 
face_cascade = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_eye.xml')

# Get the video feed from the PC's webcam.
cap = cv2.VideoCapture(0)

while True:
	# Get an image from the video-feed.
	ret, img  = cap.read()
	cv2.imshow('img',img)
	# Convert the  image to grayscale.
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# # Use the imported classifier to carry out detection at different scales. (see 'image pyramid')
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for(x,y,w,h) in faces:
		# Draw a rectangle indicating the face on the original image.		
		cv2.rectangle(img,(x,y), (x+w,y+h), (255,0,0), 2 )
		# roi_gray is the area of the gray-image where we have a face.		
		roi_gray = gray[y:y+h, x:x+w]
		#roi_color is the same area as above, but in the original image.		
		roi_color = img[y:y+h, x:x+w]
		# Search for eyes in this roi_gray( the face region), at multiple scales again.
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for(ex,ey,ew,eh) in eyes:
			# Draw rectangles indicating the eyes on the original image.
			cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2 )
		
	cv2.imshow('img',img)
	k = cv2.waitKey(30) & 0xff

	if k == 27:
		break;

cap.release()
cv2.destroyAllWindows()


