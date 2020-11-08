import cv2
import sys
import os.path

def detect(cascade_file, filename, outputname):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    

    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor = 1.1,
                                     minNeighbors = 5,
                                     minSize = (250, 250))
    i=0
    for (x, y, w, h) in faces:
        cropped = image[y: y + h, x: x + w]
        cv2.imwrite(outputname+str(i)+".png", cropped)
        i=i+1

if len(sys.argv) != 4:
    sys.stderr.write("usage: detect.py <animeface.xml file>  <input> <output prefix>\n")
    sys.exit(-1)

detect(sys.argv[1], sys.argv[2], sys.argv[3])