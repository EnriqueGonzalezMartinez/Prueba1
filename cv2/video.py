import cv2

# Abre un video
vid = cv2.VideoCapture("C:/Users/Adrian/Videos/video.mp4")
while True:
    success, img = vid.read()
    cv2.imshow("video",img)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()