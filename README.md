# opencv_demo
Feature Detection using Sift
-----------------------------
Scale Invariant Feature Transform (SIFT) is a feature detection algorithm to detect and describe local features in an image. Opencv_Contrib has inbuilt functions of Sift in which first keypoints in a grayscale image are detected and then drawn. These keypoints are then computed to get their description. This description, extracted from a training image, can then be used to identify the object when attempting to locate the object in a test image containing many other objects.


Feature Detection using Surf
----------------------------
In computer vision, speeded up robust features (SURF) is a patented local feature detector and descriptor. It can be used for tasks such as object recognition, image registration, classification or 3D reconstruction.The functionalaties of SURF are included in opencv_contrib packages.


Feature Detection Using Orb
----------------------------
ORB(Oriented Fast And Rotated Brief) is an efficient alternative to SIFT and SURF. Moreover,Orb is not a patented algorithm unlike sift and surf and can be readily used.


Face detection using the HAAR feature based cascade classifiers
--------------------------------------------------------------
Haar features are a set of values obtained by convolving the image with simple kernels each of which are designed to detect features like edges and lines.
Since this will result in an huge number of computations, the concept of integral images was introduced. Also, not all of these features are always used, only the ones yielding the best results. To further simplify the computation, the concept of a 'cascade of classifiers' is used, where these features are grouped into stages and windows in the image  which fail the early stages are discarded before proceeding to the next stage.
for a more detailed description, refer to this link: http://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html

Motion Detection using Optical Flow
-------------------------------------
Optical Flow is estimated using Lucas-Kanade method for a sparse feature set (in our example, corners detected using Shi-Tomasi algorithm).


Note:haardet.py: detects face from a still image
haarvid.py: detects face using a camera. Need to install fswebcam package on raspberry PI. 

The codes are from OpenCV tutorial. We have used OpenCV 3.2.0.


