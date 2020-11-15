import cv2

# activar webcam
vid = cv2.VideoCapture(0)
vid.set(3,640)
vid.set(4,480)
vid.set(10,100)
while True:
    success, img = vid.read()
    cv2.imshow("video",img)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()