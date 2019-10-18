from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")



@app.route("/")
def home():
    # For initial run, if db DNE
    mars_data ={"news_title":"", "news_p":"", "featured_img":"", "weather":"", "facts":"", "hemispheres":\
    [{"title":"","img_url":""},{"title":"","img_url":""},{"title":"","img_url":""},{"title":"","img_url":""}] }
    # Check if db not empty
    if mongo.db.recent.find_one() != None:
        mars_data = mongo.db.recent.find_one()

    return render_template("index.html", mars_data=mars_data)

@app.route("/scrape")
def scrape():

    # Run the scrape function
    data = scrape_mars.scrape()

    # update the mars_db using upsert
    mongo.db.recent.update_one({}, {"$set": data}, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)