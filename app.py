from flask import Flask, render_template, request , jsonify
import pickle
import numpy as np

app = Flask(__name__)

top_50_books = pickle.load(open("models\popolar_books.pkl" , "rb"))

list_of_book = pickle.load(open("models\list_of_book.pkl" , "rb"))
pivot_table = pickle.load(open("models\pivot_table.pkl" , "rb"))
similarity_score = pickle.load(open("models\similarity_score.pkl" , "rb"))
books = pickle.load(open("models\Books.pkl" , "rb"))

sorted_books = sorted(list_of_book)


@app.route("/")
def index():
    return render_template("index.html" , 
                           book_name = list(top_50_books['Book-Title'].values),
                            Number_of_Rating=list(np.round(top_50_books['Number-of-Rating'].values, 0).astype(int)),
                            Avg_Rating = list(top_50_books['Avg-Rating'].values),
                            image_url = list(top_50_books['Image-URL-L'].values),
                            Book_Author = list(top_50_books['Book-Author'].values),
                            Publisher = list(top_50_books['Publisher'].values))


@app.route("/recommend")
def recommend_ui():
    return render_template("recommned.html" )

@app.route("/recommend_books" , methods = ["post"])
def recommend_books():
    user_input = request.form.get("user_input")
    index = np.where(pivot_table.index == user_input)[0][0]
    similar_books = sorted(list(enumerate(similarity_score[index])) , key = lambda x: x[1] , reverse= True)[1:9]

    data = []

    for i in similar_books:
        items = []
        temp_df = books[books["Book-Title"] == pivot_table.index[i[0]]]
        items.extend(list(temp_df.drop_duplicates("Book-Title")["Book-Title"].values))
        items.extend(list(temp_df.drop_duplicates("Book-Title")["Book-Author"].values))
        items.extend(list(temp_df.drop_duplicates("Book-Title")["Image-URL-L"].values))
        items.extend(list(temp_df.drop_duplicates("Book-Title")["Publisher"].values))

        data.append(items)
    
    print(data)
        
    return render_template("recommned.html" , data = data)

@app.route("/suggest_books", methods=["GET"])
def suggest_books():
    query = request.args.get("query", "").lower()
    suggestions = [book for book in sorted_books if query in book.lower()]
    return jsonify(suggestions)


if __name__ == '__main__':
    app.run(debug = True)