import cv2

#%matplotlib inline
from matplotlib import pyplot as plt

car_cascade = cv2.CascadeClassifier('../data/cars.xml')

cap = cv2.VideoCapture("../data/KM84.mp4")
while not cap.isOpened():
    cap = cv2.VideoCapture("../data/KM84.mp4")
    cv2.waitKey(1000)
    print "Wait for the header"

pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
while True:
    ncars = 0
    flag, frame = cap.read()
    if flag:
        # The frame is ready and already captured
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)

        # Draw border
        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
            ncars = ncars + 1

        plt.figure(figsize=(10,20))
        # plt.imshow(frame)

        # find the speed

        cv2.imshow('video', frame)
        pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
        print str(pos_frame)+"frames"
        print "ncars : " + str(ncars)
    else:
        # The next frame is not ready, so we try to read it again
        cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos_frame-1)
        print "frame is not ready"
        # It is better to wait for a while for the next frame to be ready
        cv2.waitKey(1000)

    if cv2.waitKey(10) == 27:
        break
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        # If the number of captured frames is equal to the total number of frames,
        # we stop
        break
