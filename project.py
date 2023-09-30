from bs4 import BeautifulSoup
import requests
import time

mySkills = input("Enter your skills> ")
def findJobs():
    html_txt = requests.get(
    "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation="
    ).text
    
    soup = BeautifulSoup(html_txt, "lxml")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
    print(f"Filtering out jobs that include the skill: {mySkills}\n")

    for index, job in enumerate(jobs):
        publishedDate = job.find("span", class_="sim-posted").span.text
        
        if "few" in publishedDate:
            skills = job.find("span", class_="srp-skills").text.replace(" ","")
            if(mySkills in skills):
                with open(f'Jobs/Job{index}.txt', 'w') as f:
                    companyName = job.find("h3", class_="joblist-comp-name").text.replace(" ","")
                    moreInfo = job.header.h2.a["href"]
                    f.write(f"Company Name: {companyName.strip()}\nSkills Required: {skills.strip()}\nMore Info: {moreInfo.strip()}\n")
                    print(f"File saved: Job{index}.txt")
if __name__ == "__main__":
    while True:
        findJobs()
        time_mins = 10
        print(f"Waiting {time_mins} minutes...")
        time.sleep(time_mins * 60)