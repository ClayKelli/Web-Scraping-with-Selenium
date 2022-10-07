# Web-Scraping-with-Selenium
Instructions on how to use the selenium library and move that data into a pandas dataframe. Includes edge cases of trickier websites.

To start off I will be showing how to scrape Amazon, but will go on to show more complicated websites with more complicated edge cases. The point of these programs is to grab the data of multiple web pages with similar layouts(such as the product pages of specific products on Amazon) and move it into a pandas dataframe. The pandas dataframe can then be exported as a CSV file or excel file. 


We start off by importing the required libraries

>import time<br />
>from selenium import webdriver<br />
>import pandas as pd<br />
>from selenium.common.exceptions import NoSuchElementException<br />
>from datetime import date<br />
After this now is time to initialize the variables for the pandas dataframe and the Selenium WebDriver. We will be scraping multiple pages with the same format: Amazon product pages. The columns in the dataframe will reflect the data we are grabbing. 

>driver = webdriver.Firefox(executable_path=r'PATH')
The path is where your geckdriver.exe file is located. 

>df = pd.DataFrame(columns=['Name', 'Price', 'Description', 'Link']

