from configparser import Interpolation
from tkinter import font
from turtle import distance
import cv2
import math
import pygame
distance = 0.0
font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while True:
    ret, huge_frame = cap.read()
    frame = cv2.resize(huge_frame, (1080,720), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        distancei = (2*3.14 * 180)/(w+h*360)*1000 + 3
        print (distancei)
        distance = int(distancei*2.54)
        #distance = math.floor(distancei/2)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.putText(frame, 'Jarak = ' + str(distance) + ' Cm', (5,100), font, 1,(255,255,255),2)
    if distance <= 26:
        pygame.mixer.init()
        pygame.mixer.music.load('beep.wav')
        pygame.mixer.music.play()
        cv2.putText(frame, 'PERINGATAN!', (500,40), font, 0.5, (0,191,255),2)
        cv2.putText(frame, 'JARAK MATA ANDA TERLALU DEKAT DENGAN LAYAR MONITOR', (500,60), font, 0.4, (0,0,255),2)
    cv2.imshow('face detection', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



