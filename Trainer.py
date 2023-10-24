import os
import numpy as np
from PIL import Image
import cv2
import pickle

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceReconizer_create()

baseDir = os.path.dirname(os.path.abspath(__file__))  //obtenemos la ruta del directorio de trabajo
imageDir = os.path.join(baseDir,"images")     //directorio donde estan guardadas las imagenes

currentId = 1
labelIds = {}
yLabels = []
xTrain = []

for root,dirs,files in os.walk(imageDir):   //clasificador de imagenes(se combienten en matriz numpy)
	print(root,dirs,files)
	for file in files:
		print(file)
		if file.endswith("png") or file.endswith("jpg"):
			path = os.path.join(root,file)
			label = os.path.basename(root)
			print (label)

			if not label in labelIds:
				labelIds[label] = currentId
				print(labelIds)
				currentId += 1

				id = labelIds[label]
				pilImage = Image.open(path).convert("L")
				imageArray = np.array(pilImage,"uint8")
				faces = faceCascade.detectMultiScale(imageArray,scaleFactor = 1.1,minNeighbors = 5)  //re deteccion y aseguramiento de imagenes correctas

				for (x,y,w,h) in faces:
					roi = imageArray[y:y+h,x:x+w]
					xTrain.append(roi)
					yLabels.append(id_)

with open ("labels","wb")as f :
	pickle.dump(labelIds,f)
	f.close()

recognizer.train(xtrain.np.array(yLabels))   //entrenamiento de datos y guardado
recognizer.save("trainer.yml")
print(labelIds)