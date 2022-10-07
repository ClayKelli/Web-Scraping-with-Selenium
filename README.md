# Web-Scraping-with-Selenium
Instructions on how to use the selenium library and move that data into a pandas dataframe. Includes edge cases of more complicated websites.

To start off I will be showing how to scrape Amazon, but will go on to show more complicated websites with more complicated edge cases. The point of these programs is to grab the data of multiple web pages with similar layouts(such as the product pages of specific products on Amazon) and move it into a pandas dataframe. The pandas dataframe can then be exported as a CSV file or excel file. 


We start off by importing the required libraries

>import time<br />
>from selenium import webdriver<br />
>import pandas as pd<br />
>from selenium.common.exceptions import NoSuchElementException<br />
>from datetime import date<br />

After this now is time to create the variables for the pandas dataframe and the Selenium WebDriver. We will be scraping multiple pages with the same format: Amazon product pages. The columns in the dataframe will reflect the data we are grabbing. 

The path is where your geckdriver.exe file is located. 

>driver = webdriver.Firefox(executable_path=r'PATH')


>df = pd.DataFrame(columns=['Name', 'Price', 'Description', 'Link', 'DateScraped']

I create a variable 'index' and set it to 0. This variable will be used as the index to the dataframe  

>index = 0

I also create a variable for the current date. This is used for identifying new items if the scrape is being run recurringly. 

>today = date.today()
>today = today.strftime('%Y-%m-%d') 


Now is time to create the class named 'amazon' with the variable 'item'. We are going to use the variable 'item' as the name of the product that we want to put in the search bar.

>def amazon(item)
>    global index
>    driver.get('amazon.com')
>    

