from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui

import time


SHOWS = {"inorbit" : 'https://in.bookmyshow.com/booktickets/CXCB/71095',
		 "sujana"  : 'https://in.bookmyshow.com/booktickets/PVSF/62187'
}

class BookMyShow:
	def __init__(self, link):
		self.baseurl = link
		self.xpaths = ["//*[@id=\"lnkMainBuyTickets\"]",
					   "//*[@id=\"pop_1\"]",
			           "//*[@id=\"proceed-Qty\"]",
			           "//*[@id=\"A_11_02\"]/a",
			           "//*[@id=\"btmcntbook\"]",
			           "//*[@id=\"shmticket\"]/label",
			           "//*[@id=\"prePay\"]"
					]

		# self.binary = FirefoxBinary('/usr/bin/firefox')
		options = Options()
		options.add_argument("--headless")
		self.driver = webdriver.Firefox(firefox_options=options, executable_path='./geckodriver')
		self.driver.get(self.baseurl)
		self.flag = 0
		self.crash = 0
		self.first_result = ""
		self.first_link = ""

	def clickButton(self, xpath):
		try:
			button = self.driver.find_elements_by_xpath(xpath)[0]
			button.click()
		except:
			print("Error" + xpath)
			return 0
		else:
			return 1

def getseatlist(label, rowstart, rowend, col1, col2, col3, col4, fill1, fill2):
	seat_list = []
	for i in range(rowstart, rowend):
		for j in range(col1, col2):
			seat = label + '_' + str(i).zfill(fill1) + '_' + str(j).zfill(fill2)
			seat_list.append(seat)
		for j in range(col3, col4):
			seat = label + '_' + str(i).zfill(fill1) + '_' + str(j).zfill(fill2)
			seat_list.append(seat)
	return seat_list

def bookticket(theater, seat, count):

	status = 0

	trial = BookMyShow(theater)
	trial.xpaths[1] = count
	trial.xpaths[3] = "//*[@id=\"" + seat + "\"]/a"
	for ids in trial.xpaths:
		status = trial.clickButton(ids)
		time.sleep(5)
		if not status:
			break


if __name__ == "__main__":

	# sujana_seats = getseatlist("B", 4, 10, 1, 5, 7, 18, 1, 2)

	# seat_list = ["B_9_01","B_9_07","B_9_13"]

	for i in range(5,10):

		bookticket(SHOWS["sujana"], "B_" + str(i).zfill(1) + "_01", "//*[@id=\"pop_4\"]")
		bookticket(SHOWS["sujana"], "B_" + str(i).zfill(1) + "_07", "//*[@id=\"pop_6\"]")
		bookticket(SHOWS["sujana"], "B_" + str(i).zfill(1) + "_13", "//*[@id=\"pop_5\"]")


