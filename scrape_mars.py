#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import time


# In[2]:

def scrape():

#create browser instance
    executable_path = {"executable_path":"/usr/local/bin/chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)


    # In[3]:


    # extract nasa mars news
    url = "https://mars.nasa.gov/news/"
    # new in ul element/ class "item_list "
    browser.visit(url)
    time.sleep(1)
    soup = bs(browser.html, "lxml")
    articles = soup.find("ul", class_="item_list")
    recent_news = articles.find("div", class_="content_title")
    teaser = articles.find("div", class_="article_teaser_body")
    news_title = recent_news.text
    news_p = teaser.text


    # In[4]:


    # scrape jpl featured image
    # update url
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    time.sleep(1)
    soup = bs(browser.html, "lxml")
    # direct towards full image reel
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(3)
    browser.click_link_by_partial_href('/spaceimages/details.php')
    time.sleep(1)
    # instead of using beautiful soup, fully direct to photojournal and get url, i.e. raw image, instead of large image
    # on second page
    browser.click_link_by_partial_text('.jpg')
    featured_image_url = browser.url


    # In[5]:


    # next up, mars weather on twitter
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    time.sleep(1)
    soup = bs(browser.html, "lxml")
    #find latest tweet
    newest_tweet = soup.find("div", class_="js-tweet-text-container")
    # isolate text and format
    newest_tweet = newest_tweet.find("p").text
    new_isol = newest_tweet[newest_tweet.find("sol"):newest_tweet.rfind("hPa") + 3]
    mars_weather = new_isol.replace("\n", " ").capitalize()


    # In[6]:


    # time to get some fun facts using pandas
    url = "https://space-facts.com/mars/"
    table = pd.read_html(url)[1]
    table = table.rename(columns= {0:"",1:"value" })
    table = table.to_html(index= False)


    # In[13]:


    # scrap hemisphere images
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    time.sleep(1)
    soup = bs(browser.html, "lxml")
    # use splinter to navigate every image
    hemispheres = soup.find("div", class_="collapsible results")
    hemispheres = hemispheres.find_all("div", class_="description")
    # set-up empty list for urls of images, and names of hemispheres
    hemisphere_image_urls =[]
    # find hrefs via soup
    # need to click href, get url, then go back
    for section in hemispheres:
        temp = {}
        title = section.find("a").text
        browser.click_link_by_partial_text(title)
        time.sleep(1)
        # fill
        soup = bs(browser.html, "lxml")
        downloads = soup.find("div", class_="downloads")
        link = downloads.find("a")["href"]
        temp["title"] = title[:-9]
        temp["img_url"] = link
        hemisphere_image_urls.append(temp)
        # fill
        browser.back()
        time.sleep(1)


    # In[14]:


    data = {}
    data['news_title'] = news_title
    data['news_p'] = news_p 
    data['featured_img'] = featured_image_url
    data['weather'] = mars_weather
    data['facts'] = table
    data['hemispheres'] = hemisphere_image_urls
    browser.quit()
    return data

# In[ ]:




