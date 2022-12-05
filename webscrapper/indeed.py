import requests
from bs4 import BeautifulSoup


def search_job(html):
    title = html.find('a', {'class': 'jobtitle'}).text
    company = html.find('span', {'class': 'companyName'}).string.strip()
    link = 'https://www.indeed.com' + \
        html.find('a', {'class': 'jobtitle'}).get('href')
    return {'title': title, 'company': company, 'link': link}


def indeed_jobs():
    url = f"https://www.indeed.com/jobs?as_and=python&limit=50&vjk=d1218a12442b5c05"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all('div', {'class': 'jobsearch-SerpJobCard'})
    for i in results:
        print(i)
