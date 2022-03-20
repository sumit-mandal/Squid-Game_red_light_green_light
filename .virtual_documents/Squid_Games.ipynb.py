import cv2
from matplotlib import pyplot as plt
import os
import numpy as np
import time
from playsound import playsound


import os
os.listdir()





folderPath = 'images'
imglist = os.listdir(folderPath)
graphic = [cv2.imread(f'{folderPath}/{imPath}') for imPath in imglist]
green = graphic[0]
red = graphic[1]
kill = graphic[2]
winner = graphic[3]
intro = graphic[4]




plt.imshow(kill)
plt.title('kill')


plt.imshow(red)
plt.title('red')


plt.imshow(green)
plt.title('green')


plt.imshow(winner)
plt.title('winner')


plt.imshow(intro)
plt.title('intro')


cv2.imshow('Squid Game',cv2.resize(intro,(0,0),fx=0.5,fy=0.5))
cv2.waitKey(125)

playsound('music\squidWin.mp3')
cv2.destroyAllWindows()


while True:
    cv2.imshow('Squid Game',cv2.resize(intro,(0,0),fx=0.5,fy=0.5))
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        
cv2.destroyAllWindows()


TIMER_MAX = 10
TIMER = TIMER_MAX
maxMove = 6500000
font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)
frameHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) #Height of the frames in the video stream
frameWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH) #Width of the frames in the video stream


win = False


prev = time.time()
prevDoll = prev
showFrame = cv2.resize(green,(0,0),fx=0.5,fy=0.5)
isgreen = True


cv2.imshow('Squid Game',cv2.resize(intro,(0,0),fx=0.5,fy=0.5))
cv2.waitKey(125)

playsound('music\squidWin.mp3')
cv2.destroyAllWindows()

while True:
    cv2.imshow('Squid Game',cv2.resize(intro,(0,0),fx=0.5,fy=0.5))
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        
TIMER_MAX = 2
TIMER = TIMER_MAX
maxMove = 6500000
font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)
frameHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) #Height of the frames in the video stream
frameWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH) #Width of the frames in the video stream


win = False


prev = time.time()
prevDoll = prev
showFrame = cv2.resize(green,(0,0),fx=0.5,fy=0.5)
isgreen = True




while cap.isOpened() and TIMER >=0:
    ''' press 'w' to win'''
    
    if isgreen and (cv2.waitKey(10) & 0xFF == ord('w')):
        win = True
        break
        
    ret,frame = cap.read()
    cv2.putText(showFrame,str(TIMER),(50,50),font,1,(0, int(255*(TIMER)/TIMER_MAX),int(255*(TIMER_MAX-TIMER)/TIMER_MAX)),4,cv2.LINE_AA)
    
    # current time
    cur = time.time()
    
    
    # update and keep track of CountDown
    # if time elapsed is one second than decrease the counter
    
    if cur-prev >=1:
        prev = cur
        TIMER = TIMER-1
        if cv2.waitKey(10) & 0xFF == ord('w'):
            win = True
            break
            
        if isgreen:
            showFrame = cv2.resize(red,(0,0),fx=0.5,fy=0.5)
            print('is green true')
            isgreen = False
            ref = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


        else:
            showFrame = cv2.resize(green,(0,0),fx=0.5,fy=0.5)
            print('is green false')
            isgreen = True
            
            
    if not isgreen:
        
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frameDelta = cv2.absdiff(ref,gray)
        thresh = cv2.threshold(frameDelta,20,255,cv2.THRESH_BINARY)[1]
        change = np.sum(thresh)
        print('not is green')
        
        if change>maxMove:
            break
            
    else:
        
        if cv2.waitKey(10) & 0xFF == ord('w'):
            win = True
            break
        

        
    camShow = cv2.resize(frame,(0,0),fx=0.3,fy=0.3)
    
    camH,camW = camShow.shape[0],camShow.shape[1]
    showFrame[0:camH,-camW:] = camShow
    
    cv2.imshow('Squid Game',showFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        
    if isgreen and (cv2.waitKey(10) & 0xFF == ord('w')):
        win = True
        break
        
cap.release()

if not win:
    for i in range(10):
        print('killed')
        cv2.imshow('Squid Game',cv2.resize(kill,(0,0),fx=0.5,fy=0.5))
        
    playsound('music\kill.mp3')
    
    while True:
        cv2.imshow('Squid Game',cv2.resize(kill,(0,0),fx=0.5,fy=0.5))
        print('killed 2')
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
            
else:
    
    cv2.imshow('Squid Game',cv2.resize(winner,(0,0),fx = 0.5,fy=0.5))
    cv2.waitKey(125)
    playsound('music\win.mp3')
    
    
    while True:
        cv2.imshow('Squid Game',cv2.resize(winner,(0,0),fx=0.5,fy=0.5))
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break


cv2.destroyAllWindows()
    
    
        
            
            


cv2.imshow('Squid Game',cv2.resize(intro,(0,0),fx=0.5,fy=0.5))
cv2.waitKey(125)

playsound('music\squidWin.mp3')
cv2.destroyAllWindows()

while True:
    cv2.imshow('Squid Game',cv2.resize(intro,(0,0),fx=0.5,fy=0.5))
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        
TIMER_MAX = 10
TIMER = TIMER_MAX
maxMove = 6500000
font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)
frameHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) #Height of the frames in the video stream
frameWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH) #Width of the frames in the video stream


win = False


prev = time.time()
prevDoll = prev
showFrame = cv2.resize(green,(0,0),fx=0.5,fy=0.5)
isgreen = True




while cap.isOpened() and TIMER >=0:
    ''' press 'w' to win'''
    
    if isgreen and (cv2.waitKey(10) & 0xFF == ord('w')):
        win = True
        break
        
    ret,frame = cap.read()
    cv2.putText(showFrame,str(TIMER),(50,50),font,1,(0, int(255*(TIMER)/TIMER_MAX),int(255*(TIMER_MAX-TIMER)/TIMER_MAX)),4,cv2.LINE_AA)
    
    # current time
    cur = time.time()
    
    
    # update and keep track of CountDown
    # if time elapsed is one second than decrease the counter
    
    if cur-prev >=2:
        prev = cur
        TIMER = TIMER-1
        if cv2.waitKey(10) & 0xFF == ord('w'):
            win = True
            break
            
        if isgreen:
            showFrame = cv2.resize(red,(0,0),fx=0.5,fy=0.5)
            print('is green true')
            isgreen = False
            ref = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


        else:
            showFrame = cv2.resize(green,(0,0),fx=0.5,fy=0.5)
            print('is green false')
            isgreen = True
            
            
    if not isgreen:
        
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frameDelta = cv2.absdiff(ref,gray)
        thresh = cv2.threshold(frameDelta,20,255,cv2.THRESH_BINARY)[1]
        change = np.sum(thresh)
        print('not is green')
        
        if change>maxMove:
            break
            
    else:
        
        if cv2.waitKey(10) & 0xFF == ord('w'):
            win = True
            break
        

        
    camShow = cv2.resize(frame,(0,0),fx=0.3,fy=0.3)
    
    camH,camW = camShow.shape[0],camShow.shape[1]
    showFrame[0:camH,-camW:] = camShow
    
    cv2.imshow('Squid Game',showFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        
    if isgreen and (cv2.waitKey(10) & 0xFF == ord('w')):
        win = True
        break
        
cap.release()

if not win:
    for i in range(10):
        print('killed')
        cv2.imshow('Squid Game',cv2.resize(kill,(0,0),fx=0.5,fy=0.5))
        
    playsound('music\kill.mp3')
    
    while True:
        cv2.imshow('Squid Game',cv2.resize(kill,(0,0),fx=0.5,fy=0.5))
        print('killed 2')
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
            
else:
    
    cv2.imshow('Squid Game',cv2.resize(winner,(0,0),fx = 0.5,fy=0.5))
    cv2.waitKey(125)
    playsound('music\win.mp3')
    
    
    while True:
        cv2.imshow('Squid Game',cv2.resize(winner,(0,0),fx=0.5,fy=0.5))
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break


cv2.destroyAllWindows()
    
    
        
            
            






