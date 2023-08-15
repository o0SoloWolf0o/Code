import cv2
# print(cv2.__version__)

img = cv2.imread('C:/Users/porpu/Desktop/Code/CSS496/geeks14.png', 0)

cv2.imshow('image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()