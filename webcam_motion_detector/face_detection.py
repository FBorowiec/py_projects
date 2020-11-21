import cv2


class FaceDetector:
    def __init__(self, image):
        self.face_cascade = cv2.CascadeClassifier(
            "webcam_motion_detector/haarcascade_frontalface_default.xml"
        )
        self.img = cv2.imread("webcam_motion_detector/" + image + ".jpg")
        self.grayscale_image()
        self.detect_faces()
        self.print_image()

    def grayscale_image(self):
        try:
            self.gray_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        except:
            self.gray_img = self.img

    def detect_faces(self):
        self.faces = self.face_cascade.detectMultiScale(
            self.gray_img, scaleFactor=1.2, minNeighbors=5
        )

        for x, y, w, h in self.faces:
            self.img = cv2.rectangle(self.img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    def print_image(self):
        cv2.imshow("Detected Faces", self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    FaceDetector("picture")
