import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.calibration import CalibratedClassifierCV
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
'''
Read in data
'''
data = pd.read_csv('clean_data.csv')
texts = data['text'].astype(str)# convert to strings
# print("texts",[texts[0]])
y = data['is_offensive']

# # Vectorize the text
vectorizer = CountVectorizer(stop_words='english', min_df=0.0001)  #TẠO LIST TỪ ĐIỂN
X = vectorizer.fit_transform(texts)
# print(vectorizer.get_feature_names())
'''
Train the model
'''
model = LinearSVC(class_weight="balanced", dual=False, tol=1e-2, max_iter=1e5) #khởi tạo model
cclf = CalibratedClassifierCV(base_estimator=model)
cclf.fit(X, y)
'''
Save the model
'''
joblib.dump(vectorizer, 'vectorizer.pkl')
joblib.dump(cclf, 'model.pkl') 
