from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas

chrome_driver_path = Service(r"C:\Development\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_driver_path)

driver.maximize_window()

driver.get("https://www.python.org/")

event_times = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for n in range(len(event_times)):
	events[n] = {
		"time": event_times[n].text,
		"name": event_names[n].text
	}

