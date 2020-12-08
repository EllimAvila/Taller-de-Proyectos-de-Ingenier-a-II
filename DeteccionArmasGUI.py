# -*- coding: utf-8 -*-
"""
Elaborado por:
    Avila Zambrano Ellim
    Parado Sulca Yurgen
    Rodriguez Manuelo Jhoelver
"""
import cv2
import imutils
import numpy as np
import random
import time
import json
import requests
    
def generarReporteDelito(url, ID_Camara,ID_Usuario,RD_Descripcion,RD_Fecha_Hora,
                         RD_Tipo_Delito,RD_Lugar_Delito,RD_Latitud,RD_Longitud):
    cuerpoJson={"ID_Camara":ID_Camara,
    "ID_Usuario":ID_Usuario,
    "RD_Descripcion":RD_Descripcion,
    "RD_Fecha_Hora":RD_Fecha_Hora,
    "RD_Tipo_Delito":RD_Tipo_Delito,
    "RD_Lugar_Delito":RD_Lugar_Delito,
    "RD_Latitud":RD_Latitud,
    "RD_Longitud":RD_Longitud
    }
    _headers={'Content-Type':'application/json; charset=UTF-8'}
    respuesta=requests.post(url, data=json.dumps(cuerpoJson), headers=_headers)
    desglozar=respuesta.json()
    print(desglozar['message']+'camara '+str(ID_Camara))

def numTexto(comprobar):
    if comprobar.isdigit()==True:
        comprobar=int(comprobar)
    return comprobar

with open('Fuentes/fuentes.json') as file:
    fuentes = json.load(file)
    
with open('Fuentes/id.json') as file:
    idUsuario = json.load(file)
    
fuente1=int(fuentes['fuenteCamara1'])
fuente2=int(fuentes['fuenteCamara2'])

idParam=idUsuario['idUsuario']

latCam1=fuentes['latCam1']
lonCam1=fuentes['lonCam1']
latCam2=fuentes['latCam2']
lonCam2=fuentes['lonCam2']

# fuente1=numTexto(fuente1) 
# fuente2=numTexto(fuente2)

camara1 = cv2.VideoCapture(fuente1, cv2.CAP_DSHOW)
camara2 = cv2.VideoCapture(fuente2, cv2.CAP_DSHOW)

#Cámara IP
# camara1=cv2.VideoCapture('http://192.168.0.21:4747/video') 

detector_armas = cv2.CascadeClassifier('cascade2.xml')
ventanaControl=None
paramTrigger='0'

# LOCAL
# urlInsert ="http://localhost/SmartCity-main/ReporteDelito/insertar_delito.php" 
# SERVIDOR
urlInsert ='http://smartcityhyo.tk/api/ReporteDelito/insertar_delito.php'

ruta="Capturas/"



formato=".png"
codigoImagen = str(random.randrange(99999))
#num=hora+fecha
nombreimagen= codigoImagen

#def generarRegistro(param):

while True:
    
    recibe1,fotograma1 = camara1.read()
    recibe2,fotograma2 = camara2.read()
    
    
    grises1 = cv2.cvtColor(fotograma1, cv2.COLOR_BGR2GRAY)
    grises2 = cv2.cvtColor(fotograma2, cv2.COLOR_BGR2GRAY)
    
    toy1 = detector_armas.detectMultiScale(grises1,
    scaleFactor = 10,
    minNeighbors = 95,
    minSize=(60,68))
    toy2 = detector_armas.detectMultiScale(grises2,
    scaleFactor = 8,
    minNeighbors = 100,
    minSize=(60,68))
    
    alerta=0
    
    for (x,y,w,h) in toy1:
        cv2.rectangle(fotograma1, (x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(fotograma1,'Pistola',(x,y-10),2,0.7,(255,0,0),2,cv2.LINE_AA)
        cv2.putText(ventanaControl,'Posible actividad delictiva',(10,260),1,1,(0,0,255),1,cv2.LINE_AA)
        cv2.putText(ventanaControl,'en la camara 1',(10,300),1,1,(0,0,255),1,cv2.LINE_AA)
        cv2.rectangle(ventanaControl,(8,80),(360,120),(0,255,255),2)
        alerta=1
    for (x,y,w,h) in toy2:
        cv2.rectangle(fotograma2, (x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(fotograma2,'Pistola',(x,y-10),2,0.7,(255,0,0),2,cv2.LINE_AA)
        cv2.putText(ventanaControl,'Posible actividad delictiva',(10,260),1,1,(0,0,255),1,cv2.LINE_AA)
        cv2.putText(ventanaControl,'en la camara 2',(10,300),1,1,(0,0,255),1,cv2.LINE_AA)
        cv2.rectangle(ventanaControl,(8,160),(360,200),(0,255,255),2)
        alerta=1
    
    fotograma1=imutils.resize(fotograma1,width=500)
    fotograma2=imutils.resize(fotograma2,width=500)
    
    if np.all(ventanaControl) is None:
        ventanaControl=np.zeros(fotograma1.shape,dtype=np.uint8)
    if alerta == 0:
        ventanaControl=np.zeros(fotograma1.shape,dtype=np.uint8)
        
    vista_camaras=cv2.hconcat([fotograma1,fotograma2])
    #vista_camaras=cv2.hconcat([vista_camaras,ventanaControl])
    
    
    fecha=time.strftime("%x %X")
    fechaEnviar=time.strftime("%y-%m-%d %H:%M:%S")
    
    
    cv2.putText(vista_camaras,'Camara 1',(10,20),2,0.7,(0,0,255),2,cv2.LINE_AA)
    cv2.putText(vista_camaras,'Camara 2',(510,20),2,0.7,(0,0,255),2,cv2.LINE_AA)
    cv2.putText(vista_camaras,fecha,(600,350),2,1,(0,0,255),2,cv2.LINE_AA)
    
    cv2.putText(ventanaControl,'Camaras',(10,20),2,0.7,(0,255,0),2,cv2.LINE_AA)
    cv2.putText(ventanaControl,'Camara 1 --> presione "1" para acceder',(10,100),1,1,(0,255,0),1,cv2.LINE_AA)
    cv2.putText(ventanaControl,'Camara 2 --> presione "2" para acceder',(10,180),1,1,(0,255,0),1,cv2.LINE_AA)
    
    cv2.imshow('Detector de Armas',vista_camaras)
    cv2.imshow('Panel de control',ventanaControl)
    
    k = cv2.waitKey(1)
    if k == 49:
        aux1=fotograma1
        aux1=imutils.resize(aux1,width=800)
        cv2.imshow('Camara 1',aux1)
        paramTrigger='1'
    if k == 50:
        aux2=fotograma2
        aux2=imutils.resize(aux2,width=800)
        cv2.imshow('Camara 2',aux2)
        paramTrigger='2'
    if cv2.waitKey(1)==ord('q'):
        if paramTrigger == '1':
            codigoImagen = str(random.randrange(99999))
            cv2.putText(aux1,fecha,(20,530),2,1,(0,0,255),2,cv2.LINE_AA)
            cv2.imwrite(ruta+(codigoImagen+'_camara1'+formato),aux1)
            generarReporteDelito(urlInsert, 1, idParam, codigoImagen, fechaEnviar, 'Asalto', 'San Carlos',latCam1,lonCam1)
            print(idParam)
        elif paramTrigger=='2':
            codigoImagen = str(random.randrange(99999))
            cv2.putText(aux2,fecha,(20,530),2,1,(0,0,255),2,cv2.LINE_AA)
            cv2.imwrite(ruta+(codigoImagen+'_camara2'+formato),aux2)
            generarReporteDelito(urlInsert, 2, idParam, codigoImagen, fechaEnviar, 'Asalto', 'El Tambo',latCam2,lonCam2)
            print(idParam)
    if cv2.waitKey(1) == 27:
        break
camara1.release()
camara2.release()
cv2.destroyAllWindows()










