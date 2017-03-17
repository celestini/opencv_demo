import cv2
import numpy as np
import argparse
from imutils.video import VideoStream

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,
    help="path to output video file")
# ap.add_argument("-p", "--picamera", type=int, default=-1,
#   help="whether or not the Raspberry Pi camera should be used")
ap.add_argument("-f", "--fps", type=int, default=20,
    help="FPS of output video")
ap.add_argument("-c", "--codec", type=str, default="MJPG",
    help="codec of output video")
args = vars(ap.parse_args())

# intalize the video writer and output options.
fourcc = cv2.VideoWriter_fourcc(*args["codec"])
writer = None
(h, w) = (None, None)
zeros = None

cap = cv2.VideoCapture("data_source/vtest.avi")

ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255

while(1):
    ret, frame2 = cap.read()
    next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)


    # check if the writer is None
    if writer is None:
        # store the image dimensions, initialzie the video writer,
        # and construct the zeros array
        (h, w) = frame1.shape[:2]
        writer = cv2.VideoWriter(args["output"], fourcc, args["fps"],
        (w , h ), True)
        zeros = np.zeros((h, w), dtype="uint8")

    flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    hsv[...,0] = ang*180/np.pi/2
    hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
    rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

    cv2.imshow('frame2',rgb)
    writer.write(rgb)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite('opticalfb.png',frame2)
        cv2.imwrite('opticalhsv.png',rgb)
    prvs = next

cap.release()
cv2.destroyAllWindows()
writer.release()
