from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

@app.route("/")
def home():

    mars_data = mongo.db.recent.find_one()

    return render_template("index.html", mars_data=mars_data)

@app.route("/scrape")
def scrape():
    # make sure to remove any existing collection
    mongo.db.recent.drop()

    # Run the scrape function
    data = scrape_mars.scrape()

    # update the mars_db using insert
    mongo.db.recent.insert(data)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)