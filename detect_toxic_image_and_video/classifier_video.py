# py classifier_video.py --video C:/Users/anlan/OneDrive/Desktop/1.mp4
import keras
import numpy as np
import cv2
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--video", required = True,
	help = "Path to the image to be scanned")
args = vars(ap.parse_args())


def load_images(image_paths, image_size):
    loaded_images = []
    loaded_image_paths = []
    cap =cv2.VideoCapture(image_paths)
    i = 0
    while True:
        i += 1
        ret,frame = cap.read()
        if ret:
            if i % 28 == 0:  #sau mỗi 28 frame hình thì sẽ lấy 1 hình đưa vào array
                image = cv2.resize(frame,(256, 256)) # resize image
                image = image/255.0  # chuẩn hóa dữ liệu về dạng 0 va 1
                loaded_images.append(image)
                loaded_image_paths.append(image_paths) 
        else:
            break 
    return np.asarray(loaded_images), loaded_image_paths

class Classifier():
    nsfw_model = None
    def __init__(self, model_path):
        Classifier.nsfw_model = keras.models.load_model(model_path)

    def classify(self, image_paths = "", batch_size = 32, image_size = (256, 256), categories = ['unsafe', 'safe']):
        loaded_images, loaded_image_paths = load_images(image_paths, image_size)       
        if not loaded_image_paths:
            return {}
        model_preds = Classifier.nsfw_model.predict(loaded_images, batch_size = batch_size) #predict 1 array image 
        images_preds = np.average(model_preds, axis = 0)  #lấy trung bình theo cột
        return images_preds


if __name__ == '__main__':
    weights_path = "classifier_model"
    m = Classifier(weights_path)
    result = m.classify(args["video"])
    # result = m.classify("C:/Users/anlan/OneDrive/Desktop/1.mp4")
    if result[0] > result[1]:
        print("toxic")
    else: print("no toxic")

# {'safe': 0.01849486, 'unsafe': 0.9815051}}

'''
model_preds [[0.00747683 0.99252313]
 [0.00745127 0.9925487 ]
 [0.00669979 0.9933002 ]
 [0.00798242 0.9920176 ]
 [0.00657054 0.9934295 ]
 [0.00708546 0.99291456]
 [0.0066964  0.9933036 ]
 [0.00737985 0.99262017]
 [0.00903959 0.9909604 ]
 [0.0084687  0.9915314 ]
 [0.00824533 0.99175465]
 [0.00807763 0.9919224 ]
 [0.00616169 0.99383837]
 [0.00741947 0.99258053]
 [0.00708305 0.99291694]
 [0.00617239 0.99382764]
]
'''