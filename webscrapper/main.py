# https://www.indeed.com/q-python-jobs.html?vjk=d1218a12442b5c05
# https://www.indeed.com/jobs?as_and=python&limit=50&vjk=d1218a12442b5c05
from indeed import extract_indeed_pages
from indeed import extract_indeed_jobs, extract_indeed_jobs

last_indeed_page = extract_indeed_pages()
extract_indeed_jobs(last_indeed_page)
