import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_trending():
    url = "https://github.com/trending"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to fetch trending repositories")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    repos = soup.find_all("article", class_="Box-row")
    data = []


    for repo in repos:
        repo_name = repo.find("h2", class_="h3").get_text(strip=True)
        repo_link = "https://github.com/" + repo_name.replace(" ", "")
        description = repo.find("p", class_="col-9").get_text(strip=True) if repo.find("p", class_="col-9") else "No description"
        stars = repo.find("a", href=lambda x: x and "/stargazers" in x).get_text(strip=True)
        stars_today = repo.find("span", class_="d-inline-block float-sm-right").get_text(strip=True).replace(" stars today", "")

        data.append({"name": repo_name, "link": repo_link, "description": description, "stars": stars, "stars_today": stars_today})

    return data
