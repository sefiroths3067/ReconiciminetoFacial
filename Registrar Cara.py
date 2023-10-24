import cv2
from picamera.array import PIRGBArray
from picamera import PiCamera
import numpy as np
import os
import sys

camera = PiCamera()                  //inicializar objeto camara
camera =.resolution = (640,480)      //ajuste de resolucion de camara
camera.framerate = 30                // ajuste frames de camara
rawCapture = PiRGBArray(camera, size=(640, 480))    //entrega matriz tridimencional

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

name = imput("ingrese el nombre de la persona :")   //se solicita a usuario nombre 
dirName= "./images/"+ name
print(dirName)
if not os.path.exists(dirName):
	os.makedirs(dirName)
	print("se ha creado el diectorio con exito. ")
else:
	print("Esta persona ya se encuentra registrada.")
	sys.exit()
count = 1
for frame in camera.capture_continuous(rawCapture,format="brg",use_video_port= True):  //se inicia la captura continua
	if count > 30:
		break
		frame = frame.array           //se llama funcion de clasificador
		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  //1er argumento imagen a escala de grises
		faces = faceCascade.detectMultiScale(gray,scaleFactor = 1.5,minNeighbors = 5) //2do parametro que ajusta escala de imagen,3er argumento parametro cuantos vecinos vediesen tener cada rectangulo,un numero mas alto da menos falsos positivos
		for (x,y,w,h) in faces:                            //coordenadas rectangulares del area de la cara para extraer la cara de la imagen
			roiGray = gray[y:y+h,x:x+w]
			filename = dirName +"/"+ name + str(count) + ".jpg"
			cv2.imwrite(fileName,roiGray)
			cv2.imshow("face",roiGray)
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
			count += 1

		cv2.imshow('frame',frame)     // se muestra marco original en la ventana de salida
		key = cv2.waitKey(1)         // espera funcion de algun teclado
		rawCapture.truncate(0)        //nos ayuda a preparar el siguente cuadro o capturas

		if key == 27:
			break
