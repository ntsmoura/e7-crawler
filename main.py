from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from datetime import datetime
import e7crawler
import os
import schedule
import time
from dotenv import load_dotenv

load_dotenv()

HCTI_API_ENDPOINT = os.getenv("HTCI_ENDPOINT")
HCTI_API_USER_ID = os.getenv("HTCI_USER")
HCTI_API_KEY = os.getenv("HTCI_API_KEY")
WEBHOOK_TOKEN = os.getenv("WEBHOOK_TOKEN")
WEBHOOK_ID =  os.getenv("WEBHOOK_ID")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

actual_timestamp = datetime.now()
#actual_timestamp = datetime.strptime("2022.06.29 05:59", "%Y.%m.%d %H:%M")

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)


def events_search():
   global actual_timestamp, driver
   timestamp = e7crawler.events_crawler(driver, actual_timestamp, HCTI_API_ENDPOINT, HCTI_API_USER_ID, HCTI_API_KEY, WEBHOOK_TOKEN, WEBHOOK_ID, WEBHOOK_URL)
   if(timestamp > actual_timestamp): actual_timestamp = timestamp

schedule.every(10).minutes.do(events_search)


while True:
   try:
      schedule.run_pending()
      time.sleep(1)
   except KeyboardInterrupt:
      break

print("Bye...")