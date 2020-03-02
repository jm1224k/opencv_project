import cv2

# not frame, but information about input video. it has frame setting, codec, etc.
capture = cv2.VideoCapture("../video/suda.mp4")

while True:
    # in video, ret = bool --> is correct frame when you read in capture variable, frame = current frame
    ret, frame = capture.read()

    # current frame number is equal to total video frame
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.open("../video/suda.mp4")

    # show video and if you push 'q', video will stop
    # FPS(frame per second) = 1000/interval = 1000/33
    cv2.imshow("Video", frame)
    if cv2.waitKey(33) == ord('q'):
        break

# free memory
capture.release()
cv2.destroyAllWindows()
