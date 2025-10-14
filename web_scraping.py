import requests
import os
import pandas as pd
from bs4 import BeautifulSoup
def fetch_and_save_to_file(url, path):
    try:
        response = requests.get(url, timeout=10)  # Adding timeout for better reliability
        response.raise_for_status()  # Raise exception for HTTP errors (4xx, 5xx)

        os.makedirs(os.path.dirname(path), exist_ok=True)  # Ensure directory exists

        with open(path, "w", encoding="utf-8") as file:
            file.write(response.text)

        print(f"Saved content to {path}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")

# Example usage
url = "https://indianexpress.com/about/human-metapneumovirus/"
fetch_and_save_to_file(url, "data/times.html")

with open("data/times.html", "r", encoding="utf-8") as f:  # Added encoding for safety
    html_doc = f.read()

soup = BeautifulSoup(html_doc, "html.parser")  # Fixed parser name
# Select all divs with class "img-context"
divs = soup.select("div.img-context")

# Extract titles from <a> inside <h3> in each div
titles = [div.find("a").get("title") for div in divs if div.find("a")]

# Print the extracted titles
for title in titles:
    print(title)

news_list = []

for div in soup.select("div.img-context"):
    title = div.find("a").get("title")
    link = div.find("a").get("href")
    date = div.find("p").text.strip() if div.find("p") else "No Date"
    news_list.append([title, link, date])
    
df = pd.DataFrame(news_list, columns=["Title", "Link", "Date"])
df.to_csv("hmpv_news.csv", index=False)
print("News saved to hmpv_news.csv")


