from cvzone.ClassificationModule import Classifier
import cv2


def ImageClassify():
    cap = cv2.VideoCapture(0)
    myClassifier = Classifier("keras_model.h5", "labels.txt")

    while True:
        _, img = cap.read() 
        prediction, index = myClassifier.getPrediction(img)
        cv2.imshow("image", img)
        if (cv2.waitKey(1) == 27):
            break
