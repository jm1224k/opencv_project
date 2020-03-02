import cv2

img = cv2.imread("../img/do-il.jpeg", flags=cv2.IMREAD_COLOR)

cv2.namedWindow("do-il", flags=cv2.WINDOW_FREERATIO)
cv2.imshow("do-il", img)
cv2.waitKey(0)
cv2.destroyWindow("do-il")
