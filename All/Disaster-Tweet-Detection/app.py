from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import redirect
from flask import url_for
from nltk.stem import WordNetLemmatizer
import re
import nltk
from nltk.corpus import stopwords
import numpy as np
import string
#from sklearn.externals import joblib
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from unidecode import unidecode
import contractions 

nltk.download('stopwords')
nltk.download('wordnet')
#nltk.download('WordNetLemmatizer')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html" )

@app.route("/api", methods=["GET","POST"])
def api():
    if request.method == "POST":
        cv = joblib.load('count.pkl')
        model = joblib.load('tweet.pkl')

        tweet = request.form["tweet"]
        text = tweet

        text = text.lower()
        text = text.split()
        p=[]
        for word in text:
            p.append(contractions.fix(word))
        t=[' '.join(p)]
        text=t[0]

        text = re.sub("[^a-zA-Z]", ' ', text)
        text=re.sub("https\S+"," ",text)
        text=re.sub("http\S+"," ",text)
        text=re.sub("\W"," ",text)
        text=re.sub("\d"," ",text)
        text=re.sub("\_","",text)
        text = unidecode(text)
     
        text = text.split()

        

        nonpunc=[]
        for c in text:
            if c not in string.punctuation:
                nonpunc.append(c)
        text = nonpunc


        """
        for word in text:
            if  word in set(stopwords.words('english')):
                text.append(PorterStemmer.stem(word))"""
                
        lemmatizer=WordNetLemmatizer()
        L=[lemmatizer.lemmatize(word) for word in text]





        text = [' '.join(text)]
        
        X=cv.transform(text)

        prediction = model.predict(X)

        if prediction == 1:
            msg = "Your tweet is Not Fake (Real tweet)!!"
            return render_template("index.html", msg=msg, tweet=tweet)
        else:
            error = "Your tweet is Fake!!"
            return render_template("index.html", error=error, tweet=tweet)
    else:
        return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)

#web: gunicorn app:app