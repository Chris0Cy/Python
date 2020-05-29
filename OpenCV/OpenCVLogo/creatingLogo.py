import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,400), font, 4,(255,255,255),5,cv2.LINE_AA)

img = cv2.circle(img,(247,90), 70, (0,0,255), -1)
img = cv2.circle(img,(148,230), 70, (0,255,0), -1)
img = cv2.circle(img,(333,235), 70, (255,0,0), -1)



cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
