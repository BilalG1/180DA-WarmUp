import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame_threshold = cv2.inRange(frame_HSV, (100, 20, 20), (380, 100, 80))

    # ret,thresh = cv2.threshold(gray,127,255, cv2.THRESH_TRUNC)
    contours,hierarchy = cv2.findContours(frame_threshold, 1, 2)
    maxSize = 0
    cntStore = 0
    for cnt in contours:
      x, y, w, h = cv2.boundingRect(cnt)
      if (w*h > maxSize):
        cntStore = cnt

    x1,y1 = cntStore[0][0]
    cv2.putText(frame_threshold, 'Rectangle', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (180, 180, 180), 2)
    frame_threshold = cv2.cvtColor(frame_threshold, cv2.COLOR_GRAY2BGR)
    frame_threshold = cv2.drawContours(frame_threshold, [cntStore], -1, (0,255,0), 3)
    cv2.imshow('frame',frame_threshold)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()