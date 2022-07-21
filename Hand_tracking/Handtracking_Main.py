# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 18:57:43 2022

@author: sai
"""
import cv2
import time
import HandtrackingModule as htm

ptime=0
ctime=0

cap= cv2.VideoCapture(0)

detector = htm.handDetector()

while True:
    
      suc,img = cap.read()
      img= detector.findhands(img)
      lmlist = detector.findposition(img)
      if len(lmlist)!=0:
         print (lmlist[4])
      
      ctime= time.time()
      fps = 1/(ctime-ptime)
      ptime= ctime
      
      cv2.putText(img, str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
      cv2.imshow('image', img)
      
      if cv2.waitKey(1) & 0xFf==27:
         break 
         
cap.release()
cv2.destroyAllWindows()
