from bs4 import BeautifulSoup
import requests
import time

mySkills = input("Enter your skills> ")
html_txt = requests.get(
    "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation="
).text
# print(html_txt)

soup = BeautifulSoup(html_txt, "lxml")

jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")


print(f"Filtering out jobs that include the skill: {mySkills}\n")

for job in jobs:
    publishedDate = job.find("span", class_="sim-posted").span.text
    
    if "few" in publishedDate:
        skills = job.find("span", class_="srp-skills").text.replace(" ","")
        if(mySkills in skills):
            
            companyName = job.find("h3", class_="joblist-comp-name").text.replace(" ","")
            moreInfo = job.header.h2.a["href"]
            print(f"Company Name: {companyName.strip()}\nSkills Required: {skills.strip()}\nMore Info: {moreInfo.strip()}\n")
            print("\n---------------------------------")

