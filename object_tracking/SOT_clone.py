import cv2
import sys

if __name__ == '__main__':
    video = cv2.VideoCapture(0)

    # Init the tracker
    tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
    tracker_type = tracker_types[0]
    # traker = cv2.trackerKCF_create()

    ok, frame = video.read()

    if not ok:
        print("Cant read the webcam")
        sys.exit()

    frame = cv2.flip(frame, 1)
    print("haha")
    bbox = cv2.selectROI(frame, True)
