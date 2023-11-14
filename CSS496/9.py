import argparse
import time
import numpy as np
import cv2


def sliding_window(image, stepSize, windowSize):
    for y in range(0, image.shape[0], stepSize):
        for x in range(0, image.shape[1], stepSize):
            yield (x, y, image[y : y + windowSize[1], x : x + windowSize[0]])


def non_max_suppression(boxes, overlapThresh):
    if len(boxes) == 0:
        return []

    pick = []

    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]

    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = np.argsort(y2)

    while len(idxs) > 0:
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)

        xx1 = np.maximum(x1[i], x1[idxs[:last]])
        yy1 = np.maximum(y1[i], y1[idxs[:last]])
        xx2 = np.maximum(x2[i], x2[idxs[:last]])
        yy2 = np.maximum(y2[i], y2[idxs[:last]])

        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)
        overlap = (w * h) / area[idxs[:last]]

        idxs = np.delete(
            idxs, np.concatenate(([last], np.where(overlap > overlapThresh)[0]))
        )
    return boxes[pick].astype["int"]


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
found = []
boundingboxes = []
color = [[0, 255, 0], [0, 0, 255], [255, 0, 0]]
i = 0

for (x, y, window) in sliding_window(img1, stepSize=16, windowSize=(winW, winH)):
    if window.shape[0] != winH or window.shape[1] != winW:
        continue

    patch = window.copy()

    maxV = correlation_coefficient(patch, img2)

    if maxV > 0.4:
        found.append(maxV)
        boundingboxes.append((x, y, x + winW, y + winH))
        print(found)

    clone = img1.copy()

    cv2.rectangle(clone, (x, y), (x + winW, y + winH), color[0], 2)
    vertical = np.vstack((img2, patch))
    cv2.imshow("Match", vertical)
    cv2.imshow("Window", clone)
    cv2.waitKey(1)
    time.sleep(0.025)

cv2.destroyAllWindows()

clone = image1.copy()

for startx, starty, endx, endy in boundingboxes:
    cv2.rectangle(clone, (startx, starty), (endx, endy), color[i], 2)
    i = i + 1

boundingboxes = np.array(boundingboxes)
print(boundingboxes)
pick = non_max_suppression(boundingboxes, 0.5)
print(pick)

for startX, startY, endX, endY in pick:
    cv2.rectangle(image1, (startX, startY), (endX, endY), (0, 255, 0), 2)

cv2.imshow("BeforeSuppress", clone)
cv2.imshow("AfterSuppress", image1)

key = cv2.waitKey(0) & 0xFF
if key == ord("q"):
    cv2.destroyAllWindows()
