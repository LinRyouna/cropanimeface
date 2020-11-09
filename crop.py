import glob 
import cv2
import sys
import os
import random 
def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier("lbpcascade_animeface.xml")
    #faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = face_cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor = 1.1,
                                     minNeighbors = 3,
                                     minSize = (50, 50))
    return faces

filename = input("Enter the file name in which images are present =")

for img in glob.glob(filename+'/*.*'):
    var_img = cv2.imread(img)
    face = detect_face(var_img)
    print(face)
    if (len(face) == 0):
        continue
    #i=0
    for(ex, ey, ew, eh) in face:
        crop_image = var_img[ey:ey+eh, ex:ex+ew]
        #i=i+1
        ##cv2.imshow("cropped", crop_image)
        #cv2.waitKey(0)  
        cv2.imwrite("NyaH"+str(random.randint(1,999999999999))+".png", crop_image)
        #i=i+1
        #cv2.imshow("cropped", crop_image)
        #cv2.waitKey(0)  
    