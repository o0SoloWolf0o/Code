import sys
import os
import cv2
import numpy as np
import argparse

import sklearn.preprocessing import LabelEncoder
import sklearn.neighbors import KNeighborsClassifier
import sklearn.model_selection import train_test_split
import sklearn.metrics import classification_report

class DatasetLoad:
    def __init__(self,width =64,height=64, pre_type = 'Resize'):
        self.width = width
        self.height = height
        self.pre_type = pre_type
    
    def load(self, pathes, verbose = -1):
        datas = []
        labels = []
        
        mainfolders = os.listdir(pathes)
        
        for folder in mainfolders:
            fullpath = os.path.join(pathes, folder)
            listfiles = os.listdir(fullpath)
            
            if verbose > 0:
                print('[INFO] loading ', folder, ' ...')
            for (i, imagefile) in enumerate(listfiles):
                imagepath = pathes + '/' + folder + '/' + imagefile
                image = cv2.imread(imagepath)
                label = folder
                if(self.pre_type == 'Resize'):
                    image = cv2.resize(image, (self.width, self.height), interpolation=cv2.INTER_AREA)
                datas.append(image)
                labels.append(label)
                
                if verbose > 0 and i > 0 and (i+1) % verbose == 0:
                    print('[INFO] processed {}/{}'.format(i+1, len(listfiles)))
        return (np.array(datas), np.array(labels))

ap = argparse.ArgumentParser()
ap.add_argument('-d', '--dataset', required=True, help='path to input dataset')
ap.add_argument('-k', '--neighbors', type=int, default=1, help='# of nearest neighbors for classification')
args = vars(ap.parse_args())

pathes = args['dataset']
k = args['neighbors']

width = 64
height = 64

data = DatasetLoad(width, height)
print('[INFO] loading datasets...')

label = ['cat', 'dog', 'panda']
datas, labels = data.load(pathes, verbose=500)

print('[INFO] shape of datasets: ', datas.shape)

flat_image = datas.shape[1]*datas.shape[2]*datas.shape[3]
datas = datas.reshape((datas.shape[0], flat_image))
print('[INFO] new datas shape', datas.shape)

print("[INFO] features matrix: {:.1f}MB".format(datas.nbytes / (1024 * 1000.0)))

le = LabelEncoder()
labels = le.fit_transform(labels)

print('[INFO] split dataset to training and testing...')
(trainX, testX, trainY, testY) = train_test_split(datas, labels, test_size=0.25)

print('[INFO] evaluating k-NN classifier...')

model = KNeighborsClassifier(n_neighbors=k)
model.fit(trainX, trainY)

print(classisfication_report(testY, model.predict(testX), target_names=le.classes_))

print('[INFO] Call some image to test ...')
path = 'datasets/animals/dogs'

listfiles = os.listdir(path)
for (i, imagefile) in enumerate(listfiles):
    imagepath = path + '/' + imagefile
    image = cv2.imread(imagepath)
    img = image.copy()
    img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
    img = img.reshape((1, width*height*3))
    pred = model.predict(img)
    cv2.putText(image, "Label: {}".format(label[pred[0]]), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    cv2.imshow("Org", image)
    
    key = cv2.waitKey(1000)&0xFF
    if key == ord('q'):
        break