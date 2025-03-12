# Below is an enhanced version of the crawler that gathers titles along with all subheadings.
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time



class EnhancedWebCrawler:
    def __init__(self, start_url, max_pages):
        self.start_url = start_url
        self.max_pages = max_pages
        self.visited_urls = set()
        self.headings = []

    def crawl(self):
        self.crawl_page(self.start_url)
    
    def crawl_page(self, url):
        if url in self.visited_urls or len(self.visited_urls) >= self.max_pages:
            return
        
        print(f"Crawling: {url}")
        self.visited_urls.add(url)

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
        except requests.RequestException as e:
            print(f"Failed to retrieve {url}: {e}")
            return



# Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        self.extract_content(soup)

        # Extract links to crawl
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                full_url = urljoin(url, href)
                if full_url.startswith(self.start_url):  # Stay within the domain
                    self.crawl_page(full_url)

        
        time.sleep(1)

    def extract_content(self, soup):
       
        title = soup.title.string if soup.title else 'No title'
        print(f"Title: {title}")
        self.headings.append(('Title', title))
        
  
        for i in range(1, 4):  
            for heading in soup.find_all(f'h{i}'):
                heading_text = heading.get_text(strip=True)
                print(f"Heading h{i}: {heading_text}")
                self.headings.append((f'h{i}', heading_text))

if __name__ == '__main__':
    start_url = 'https://medium.com/@Ivan-Smith-308/how-to-write-wig-business-plan-example-guide-4d8e0070843f'
    max_pages = 10  
    crawler = EnhancedWebCrawler(start_url, max_pages)
    crawler.crawl()