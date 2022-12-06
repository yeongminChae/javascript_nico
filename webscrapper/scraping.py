import requests
from bs4 import BeautifulSoup


def extract_job(html):
    title = html.find("span", {"class": "title"}).text
    company_name = html.find("span", {"class": "company"}).text
    link_id = html.find("span", {"class": "title"}).parent["href"]

    return {
        'title': title,
        'company': company_name,
        'link': f"https://weworkremotely.com/{link_id}"
    }


def extract_jobs(url):
    jobs = []

    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("li", {"class": "feature"})

    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs


def get_jobs(word):
    url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
    jobs = extract_jobs(url)
    return jobs
