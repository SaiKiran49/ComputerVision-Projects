# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 18:01:13 2022

@author: sai
"""

import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self,mode=False,maxHands=2,mc=1,detectconf=0.5,trackconf=0.5):
        self.mode= mode
        self.hands= maxHands
        self.mc= mc
        self.det= detectconf
        self.trac= trackconf
        
        self.mphands = mp.solutions.hands
        self.hands1 = self.mphands.Hands(self.mode,self.hands,self.mc,self.det,self.trac)
        self.mpDraw= mp.solutions.drawing_utils
        
    def findhands(self,img,draw=True):
        imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.hands1.process(imgrgb)
        
        if self.results.multi_hand_landmarks:
           for eachhandlms in self.results.multi_hand_landmarks:
               if draw:
                  self.mpDraw.draw_landmarks(img, eachhandlms,self.mphands.HAND_CONNECTIONS)
                   
        return img
    
    def findposition(self, img, handno=0):
        lmlist=[]
        if self.results.multi_hand_landmarks:
           myHand = self.results.multi_hand_landmarks[handno]
           for id, lm in enumerate(myHand.landmark):
               h,w,c= img.shape
               cx,cy = int(lm.x*w),int(lm.y*h)
               lmlist.append([id,cx,cy])
        
        return lmlist
           
