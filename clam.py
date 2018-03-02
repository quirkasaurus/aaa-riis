#!/usr/bin/python
"""
FILE:    clam.py
AUTHOR:  Douglas Roberts -- droberts
CREATED: Thu Mar  1 16:07:17 EST 2018
PURPOSE: selenium test with aaa.com
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AAATest():

    def __init__(self):
        # initialize the virtual driver
        self.driver = webdriver.Firefox()
	# self.driver.set_preference("geo.enabled", False)
	# set the initial page
	self.url = 'https://www.aaalife.com/term-life-insurance-quote-input'
	return


    def post_aaa(self):
        """
	fill out the various input controls,
	post the form,
	read the resultant quote.
	"""
        # connect to the site
        self.driver.get(self.url)
        time.sleep(1)

        select = Select(self.driver.find_element_by_name('gender'))
	select.select_by_visible_text("Male")
	time.sleep(1)

        select = Select(self.driver.find_element_by_name('month'))
	select.select_by_visible_text("July")
	time.sleep(1)

        select = Select(self.driver.find_element_by_name('day'))
	select.select_by_visible_text("31")
	time.sleep(1)

        select = Select(self.driver.find_element_by_name('year'))
	select.select_by_visible_text("1962")
	time.sleep(1)

	id = 'isMemberYes'
	elem = self.driver.find_element_by_id(id)
	elem.click()
	time.sleep(1)

	elem = self.driver.find_element_by_id('contact_email')
	elem.send_keys("douglaskroberts@yahoo.com")
	time.sleep(1)

	select = Select(self.driver.find_element_by_name('feet'))
	select.select_by_visible_text("5")
	time.sleep(1)

	select = Select(self.driver.find_element_by_name('inches'))
	select.select_by_visible_text("10")
	time.sleep(1)

	elem = self.driver.find_element_by_id('weight')
	elem.send_keys("150")
	time.sleep(1)

	elem = self.driver.find_element_by_id('nicotineUseNo')
	elem.click()
	time.sleep(1)

        select = Select(self.driver.find_element_by_id('rateYourHealth'))
	select.select_by_visible_text("Excellent")
	time.sleep(1)

        select = Select(self.driver.find_element_by_id('coverageAmount'))
	select.select_by_visible_text("$100,000")
	time.sleep(1)

        select = Select(self.driver.find_element_by_id('termLength'))
	select.select_by_visible_text("15 Years")
	time.sleep(1)

        # enter a value into the zip code field
        elem = self.driver.find_element_by_id('zip')
        elem.send_keys('48187')
        time.sleep(1)

	elem = self.driver.find_element_by_id('seeQuote')
	elem.click()

	# wait until we are on the quote page...
        wait = WebDriverWait(self.driver, 20)
	wait.until(EC.title_contains("See Your Results"))

	# wait until the quote is rendered on the page...
        loc = '//span[@class="summaryPremium"]'
        wait.until(EC.presence_of_element_located((By.XPATH, loc)))
	elem = self.driver.find_element_by_xpath(loc)
	time.sleep(2)

	# print the results
	print "Your quote is:", elem.text

        self.driver.quit()
	return


if __name__ == "__main__":
    aaa = AAATest()
    aaa.post_aaa()


