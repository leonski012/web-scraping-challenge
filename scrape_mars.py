#Imports
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime as dt

def scrape_mars_all():
    #Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #call scrape_mars_news function
    news_title, news_paragraph = scrape_mars_news(browser)

    #build mars_data dictionary to store the information
    
    mars_data_dict = {
        "news_title": news_title,
        "news_p": news_paragraph,
        "featured_image_url": scrape_feature_image(browser),
        "fact_table": scrape_mars_facts(browser),
        "hemispheres": scrape_mars_hemispheres(browser),
        "lastUpdated": dt.datetime.now()
    }

    #Stop the web driver
    browser.quit()
    
    return mars_data_dict 

def scrape_mars_news(browser):

    url = 'https://redplanetscience.com/'
    browser.visit(url)
    time.sleep(3)

    # Parse HTML with Beautiful Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve the latest News Title and Paragraph Text 
    news_title = soup.find_all('div', class_='content_title')[0].text
    news_paragraph = soup.find_all('div', class_='article_teaser_body')[0].text

    return(news_title, news_paragraph)

def scrape_feature_image(browser):
    f_image_url = 'https://spaceimages-mars.com'
    browser.visit(f_image_url)
    time.sleep(3)

    # clicking the full image button and get the html details.
    browser.find_by_tag('button')[1].click()

    # Parse HTML with Beautiful Soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #featured image URL
    featured_img_url = soup.find('img', class_='fancybox-image').get('src')
    featured_image_url = f'{f_image_url}/{featured_img_url}'
     
    return(featured_image_url)

def scrape_mars_facts(browser):

    #url for Mars's facts
    mars_facts_url = 'https://galaxyfacts-mars.com'
    browser.visit(mars_facts_url)

    # Parse HTML with Beautiful Soup
    html = browser.html
    mars_facts_soup = BeautifulSoup(html, 'html.parser')

    factsLocation = mars_facts_soup.find('div', class_ ="diagram mt-4")
    mars_facts_table = factsLocation.find('table')

    #create an empty string
    mars_facts = ""

    #add mars_facts_table to empty string
    mars_facts += str(mars_facts_table)

    return mars_facts

def scrape_mars_hemispheres(browser):
    # --- visit the Mars Hemisphere website ---
    MarsHemImage_url = 'https://marshemispheres.com/'
    browser.visit(MarsHemImage_url)
    time.sleep(1)

    # --- create an empty list to store the python dictionary ---
    hemisphere_image_data = []

    for i in range(4):

        # initialize dictionary
        hemisphereInfo = {}
        
        # --- use splinter's browser to click on each hemisphere's link in order to retrieve image data ---
        browser.find_by_css("a.product-item img")[i].click()
            
        # --- Find the Sample image url and retrieve href ---
        sample_url = browser.links.find_by_text('Sample').first
        hemisphereInfo['image_url'] = sample_url['href']
        
        # --- retrieve the image title using the title class and save into variable ---
        hemisphereInfo['title'] = browser.find_by_css('h2.title').text
        
        # --- add the key value pairs to python dictionary and append to the list ---
        hemisphere_image_data.append(hemisphereInfo)
        
        # --- go back to the main page ---
        browser.back()

    #return mars hemisphere urls with titles    
    return hemisphere_image_data

if __name__ == "__main__":
   print(scrape_mars_all())