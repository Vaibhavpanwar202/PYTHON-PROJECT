import requests
from bs4 import BeautifulSoup
import schedule
import time

def scrape():
    print("⏰ Scraping Hacker News headlines...\n")
    url = "https://news.ycombinator.com/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        titles = soup.select(".titleline > a")
        for i, title in enumerate(titles[:5], start=1):  # Get top 5 headlines
            print(f"{i}. {title.text}")
    else:
        print("❌ Failed to retrieve data.")

# Schedule the job every 1 minute
schedule.every(1).minutes.do(scrape)

print("✅ Web Scraper Started (Ctrl+C to stop)")
scrape()  # Run immediately once

while True:
    schedule.run_pending()
    time.sleep(1)
