# from utils import sliding_window
import argparse
import time
import numpy as np 
import cv2

def sliding_window(image, stepSize, windowSize):
    for y in range(0, image.shape[0], stepSize):
        for x in range(0, image.shape[1], stepSize):
            yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])

def correlation_coefficient(patch1, patch2):
    product = np.mean((patch1 - patch1.mean()) * (patch2 - patch2.mean()))
    stds = patch1.std() * patch2.std()
    if stds == 0:
        return 0
    else:
        product /= stds
        return product

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-s", "--simage", required=True, help="Path to the image")
args = vars(ap.parse_args())

image1 = cv2.imread(args["image"])
image2 = cv2.imread(args["simage"])

img1 = cv2.cvtColor(image1, cv2.COLOR_RGB2GRAY)
img2 = cv2.cvtColor(image2, cv2.COLOR_RGB2GRAY)

(winH, winW) = img2.shape
found = None

for (x,y,window) in sliding_window(img1, stepSize = 16, windowSize = (winW,winH)):
    if window.shape[0] != winH or window.shape[1] != winW:
        continue
    
    patch = window.copy()
    
    maxV = correlation_coefficient(patch, img2)
    
    if found is None or maxV > found:
        found = maxV
        outx = x
        outy = y
        print(found)
    
    clone = img1.copy()
    
    cv2.rectangle(clone, (x,y),(x + winW, y + winH), (0,255,0),2)
    vertical = np.vstack((img2, patch))
    cv2.imshow("Match", vertical)
    cv2.imshow("Window", clone)
    cv2.waitKey(1)
    time.sleep(0.025)

cv2.destroyAllWindows()

patch = image1[outy:outy+winH,outx:outx+winW,:]

cv2.rectangle(image1, (outx,outy),(outx+ winW,outy+winH),(0,255,0),2)
vertical = np.vstack((image2,patch))
cv2.imshow("Match", vertical)
cv2.imshow("Final", image1)
key = cv2.waitKey(0) &0xFF

if key == ord("q"):
    cv2.destroyAllWindows()