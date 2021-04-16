import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt

#img = cv2.imread("test.png")
#text = pytesseract.image_to_string(img)
#print(text)

font=1.5
font=cv2.FONT_HERSHEY_PLAIN
cap=cv2.VideoCapture(1)
#cap=cv2.VideoCapture()
#cap.set(cv2.CAP_PROP_FPS,170)

if not cap.isOpened():
    cap=cv2.VideoCapture(1)
if not cap.isOpened():
    raise IOError("Cannot open video")

cntr=0;
while True:
    ret,frame=cap.read()
    cntr=cntr+1
    if ((cntr%20)==0):
        imgH,imgW,_=frame.shape
        x1,y1,w1,h1=0,0,imgH,imgW
        
        imgchar=pytesseract.image_to_string(frame)
        
        imgboxes=pytesseract.image_to_boxes(frame)
        
        for boxes in imgboxes.splitlines():
            boxes=boxes.split(' ')
            x,y,w,h=int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
            cv2.rectangle(frame,(x,imgH-y),(w,imgH-h),(0,0,255),3)
            
            cv2.putText(frame,imgchar,(x1+int(w1/50),y1+int(h1/50)),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),2)
            font=cv2.FONT_HERSHEY_SIMPLEX
            cv2.imshow('Text DETECTION ',frame)
            
            if cv2.waitKey(2) & 0xFF == ord('q'):
                break
        
cap.release()
cv2.destroyAllWindows()
