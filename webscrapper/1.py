import requests
from bs4 import BeautifulSoup

result = requests.get(
    "https://pornammo.com/video/damsel-in-distress-facial-abuse-5543295")
soup = BeautifulSoup(result.text, "html.parser")
results = soup.find("video")["src"]
print(results)
