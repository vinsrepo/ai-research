import keras
import numpy as np
import cv2
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image to be scanned")
args = vars(ap.parse_args())

def load_images(image_paths, image_size):
    loaded_images = []
    loaded_image_paths = []

    for i, img_path in enumerate(image_paths):
        try:
            image = cv2.imread(img_path)
            image = cv2.resize(image,(256, 256))
            image = image/255.0
            loaded_images.append(image)
            loaded_image_paths.append(img_path)
        except Exception as ex:
            print(i, img_path, ex)
    
    return np.asarray(loaded_images), loaded_image_paths

class Classifier():
    '''
        Class for loading model and running predictions.
        For example on how to use take a look the if __name__ == '__main__' part.
    '''
    nsfw_model = None

    def __init__(self, model_path):
        Classifier.nsfw_model = keras.models.load_model(model_path) # khởi tạo model


    def classify(self, image_paths = [], batch_size = 32, image_size = (256, 256), categories = ['unsafe', 'safe']):
        if isinstance(image_paths, str):
            image_paths = [image_paths]

        loaded_images, loaded_image_paths = load_images(image_paths, image_size) #load data
        
        if not loaded_image_paths:
            return {}

        model_preds = Classifier.nsfw_model.predict(loaded_images, batch_size = batch_size) # sử dụng model để predict

        return model_preds


if __name__ == '__main__':
    weights_path = "classifier_model"
    m = Classifier(weights_path)
    result = m.classify(args["image"])
    # result = m.classify("C:/Users/anlan/OneDrive/Desktop/detect_image_toxic/00000001.jpg")
    if result[0] > result[1]:
        print("toxic")
    else: print("no toxic")