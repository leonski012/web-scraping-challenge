from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars


# Flask Setup
app = Flask(__name__)

# mongodb connection
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/marsDB"
mongo = PyMongo(app)

# List all Flask Routes

#Route to render index.html template using data from Mongo
@app.route("/")
def index():
   # Find one record of data from the mongo database
    mars_details = mongo.db.mars_data.find_one()
    # Return template and data
    return render_template("index.html", mars=mars_details)
    
#scrape route

@app.route("/scrape")
def scrape():
    # identify the collection
    mars_data = mongo.db.mars_data
   
    # drop collection
    mars_data.drop()

    #calling the scrape function
    mars_scraped_data = scrape_mars.scrape_mars_all()
    
    #update mongo db
    mars_data.insert_one(mars_scraped_data)
    return redirect("/", code=302)

    session.close()

if __name__ == '__main__':
    app.run(debug=True)