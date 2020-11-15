import cv2

# Lee la imagen
img = cv2.imread('C:/Users/Adrian/Pictures/Captura.png')
print(img.shape)
#  Redimensiona la imagen
imgResize = cv2.resize(img, (200,300))
print(imgResize.shape)
# Recorta la imagen
imgCropped = img[0:200,50:300]

cv2.imshow("Image", img)
#cv2.imshow("Image resize", imgResize)
cv2.imshow("Image cropped", imgCropped)
cv2.waitKey(0)