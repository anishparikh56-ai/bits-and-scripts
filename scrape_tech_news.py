import requests
from bs4 import BeautifulSoup
import time

# List of tech news websites with their URLs and CSS selectors for article extraction
sites = [
    {"name": "TechCrunch", "url": "https://techcrunch.com/", "selector": "h2.post-block__title a"},
    {"name": "CNET", "url": "https://www.cnet.com/", "selector": "h3 a.js-trackedLink"},
    {"name": "Wired", "url": "https://www.wired.com/", "selector": "h3 a.summary-item__hed-link"},
    {"name": "The Verge", "url": "https://www.theverge.com/", "selector": "h2 a"},
    {"name": "ZDNet", "url": "https://www.zdnet.com/", "selector": "h3 a"},
    {"name": "Gizmodo", "url": "https://gizmodo.com/", "selector": "h1 a"},
    {"name": "Engadget", "url": "https://www.engadget.com/", "selector": "h2 a"},
    {"name": "Ars Technica", "url": "https://arstechnica.com/", "selector": "h2 a"},
    {"name": "TechRadar", "url": "https://www.techradar.com/", "selector": "h3 a"},
    {"name": "MIT Technology Review", "url": "https://www.technologyreview.com/", "selector": "h3 a"}
]

# Headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def scrape_articles(site):
    try:
        # Fetch the webpage
        response = requests.get(site["url"], headers=headers, timeout=10)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, "html.parser")

        # Find article elements using the site's selector
        articles = soup.select(site["selector"])[:5]  # Limit to top 5
        if not articles:
            print(f"No articles found for {site['name']}")
            return []

        # Extract title and URL
        results = []
        for article in articles:
            title = article.get_text(strip=True)
            url = article.get("href")
            # Ensure URL is absolute
            if url and not url.startswith("http"):
                url = site["url"].rstrip("/") + "/" + url.lstrip("/")
            if title and url:
                results.append({"title": title, "url": url})
        return results

    except requests.RequestException as e:
        print(f"Error fetching {site['name']}: {e}")
        return []
    except Exception as e:
        print(f"Error parsing {site['name']}: {e}")
        return []

def main():
    for site in sites:
        print(f"\nTop 5 Articles from {site['name']}:")
        print("-" * 50)
        articles = scrape_articles(site)
        if articles:
            for i, article in enumerate(articles, 1):
                print(f"{i}. {article['title']}")
                print(f"   {article['url']}")
        else:
            print("No articles retrieved.")
        time.sleep(2)  # Delay to avoid overwhelming servers

if __name__ == "__main__":
    main()
