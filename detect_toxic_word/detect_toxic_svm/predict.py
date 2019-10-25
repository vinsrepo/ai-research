import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.calibration import CalibratedClassifierCV
from sklearn.svm import LinearSVC
from sklearn.externals import joblib

#read data
data = pd.read_csv('clean_data.csv')
texts = data['text'].astype(str)# convert to strings

vectorizer = CountVectorizer(stop_words='english', min_df=0.0001)  #TẠO LIST TỪ ĐIỂN
X = vectorizer.fit_transform(texts)

loaded_model = joblib.load('model.pkl')
# test = vectorizer.transform([" fuck you"])
test = vectorizer.transform(["Then go to the village pump and suggest they change the language in how a RFC should be set up"])
result = loaded_model.predict(test)
if result[0] == 0:
    print("no toxic")
elif result[0] == 1:
    print("toxic")
    
