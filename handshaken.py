import cv2 as cv
cap=cv.VideoCapture(0)
from cvzone.HandTrackingModule import HandDetector
detector=HandDetector(detectionCon=0.5,maxHands=2)
print("HandDetector")
while(True):
    rec,frame=cap.read()
    hand,img=detector.findHands(frame) 
    if hand:
        
          hand1=hand[0]
          wichhand=hand1["type"]
          lmlist=hand1["lmList"]
          lenght0,info,_=detector.findDistance(lmlist[20][:-1],lmlist[17][:-1])



    cv.imshow("frame",frame)
    keyexit=cv.waitKey(5)&0xff
    if keyexit==27:
        break
cv.destroyAllWindows()
cap.release()