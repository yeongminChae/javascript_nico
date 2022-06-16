# https://www.indeed.com/q-python-jobs.html?vjk=d1218a12442b5c05
# https://www.indeed.com/jobs?as_and=python&limit=50&vjk=d1218a12442b5c05

import requests
from bs4 import BeautifulSoup  # beautifulsoup will get html elements

indeed_resul = requests.get(
    "https://www.indeed.com/jobs?as_and=python&limit=50&vjk=d1218a12442b5c05")

indeed_soup = BeautifulSoup(indeed_resul.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

links = pagination.find_all("a")  # list
pages = []
for link in links:
    pages.append(link.find("span").string)
pages = pages[:-1]  # get spans except last one
