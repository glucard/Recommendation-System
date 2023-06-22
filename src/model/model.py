import pandas as pd

df = pd.read_csv('BX-Books.csv',on_bad_lines='skip',encoding='latin-1',sep=';')
df.head()
df = df.drop_duplicates(subset='Book-Title')

sample_size = 15000
df = df.sample(n=sample_size, replace=False, random_state=490)

df = df.reset_index()
df = df.drop('index',axis=1)

def clean_text(author):
    result = str(author).lower()
    return(result.replace(' ',''))

df['Book-Author'] = df['Book-Author'].apply(clean_text)

df['Book-Title'] = df['Book-Title'].str.lower()
df['Publisher'] = df['Publisher'].str.lower()

# combine all strings:
df2 = df.drop(['ISBN','Image-URL-S','Image-URL-M','Image-URL-L','Year-Of-Publication'],axis=1)

df2['data'] = df2[df2.columns[1:]].apply(
    lambda x: ' '.join(x.dropna().astype(str)),
    axis=1
)

print(df2['data'].head())

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
vectorized = vectorizer.fit_transform(df2['data'])

from sklearn.metrics.pairwise import cosine_similarity

similarities = cosine_similarity(vectorized)

df = pd.DataFrame(similarities, columns=df['Book-Title'], index=df['Book-Title']).reset_index()

from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin

APP = Flask(__name__)
CORS(APP, support_credentials=True)
API = Api(APP)

class Predict(Resource):

    @staticmethod
    @cross_origin(supports_credentials=True)
    def post():
        global df
        global pd
        
        parser = reqparse.RequestParser()
        parser.add_argument('input_book')

        args = parser.parse_args()  # creates dict

        input_book = args['input_book'].lower()

        try:
            recommendations = pd.DataFrame(df.nlargest(11,input_book)['Book-Title'])
            recommendations = recommendations[recommendations['Book-Title']!=input_book]

            out = {'Prediction': recommendations['Book-Title'].tolist()}
        except:
            return {'error': "Invalid book name"}, 404
        
        return out, 200
    
API.add_resource(Predict, '/predict')

if __name__ == '__main__':
    APP.run(host="0.0.0.0", debug=True, port='80')
    print("Running...")