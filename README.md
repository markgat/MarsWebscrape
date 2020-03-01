# Mars Webscraped Website

Mars website built for all-in-one constantly updated news, discovery, and images on mars, aggregated into a single website.

![mission_to_mars](Images/mission_to_mars.png)

## Getting Started

### Prerequisites
You will need MongoDB installed if you want to run this application locally. For help installing MongoDB, visit
````
https://docs.mongodb.com/manual/installation/
````
Make sure to install splinter by entering the following in the command line:
````
python -m pip install splinter
````
Or
````
pip install splinter
````
<html>
<hr>
<html>
As well as splinter using
````
pip install splinter
````
as well as
````
brew install chromedriver
```` 
if you are on Mac with Homebrew installed.
And update the two to the latest if needed.



## Coming Soon
(30/01/2020) - Working on deploying on Heroku with updated ChromeDriver to make application web-deployed and more accessible.\
~~(30/01/2020) - Improve beautiful soup scraping queries(?)~~
## Updates
(05/02/2020) - Improved Twitter scrape by extending sleeping time for AJAX content to load. 
Additionally, renewed scrape search for updated Twitter HTML layout and created while loop to make sure 
tweet is weather related.