import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#-Variables
countries = ['Canada', 'Germany', 'Iceland', 'Pakistan', 'Singapore', 'South Africa']

class scrape(object):
    def __init__(self, locations):
        self.driver = webdriver.Chrome()
        self.locations = locations

    def the_collector(self, country, driver):        
        #-Locate textbox, clear and enter country.
        driver.find_element_by_id("countryName").clear()     
        searchbox = driver.find_element_by_id("countryName")
        searchbox.send_keys(country)
        searchbox.send_keys(Keys.RETURN)

        #-Wait for page to load elements.(My internet is slow)  
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "paymonthly"))).click()
        time.sleep(3)

        #-Locate price element & print results
        price = driver.find_element_by_xpath("//*[@id='standardRatesTable']/tbody/tr[1]/td[2]")
        print(country + ' ' + price.text)


    def finish(self): #-Close webpage.
        self.driver.close()

    def run(self):#-Open webpage & loop through countries list.
        self.driver.get("http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk")
        for place in self.locations:
            self.the_collector(place, self.driver)
        self.finish()

#-Create class instance & run.
start = scrape(countries)
start.run()

#I found the task very enjoyable, some of the bugs were fun to tackle.

#a program was blocking selenium dependencies from running with chrome. 
#slow network causing the script to read text before it had fully loaded. Fix: Add Delays (sleep(3))

#In retrospect, I should have used Visual Studios instead of VI

