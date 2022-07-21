# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 09:46:48 2022

@author: sai
"""

import cv2
import mediapipe as mp
import time
import HandtrackingModule as htm
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

detector = htm.handDetector()

tips= [4,8,12,16,20]

while True:
      success, img = cap.read()
      img = detector.findhands(img)
      lmlist = detector.findposition(img)
      if len(lmlist)!=0:
         if lmlist[0][2]> lmlist[6][2]:
            fingerlist=[]
            if lmlist[4][1]> lmlist[2][1]:
                fingerlist.append(1)
            else :
                fingerlist.append(0)
            for id in range(1,5):  
                if lmlist[tips[id]][2]< lmlist[tips[id]-2][2]:
                   fingerlist.append(1)
                else:
                   fingerlist.append(0)
            a=fingerlist.count(1)
            cv2.rectangle(img, (0,0), (100,100),(0,255,0),cv2.FILLED)
            cv2.putText(img, str(a),(30,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
            
      
      cv2.imshow('FINGERCOUNTER', img)
      
      if cv2.waitKey(1) & 0xFF ==27:
         break
     
        
cap.release()
cv2.destroyAllWindows()
