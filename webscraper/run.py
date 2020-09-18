import requests
from requests import get
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

def get_open_html(URL):
    r = requests.get(URL)
    print(r.status_code)
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.get_text())
    return soup

def get_job(URL):
    soup = get_open_html(URL)
    jobs = soup.find_all('div', class_="jobsearch-SerpJobCard unifiedRow row result clickcard vjs-highlight")
    for job in jobs:
        title = job.find('a', class_="jobtitle turnstileLink visited")
        print(title.get_text())
        salary = job.find('span', class_="salaryText")
        print(salary.get_text())
        location = job.find('span', class_="location")
        print(location.get_text())
        link = job.find('a', class_="jobtitle")
        link = link.get('ref')
        print(link.get_text())

get_job('https://www.indeed.com/jobs?q=Entry+Level+Python&l=New+Jersey')

# div class"jobsearch-SerpJobCard unifiedRow row result clickcard vjs-highlight" #container for each job
# a class="jobtitle turnstileLink visited" #jobtitle
# span class="salaryText" #salary
# span class ="location accessible-contrast-color-location" #location
