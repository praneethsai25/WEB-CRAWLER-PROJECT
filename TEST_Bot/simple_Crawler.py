import requests     # Import the requests module
from bs4 import BeautifulSoup # Import the BeautifulSoup class from the bs4 module
from urllib.parse import urljoin # Import the urljoin function from the urllib.parse module
import time



# this crawler is for extracting the title of the page and the links on the page(basic crawler)
class SimpleWebCrawler:
    def __init__(self, start_url, max_pages):
        self.start_url = start_url
        self.max_pages = max_pages
        self.visited_urls = set()



# Start the crawling process
    def crawl(self):
        self.crawl_page(self.start_url)
    
    
    
   # Crawl a page and extract links 
    def crawl_page(self, url):
        if url in self.visited_urls or len(self.visited_urls) >= self.max_pages:
            return
        
        print(f"Crawling: {url}")
        self.visited_urls.add(url)


# Send an HTTP request to the page
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
        except requests.RequestException as e:
            print(f"Failed to retrieve {url}: {e}")
            return




# Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        self.extract_title(soup)

        # Extract links to crawl
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                
                full_url = urljoin(url, href)
                if full_url.startswith(self.start_url):  # Stay within the domain
                    self.crawl_page(full_url)

        time.sleep(1)
 # Extract the title of the page
    def extract_title(self, soup):
        title = soup.title.string if soup.title else 'No title'
        print(f"Title: {title}")






if __name__ == '__main__':
    start_url = 'https://github.com/orgs/langgenius/repositories' 
    max_pages = 5
   
    crawler = SimpleWebCrawler(start_url, max_pages)
    crawler.crawl()