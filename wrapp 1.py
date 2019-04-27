import cv2
import numpy as np
import cv2
import numpy as np
import matplotlib.pyplot as plt

 
video = cv2.VideoCapture("road_car_view.mp4")
 
while True:
    ret, orig_frame = video.read()
    if not ret:
        video = cv2.VideoCapture("road_car_view.mp4")
        continue
    orig_frame=cv2.resize(orig_frame,(800,600))
    pts1 = np.float32([[343,412],[492,412],[112,600],[742,600]])
    pts2 = np.float32([[0, 0], [800, 0], [0, 600], [800, 600]])
    
   
    
    #orig_frame=cv2.warpAffine(orig_frame,m,(600,1000))
    frame = cv2.GaussianBlur(orig_frame, (9, 9), 0)
    M = cv2.getPerspectiveTransform(pts1,pts2)

    dst = cv2.warpPerspective(frame,M,(800,600))
    cv2.imshow("dst", dst)

    cv2.imshow("frame", frame)
   
    key = cv2.waitKey(25)
    if key == 27:
        break
video.release()







#cv2.imshow('k',dst)
