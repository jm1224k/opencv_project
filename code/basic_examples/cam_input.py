import cv2

# webcam index
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Video", frame)
        if cv2.waitKey(33) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
