import tensorflow as tf
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import os
import numpy as np 
import cv2

class numberGuesser:
    checkpointpath = "training.ckpt"
    def buildModel(self):
        (train_x,train_y), (test_x, test_y) = tf.keras.datasets.mnist.load_data()

        train_x, test_x = train_x / 255.0, test_x / 255.0
        
        model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(512,activation=tf.nn.relu),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(10,activation=tf.nn.softmax)
        ])

        model.compile (optimizer= 'adam', loss='sparse_categorical_crossentropy', metrics = ['accuracy'])

        try:
            model.load_weights("training.ckpt")
        except:    
            model.fit(train_x, train_y, batch_size=32, epochs=100)  
            checkpointpath = "training.ckpt"
            checkpoint_dir = os.path.dirname(checkpointpath)

            cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpointpath, save_weights_only=True, verbose=1)

            model.save_weights(checkpointpath.format(epoch=0))  
        
        model.evaluate(test_x, test_y)
        
        return model

    def guessNumber(self):
        try:
            model = self.buildModel()
            
            #OPEN IMAGE
            image = Image.open("number.png")
            #CROP
            image = image.crop((0,0,500,500))
            #MAKE IT SMALLER AND SAVE IT
            image.thumbnail((28,28), Image.ANTIALIAS)
            image.save("Converted.png")
            #OPEN IT and MAKE TO GRAY SCALE
            image = cv2.imread('Converted.png')
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            #Chage Shape and make it into array
            image.shape = (1,28,28)
            im = np.asarray(image)
                        
            for x in range(28):
                for y in range(28):
                    if im[0][x][y] == 255:
                        im[0][x][y] = 0    
            
            im = im / 255.0
            
            prediction = model.predict(im)
            prediction = np.argmax(prediction)
            return prediction
        except :
            model = self.buildModel()
            
            #OPEN IMAGE
            image = Image.open("number.png")
            #CROP
            image = image.crop((0,0,500,500))
            #MAKE IT SMALLER AND SAVE IT
            image.thumbnail((28,28), Image.ANTIALIAS)
            image.save("Converted.png")
            #OPEN IT and MAKE TO GRAY SCALE
            image = cv2.imread('Converted.png')
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            #Chage Shape and make it into array
            image.shape = (1,28,28)
            im = np.asarray(image)
                        
            for x in range(28):
                for y in range(28):
                    if im[0][x][y] == 255:
                        im[0][x][y] = 0    
            
            im = im / 255.0
            
            prediction = model.predict(im)
            prediction = np.argmax(prediction)
            return prediction
            