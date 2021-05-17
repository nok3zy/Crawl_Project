from util import getDate

from googleapiclient.discovery import build

import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



class Youtube:
    def __init__(self):
        self.api_key = "AIzaSyAyklYk5KDKCvndiOsNNoCr64NoqNcfWqM"
        self.video_ids=[]
        self.max_page = 5
    
    def wait_for(self, locator):
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(locator)
        )

    def get_id(self):
        browser = webdriver.Chrome(ChromeDriverManager().install())
        url = "https://www.youtube.com/feed/explore"
        browser.get(url)
        titles = browser.find_elements_by_id("video-title")
        for title in titles:
            title_url=str(title.get_attribute("href"))
            self.video_ids.append(title_url[32:])
        browser.quit()
        
    
    # def save_csv(self):
    #     file = open(f"{getDate()}.csv", "w",newline="",encoding="utf-8")
    #     writer = csv.writer(file)
    #     writer.writerow(("text","publishedAt"))#
    #     for comment in self.comments:
    #         writer.writerow((comment[0],comment[1]))

    def save_csv(self,code,comments):
        file = open(f"./raw_data/{getDate()}_{code}.csv", "w",newline="",encoding="utf-8")
        writer = csv.writer(file)
        writer.writerow(("text","publishedAt"))#
        for comment in comments:
            writer.writerow((comment[0],comment[1]))
    
    def get_data(self):
        self.get_id()
        for video_id in self.video_ids[1:2]:
            self.get_comment(video_id)
        return self.video_ids

    def get_thumb(self,code):
        base_url = f"https://i.ytimg.com/vi/{code}/mqdefault.jpg"
        # https://i.ytimg.com/vi/{code}/hqdefault.jpg # bigger

    def get_comment(self,video_id):
        cnt =1
        api_obj = build("youtube","v3",developerKey=self.api_key)
        response = api_obj.commentThreads().list(part='snippet,replies', videoId=video_id, maxResults=100).execute()
        comments=[]
        while response:
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']
                print(comment['textDisplay'])#
                comments.append((comment['textDisplay'], comment['publishedAt']))
                # writer.writerow((comment['textDisplay'], comment['publishedAt']))
                time.sleep(.05)
                
            if 'nextPageToken' in response and cnt <= self.max_page:
                cnt+=1
                response = api_obj.commentThreads().list(part='snippet,replies', videoId=video_id, pageToken=response['nextPageToken'], maxResults=100).execute()
            else:
                break

        self.save_csv(video_id,comments)
    

