import cv2 as cv


#'DogAndCat-Face-Opencv-master/Cat_dog_face/dog_face.xml'
harcascade = 'DogAndCat-Face-Opencv-master/Cat_dog_face/dog_face.xml'
#'dogs_75/Anahi/Anahi 1.jpeg'
#'dogs_75/Alexy/Alexy 1.jpeg'
image = 'dogs_75/Alexy/Alexy 1.jpeg'

# Carregando o classificador de faces
face_cascade = cv.CascadeClassifier(harcascade)

# Lendo a imagem
img = cv.imread(image)

#Tranformando a imagem em cinza
img_cinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detectando faces na imagem
faces = face_cascade.detectMultiScale(img_cinza)

print(faces)

for(x, y, w, h) in faces:
    cv.rectangle(img, (x , y), (x + w, y + h), (0,255,0), 2)

cv.imshow("Faces", img)
cv.waitKey()







