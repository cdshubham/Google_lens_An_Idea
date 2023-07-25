import cv2
from PIL import Image
from pytesseract import pytesseract
import gtts
import playsound


def textToAudio():
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
        pytesseract.tesseract_cmd = path_to_ter
        text = pytesseract.image_to_string(Image.open(path))
        print(text)
        return text

    text = demo()
    sound = gtts.gTTS(text, lang="en")
    sound.save("audio.mp3")
    playsound.playsound("audio.mp3")
