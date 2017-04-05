import cv2
import sys
import time
import threading
from SoloCamera import SoloCamera

#open HDMI-In as a video capture device
video_capture = SoloCamera()

#HDMI-In uses a ring buffer that stops grabbing new frames once full
#so this allows us to remove excess frames that we aren't using
CLEAR_EXTRA_FRAMES = True
kill_thread = False

def clear_frames():
    while kill_thread is False:
        video_capture.clear()
#start a background thread to clear frames
if CLEAR_EXTRA_FRAMES:
    thr = threading.Thread(target=clear_frames)
    thr.start()
try:
    while True:
        start = time.time()
        # Capture a grayscale image
        ret, frame = video_capture.read()
        cv2.imwrite("a.jpg", frame)
        time.sleep(1)
except KeyboardInterrupt:
    kill_thread = True
