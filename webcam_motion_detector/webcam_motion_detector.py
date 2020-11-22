import cv2
import pandas as pd
from datetime import datetime


class MotionDetector:
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.motion_list = [None, None]
        self.times = []
        self.df = pd.DataFrame(columns=["Start", "End"])

    def capture_video(self):
        first_frame = None

        while True:
            check, frame = self.video.read()

            motion = False

            if not check:
                raise ("Acquring Video stream failed!")

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)

            if first_frame is None:
                first_frame = gray
                continue

            delta_frame = cv2.absdiff(first_frame, gray)
            thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
            thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

            (cnts, _) = cv2.findContours(
                thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
            )

            for contour in cnts:
                if cv2.contourArea(contour) < 3000:
                    continue

                motion = True

                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

            self.motion_list.append(motion)

            if self.motion_list[-1] == True and self.motion_list[-2] == False:
                self.times.append(datetime.now())
            if self.motion_list[-1] == False and self.motion_list[-2] == True:
                self.times.append(datetime.now())

            cv2.imshow("Gray Frame - press 'q' to exit", gray)
            cv2.imshow("Delta Frame - press 'q' to exit", delta_frame)
            cv2.imshow("Threshold Frame - press 'q' to exit", thresh_frame)
            cv2.imshow("Contour Frame - press 'q' to exit", frame)

            key = cv2.waitKey(1)

            if key == ord("q"):
                if motion == True:
                    self.times.append(datetime.now())
                break

        print(len(self.times))
        for i in range(0, len(self.times), 2):
            if (self.times[i + 1] - self.times[i]).total_seconds() > 0.8:
                self.df = self.df.append(
                    {"Start": self.times[i], "End": self.times[i + 1]},
                    ignore_index=True,
                )

        print(self.df)

        self.video.release()
        cv2.destroyAllWindows


if __name__ == "__main__":
    md = MotionDetector()
    md.capture_video()
