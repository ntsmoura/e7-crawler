from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import re
import os
from dotenv import load_dotenv

load_dotenv()

HCTI_API_ENDPOINT = os.getenv("HTCI_ENDPOINT")
HCTI_API_USER_ID = os.getenv("HTCI_USER")
HCTI_API_KEY = os.getenv("HTCI_API_KEY")
WEBHOOK_TOKEN = os.getenv("WEBHOOK_TOKEN")
WEBHOOK_ID =  os.getenv("WEBHOOK_ID")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

def create_driver():
   options = webdriver.ChromeOptions()
   options.add_argument("--headless")
   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
   return driver

URL = "https://page.onstove.com/epicseven/pt/list/e7pt004?listType=2&page=1&direction=Latest"   

driver = create_driver()
driver.get(URL)
try:
   WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "subject-txt"))
    )
except:
   print("Error..")
finally:
   page = driver.page_source
   soup = BeautifulSoup(page,"html.parser")
   events = soup.find("div",{"log-area":'articleList'})
   regex = re.compile('subject-icon*')
   for event in events.find_all("li"):
      content = event.find("div",{"class":"subject-txt"})
      if(content and content.find("span").text=="[Ativo]" and ("reforços" or "check-in") in content.text.lower()): 
         link = event.find("a",{"class":regex})
         timestamp = event.find("span",{"class":"write-time-tooltip"}).text.split(" ")
         timestamp_obj= datetime.strptime(timestamp[0] + " " + timestamp[1], "%Y.%m.%d %H:%M")
         if(link and link["href"]): 
            #print("Evento: {}, Link: https:{}, Timestamp: {}".format(content.text.strip(),link["href"],timestamp_obj))
            driver.get("https:"+link["href"])
            try:
               WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
            finally:
               content_page = driver.page_source
               soup = BeautifulSoup(content_page,"html.parser")
               image = requests.post(url = HCTI_API_ENDPOINT, data = {'html':str(soup.find("table"))}, auth=(HCTI_API_USER_ID, HCTI_API_KEY))
               response = requests.post(url=WEBHOOK_URL+WEBHOOK_ID+"/"+WEBHOOK_TOKEN,json={"embeds":[{'image':{'url':image.json()['url']} ,'title':content.text.strip(),'description':str(timestamp_obj)}]})

   driver.quit()