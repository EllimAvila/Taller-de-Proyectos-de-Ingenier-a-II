# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:57:44 2019

@author: seraj
"""
import time
import cv2 
from flask import Flask, render_template, Response

detector_armas = cv2.CascadeClassifier('cascade2.xml')

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen():
    """Video streaming generator function."""
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # Read until video is completed
    while(cap.isOpened()):
      # Capture frame-by-frame
        ret, fotograma = cap.read()
        grises = cv2.cvtColor(fotograma, cv2.COLOR_BGR2GRAY)
        toy1 = detector_armas.detectMultiScale(grises,
                                               scaleFactor = 10,
                                               minNeighbors = 95,
                                               minSize=(60,68))
        for (x,y,w,h) in toy1:
            cv2.rectangle(fotograma, (x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(fotograma,'Pistola',(x,y-10),2,0.7,(255,0,0),2,cv2.LINE_AA)
            
        if ret == True:
            fotograma = cv2.resize(fotograma, (0,0), fx=1, fy=1) 
            frame = cv2.imencode('.jpg', fotograma)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            cv2.waitKey(0)
        else: 
            break
        

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

    

