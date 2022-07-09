from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import re

def events_crawler(driver, actual_timestamp, htci_endpoint, htci_user, htci_key, webhook_token, webhook_id, webhook_url):
    highest_timestap = actual_timestamp
    URL = "https://page.onstove.com/epicseven/pt/list/e7pt004?listType=2&page=1&direction=Latest"   
    driver.get(URL)
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "subject-txt"))
        )
    except:
        print("Something went wrong...")
    finally:
        page = driver.page_source
        soup = BeautifulSoup(page,"html.parser")
        events = soup.find("div",{"log-area":'articleList'})
        regex = re.compile('subject-icon*')
        for event in events.find_all("li"):
            content = event.find("div",{"class":"subject-txt"})
            if(content and content.find("span").text=="[Ativo]" and ("reforços" or "check-in" or "reforço") in content.text.lower()): 
                link = event.find("a",{"class":regex})
                timestamp = event.find("span",{"class":"write-time-tooltip"}).text.split(" ")
                timestamp_obj= datetime.strptime(timestamp[0] + " " + timestamp[1], "%Y.%m.%d %H:%M")
                if(timestamp_obj >= actual_timestamp):
                    if(link and link["href"]): 
                        driver.get("https:"+link["href"])
                        try:
                            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
                        finally:
                            content_page = driver.page_source
                            soup = BeautifulSoup(content_page,"html.parser")
                            image = requests.post(url = htci_endpoint, data = {'html':str(soup.find("table"))}, auth=(htci_user, htci_key))
                            requests.post(url=webhook_url+webhook_id+"/"+webhook_token,json={"embeds":[{'image':{'url':image.json()['url']} ,'title':content.text.strip(),'description':str(timestamp_obj)}]})
                    if(timestamp_obj>=highest_timestap): highest_timestap = timestamp_obj
    return highest_timestap
