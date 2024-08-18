from flask import Flask, render_template
import pickle
import numpy as np

app = Flask(__name__)

top_50_books = pickle.load(open("models\popolar_books.pkl" , "rb"))

@app.route("/")
def index():
    return render_template("index.html" , 
                           book_name = list(top_50_books['Book-Title'].values),
                            Number_of_Rating = list(np.round(top_50_books['Number-of-Rating'].values)),
                            Avg_Rating = list(top_50_books['Avg-Rating'].values),
                            image_url = list(top_50_books['Image-URL-L'].values),
                            Book_Author = list(top_50_books['Book-Author'].values),
                            Publisher = list(top_50_books['Publisher'].values))


@app.route("/recommend")
def recommend():
    return render_template("recommned.html")

if __name__ == '__main__':
    app.run(debug = True)