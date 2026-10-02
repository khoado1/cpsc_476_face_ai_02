from djitellopy import tello
import cv2
from cvzone.FaceDetectionModule import FaceDetector


detector = FaceDetector()
while True:
    #img = me.get_frame_read().frame
    #img, bboxs = detector.findFaces(img, draw=True)
    # cv2.imshow("Image", img)
    # if cv2.waitKey(5) & 0xFF == ord('q'):
    #     break
    cv2.destroyAllWindows()