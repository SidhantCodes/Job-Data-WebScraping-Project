# Job Search Script Readme

This Python script is designed to help you find job listings based on specific skills using web scraping techniques. It targets the TimesJobs website to search for jobs related to the skills you input. Here's how you can use it:

## Prerequisites

Before using the script, ensure you have the following installed:
- Python (version 3.x)
- Required Python packages: `requests` and `BeautifulSoup` (you can install them using `pip install requests beautifulsoup4`)

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where you saved the script.

3. Run the script using the following command:
   ```python job_search.py```

4. You will be prompted to enter the skills you want to search for. Input your skills and press Enter.

5. The script will connect to the TimesJobs website, scrape job listings that match your specified skills, and save the details of matching jobs in individual text files within a "Jobs" directory.

6. The script will run in an infinite loop, searching for jobs every 10 minutes (you can adjust the time interval as needed). It will continue to append new job listings to the "Jobs" directory.

7. To stop the script, press `Ctrl+C` in the terminal.

## Script Explanation

- The script uses the `requests` library to make HTTP requests to the TimesJobs website and retrieve the HTML content of the job search page.

- It then uses `BeautifulSoup` to parse the HTML and extract relevant job listings.

- The script filters job listings based on the skills you provided and checks if the job was posted "few" days ago (you can modify this condition as needed).

- For each matching job, it creates a text file with details including the company name, required skills, and a link to the job listing.

- The script runs continuously, periodically updating the job listings.

## Customization

You can customize the script by modifying the following:

- The URL of the TimesJobs search page to target a specific location or job type.

- The time interval for job searches (currently set to 10 minutes).

- The condition for filtering job listings based on the published date.

## Disclaimer

Please use this script responsibly and be mindful of the terms of use and policies of the websites you scrape. Web scraping may be subject to legal restrictions, and it's important to respect the website's terms of service.
