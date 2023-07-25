import cv2
from PIL import Image
from pytesseract import pytesseract


def textDetect():
    url = 'http://192.168.29.71:8080/video'
    camera = cv2.VideoCapture(url)

    while True:
        _, image = camera.read()
        cv2.imshow("Text Detection", image)

        if (cv2.waitKey(1) == 27):
            cv2.imwrite("text.jpg", image)
            break

    camera.release()

    cv2.destroyAllWindows()

    def demo():
        path_to_ter = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        path = "text.jpg"
        # sets the path to the Tesseract OCR engine executable for the
        # pytesseract library in Python.
        pytesseract.tesseract_cmd = path_to_ter
        text = pytesseract.image_to_string(Image.open(path))
        print(text)

    demo()
