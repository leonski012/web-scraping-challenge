# Unit 12 Homework: Mission to Mars

In this assignment, a web application was built that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

## Instructions 

There are two parts to this assignment: 

1. Scraping 

2. MongoDB and Flask Application

## Part  1: Scraping

Completed initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Created a Jupyter Notebook file called `mission_to_mars.ipynb`. Use this file to complete all your scraping and analysis tasks. The following information outlines what you need to scrape.

### NASA Mars News

* Scraped the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

```python
# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
```

### JPL Mars Space Images—Featured Image

* Visited the URL for the Featured Space Image site [here](https://spaceimages-mars.com).

* Used Splinter to navigate the site and find the image URL for the current Featured Mars Image, then assign the URL string to a variable called `featured_image_url`.

* Made sure to find the image URL to the full-sized `.jpg` image.

* Made sure to save a complete URL string for this image.

```python
# Example:
featured_image_url = 'https://spaceimages-mars.com/image/featured/mars2.jpg'
```

### Mars Facts

* Visited the [Mars Facts webpage](https://galaxyfacts-mars.com) and use Pandas to scrape the table containing facts about the planet including diameter, mass, etc.

* Used Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* Visited the [astrogeology site](https://marshemispheres.com/) to obtain high-resolution images for each hemisphere of Mars.

* Clicked each of the links to the hemispheres in order to find the image URL to the full-resolution image.

* Saved the image URL string for the full resolution hemisphere image and the hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.

* Appended the dictionary with the image URL string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```

- - -

## Part 2: MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all the information that was scraped from the URLs above.

* Started by converting your Jupyter notebook into a Python script called `scrape_mars.py` by using a function called `scrape`. This function should  execute all your scraping code from above and return one Python dictionary containing all the scraped data.

* Next, created a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

  * Stored the return value in Mongo as a Python dictionary.

* Created a root route `/` that will query your Mongo database and pass the Mars data into an HTML template for displaying the data.

* Created a template HTML file called `index.html` that will take the Mars data dictionary and display all the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

![final_app_part1.png](Images/final_app.png)

- - -

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
