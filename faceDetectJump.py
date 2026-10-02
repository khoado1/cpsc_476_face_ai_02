from typing import cast

from djitellopy import tello
import cv2
from cvzone.FaceDetectionModule import FaceDetector
import time

# Step 4 is a bit challenging. 

# need to develop a program (called faceDetectJump.py). In this program, 

# the drone takes off first and
# detects a face. 
# Once detected, 
#   the drone flies a bit higher for 3 seconds and 
#   then back down to the original elevation. 
# When the key q (on the laptop) is pressed, the drone lands.

me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamoff()
me.streamon()

detector = FaceDetector()

# the drone takes off first and
me.takeoff()

while True:
    # detects a face. 
    img = me.get_frame_read().frame
    img, bboxs = detector.findFaces(img, draw=True)
    if bboxs:
        # Once detected, 
        #   the drone flies a bit higher for 3 seconds and 
        #   then back down to the original elevation. 
        me.move_up(30)
        time.sleep(3)
        me.move_down(30)

    cv2.imshow("Image", cast(cv2.typing.MatLike, img))

    # When the key q (on the laptop) is pressed, the drone lands.
    if cv2.waitKey(5) & 0xFF == ord('q'):
        me.land()
        break
cv2.destroyAllWindows()