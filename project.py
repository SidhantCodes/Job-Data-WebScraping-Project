from bs4 import BeautifulSoup
import requests
import time

html_txt = requests.get(
    "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation="
).text
# print(html_txt)

soup = BeautifulSoup(html_txt, "lxml")

jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
