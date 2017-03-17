
import numpy as np
import cv2
import time

########################### Pedestrian Detection using HOG Descriptor; INbuilt library of OPENCV ############################
def inside(r, q):
    rx, ry, rw, rh = r
    qx, qy, qw, qh = q
    return rx > qx and ry > qy and rx + rw < qx + qw and ry + rh < qy + qh


def draw_detections(img, rects, thickness = 1):
    for x, y, w, h in rects:
        # the HOG detector returns slightly larger rectangles than the real objects.
        # so we slightly shrink the rectangles to get a nicer output.
        pad_w, pad_h = int(0.15*w), int(0.05*h)
        cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 0, 255), thickness=2)

start_time = time.time()

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

img = cv2.imread('frame341.jpg')
found,w=hog.detectMultiScale(img, winStride=(8,8), padding=(32,32), scale=1.05)
draw_detections(img,found)
# cv2.imshow('feed',img)
# k = cv2.waitKey(3000)
cv2.imwrite('marked.jpg',img)

print("The execution time is ", time.time() - start_time)

cv2.destroyAllWindows()
