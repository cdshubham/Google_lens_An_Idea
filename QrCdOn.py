import cv2
import webbrowser


def hell():
    # Capturing Video
    cap = cv2.VideoCapture(0)
    # Create instance of QR Code Detector
    detector = cv2.QRCodeDetector()

    while (True):
        _, img = cap.read()
        # return info,coordinates,extra info
        data, one, _ = detector.detectAndDecode(img)

        if (data):
            a = data
            break
        cv2.imshow("QrCode", img)
        if (cv2.waitKey(1) == ord('q')):
            break

    b = webbrowser.open(str(a))
    cap.release()
    cv2.destroyAllWindows()
