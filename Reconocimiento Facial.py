import cv2
import theading
import numpy as np
import pickle
import RPi.GPIO as GPIO
import time
from picamera.array import PiRGBArray
from picamera import PiCamera


with open ('labels','rb')as f:  // se habre e importa el archivo tipo pickle.
	dicti = pickle.load(f)
	f.close()


def theadRelay():                            //definicion de HILO el cual se encarga de activar el relay
	relay_pin = [4]
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(relay_pin,GPIO.OUT)
	GPIO.output(relay_pin,1)
	time.sleep(5)
	GPIO.output(relay_pin,0)
	exit = True

camera = PiCamera()                         //configuracion de camara
camera.resolution =	(480,480)
camera.framerate = 30
rawCapture = PiRGBArray(camera,size =(480,480))



faceCascade = cv2.CascadeClassifier("haarcascade_frontal_default.xml")   //carga de clasificador y predictor
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")



font = cv2.FONT_HERSHEY_SIMPLEX                                      //fuente a utilizar



for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port = True):  //frame que se utiliza y configuracion
	frame = frame.array
	gray = cv2.cvtColot(frame.COLOR BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray,scaleFactor = 1.5 ,minNeighbors = 5)

	cv2.imshow('Reconocimiento facial',frame)                        // nombre asignado a frame
	key = cv2.waitKey(1)
	rawCapture.truncate(0)



	for (x,y,w,h) in faces :                                        //reconocimineto facial
		roiGray = gray[y:y+h,x:x+w]

		id_,conf = recognizer.predict(roiGray)

		for name,value in dicti.items():
			if value == id_:
				print(name)                                        //impresion de nombre reconocida

		if conf <= 70:                                             //si no detecta confiabilidad de sobre 70% no enciende relay
			Hilo = threading.thread(target = threadRellay)
			Hilo.start()


			if key == 27:
				break

cv2.destroyAllWindows()