# Importing necessary modules and libraries.
from bs4 import BeautifulSoup
import requests

# To get the keyword.
key="Data"#input("Enter Keyword: ")

# To search the keyword given.
response = requests.get(f"https://www.linkedin.com/jobs/search?keywords={key}&location=Bengaluru%2C%20Karnataka%2C%20India&geoId=105214831&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0").text

# To parse the html file using lxml.
soup = BeautifulSoup(response, 'lxml')

# To create a list of job details.
jobs = soup.find_all("div", class_="base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card")

# To get the details of each job in the list and to store the required text only without unnecessary text and whitespace.
for job in jobs:
    company_name = job.find("h4", class_="base-search-card__subtitle").text.replace('''  
    ''', "")
    position = job.find("h3", class_="base-search-card__title").text.replace('''  
    ''', "")
    location = job.find("span", class_="job-search-card__location").text.replace('''  
    ''', "")
    time = job.find("div", class_="base-search-card__metadata").time.text.replace('''
    ''', "")
    detail = job.find("div", class_="result-benefits")
# Since some jobs don't have any details given, the if statement is needed to prevent any error(which will terminate the program early).
    if detail is None:
        detail="\n\t\tNo Details Given.\n"
    else:
        detail=detail.span.text.replace('''  
        ''', "")

# To print the details.
    print(f'''
    Company Name:{company_name}
    Position:{position}
    Location:{location}
    Details:{detail}
    Time Posted:{time}
    ''')
    print(" ")
    print("\n\n")
