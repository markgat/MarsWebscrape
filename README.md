# Mars Webscraped Website

Mars website built for all-in-one constantly updated news, discovery, and images on mars, aggregated into a single website.

![mission_to_mars](Images/mission_to_mars.png)

## Getting Started

### Prerequisites
1) You will need MongoDB installed if you want to run this application locally. For help installing MongoDB, visit
````
https://docs.mongodb.com/manual/installation/
````
2) Make sure to install splinter by entering the following in the command line:
````
$ pip install splinter
````
3) If you are on Mac with Homebrew installed, install Chromedriver using:
````
$ brew cask install chromedriver
```` 
For Windows, the Chromedriver can be installed using the following link:
````
https://chromedriver.chromium.org/downloads
```` 
4) Make sure Selenium is installed. To install, just enter the following command:
````
$ pip install selenium
````
Make sure that Chromedriver version is compatible with the Selenium installed in computer.

## Installing
1) Git clone the repository to your local machine:
````
$ git clone https://github.com/markgat/MarsWebscrape.gits
````
2) Look into the "scrape_mars.py" file, and make sure the executable path is set
to where the Chromedriver is installed. By default, the path is set to where it is installed for Mac.
## Running

1) To begin, run the MongoDB daemon by entering the command:
````
$ mongod
````
2) Next, run the python program "app.py".
3) A URL will be displayed from the returned results,
````
 Running on http://127.0.0.1:5000/
````
Open link to startup web application locally on web browser.  
4) Lastly, press the "Scrape New Data" button to begin the scraping process,
after which your Mars summary page will be displayed.
![web_results](Images/MarsWeb.png)
5) To close program, close the web page, and shut off the MongoDB deamon and the terminal 
containing the URL by pressing Ctr + C within each window.

## Coming Soon
(30/01/2020) - Working on deploying on Heroku with updated ChromeDriver to make application web-deployed and more accessible.\
~~(30/01/2020) - Improve beautiful soup scraping queries(?)~~
## Updates
(05/02/2020) - Improved Twitter scrape by extending sleeping time for AJAX content to load. 
Additionally, renewed scrape search for updated Twitter HTML layout and created while loop to make sure 
tweet is weather related.