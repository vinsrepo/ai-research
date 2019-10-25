## AI-research
## Mục lục
[I. Detect toxic image and video](#I)
- [1. Classifier_image](#classifier_image)
- [2. Classifier_video](#classifier_video)

[II. Detect toxic word](#II)
- [1. Detect_toxic_svm](#detect_toxic_svm)
- [2. Filter_toxic_from_array](#filter_toxic_from_array)
- [3. Bert_classification](#bert_classification)

<a name="I"></a>
## I. Detect toxic image and video
Project dựa theo repo https://github.com/bedapudi6788/NudeNet

Bạn cần tải pre-train model "classifier_model" ở đây https://github.com/bedapudi6788/NudeNet-models/tree/master/v1
<a name="classifier_image"></a>
### 1. Classifier_image:
### Sử dụng:
```
py classifier.py --image C:/Users/anlan/OneDrive/Desktop/detect_image_toxic/00000001.jpg
```
<a name="classifier_video"></a>
### 2. Classifier_video:
### Sử dụng:
```
py classifier_video.py --video C:/Users/anlan/OneDrive/Desktop/1.mp4
```

<a name="II"></a>
## II. Detect toxic word

<a name="detect_toxic_svm"></a>
### 1. Detect_toxic_svm:
Project sử dụng mô hình SVM tuyến tính được đào tạo trên gần 200k mẫu chuỗi văn bản bình thường và thô tục.
### a Train:
```
py train.py
```
### b Predict:
```
py predict.py
```

<a name="filter_toxic_from_array"></a>
### 2. Filter_toxic_from_array:
Lọc qua 1 từ điển các từ thô tục và so sánh với từng từ trong câu để kiểm tra xem câu có thô tục hay bình thường
### Sử dụng:
```
py filter_toxic.py
```

<a name="bert_classification"></a>
### 3. Bert_classification:

Sử dụng mô hình bert để phân loại 20 loại tin tức

Sử dụng bộ dữ liệu 20news group: http://qwone.com/~jason/20Newsgroups/20news-18828.tar.gz

Mô hình được train trên google colab bạn chuyển file bert_classification.ipynb sang google colab để sử dụng
