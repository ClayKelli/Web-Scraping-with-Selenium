# -*- coding: utf-8 -*-

#import the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common import exceptions
import pandas as pd
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import TimeoutException
#from selenium.common.exceptions import StaleElementReferenceException
#from selenium.common.exceptions import WebDriverException
#from selenium.common.exceptions import ElementNotInteractableException
#from selenium.webdriver.common.action_chains import ActionChains
#import pandas as pd
from datetime import date
import time

#The driver is the variable we will use to control the webdriver windows. The path should be where your geckodriver.exe file is(if you are using the firefox driver)
driver = webdriver.Firefox(executable_path=r'C:\Users\clayk\OneDrive\Desktop\legal\geckodriver.exe') 
#This line of code is creating the dataframe and the column names for the dataframe. This dataframe will eventually be exported as a .csv file.
df = pd.DataFrame(columns=['Title', 'Price', 'Link', 'DateScraped'])
#The index is set to 0 so we can iterate over the dataframe and add new rows
index = 0
#Setting the variable today to today's date
today = date.today()
today = today.strftime('%Y-%m-%d') 


#declaring the Amazon class with the item paramater.
def Amazon(item):
    #declaring the index variable as a global variable
    global index
    #hrefs is the list where we will store the links to the pages we want to scrape
    hrefs = []
    #driver.get instructs the web driver to go the the url we give it
    driver.get('https://www.amazon.com')
    #Enters the variable 'item' in the search box and presses the enter key
    driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').send_keys(item)
    driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').send_keys(Keys.RETURN)
    #To get the XPath of all the product links in the result page, I got two individual XPaths of elements in the group of product links I wanted.
    #/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[29]/div/div/div/div/div[2]/div[1]/h2/a
    #/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[28]/div/div/div/div/div[2]/div[1]/h2/a
    #Then I delete the brackets where the numbers don't match to create the XPath I will use to create the new Xpath
    #so where div[29] and div[28] were, now it is just div. 
    #/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div/div/div/div/div/div[2]/div[1]/h2/a
    #The nextButtonStatus variable checks the availability of the 'Next' or pagination button. When it is false, the loop stops.
    nextButtonStatus = True
    #This is the pagination loop that will gather the links for the products on each page, then click the 'Next' button.
    while nextButtonStatus == True:
        #Sleep for two seconds so the page can load.
        time.sleep(2)
        #Here is where I use the curated xpath from above to get all the products on one page into a list of individual elements.
        els = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div/div/div/div/div/div[2]/div[1]/h2/a')
        #I then loop through this list of elements and add the 'href' attribute(the links) to the href list that was created earlier
        for link in els:    
            hrefs.append(link.get_attribute("href"))
        #Here I give the driver 5 seconds to click the 'Next' pagination button. If the element is not clickable, the program times out.
        #This timeout is handled with the TimeoutException and the nextButtonStatus is turned to False, ending this part of the loop 
        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]'))).click()
        except TimeoutException:
            nextButtonStatus = False
    #Now that we have all the links of the pages we want to scrape in the 'hrefs' list, it is time to iterate and scrape the links in this list
    for x in hrefs:
        #Makes the webdriver go to every link in the hrefs list
        driver.get(x)
        #Here we are assigning the title variable to the innerHTML of the corresponding XPath. If the XPath is not on the page, that means the layout of the page is different. So I just assign 'NA' to the variable. 
        try:
            title = driver.find_element_by_xpath('//*[@id="productTitle"]').get_attribute('innerHTML')
        except NoSuchElementException:
            title = 'NA'
        #The same thing is done with the 'price' variable. 
        try:                        
            price = driver.find_element_by_xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[1]').get_attribute('innerHTML')
        except NoSuchElementException:
            price = 'NA'
        #These variables are then placed in the dataframe we created in the spot of the current index.
        df.loc[index] = [title, price, x, today]
        #The index is increased by one so that the next entry to the dataframe is in the correct place
        index += 1
        
#In this list, each item will be put into the search bar and the class above will run
productList = ['Shoes', 'Socks', 'Footwear']
#These two lines run the Amazon class we just made using the productList list as variables for the search bar.
for product in productList:
    Amazon(product)
    
df.to_csv(r"C:\Users\clayk\OneDrive\Desktop\legal\nationalHomeInspector2022-10-5.csv", index=False)
