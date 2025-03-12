from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests

# Connect to MongoDB
client: MongoClient = MongoClient('mongodb://localhost:27017/')
db = client['NEW_DATABASE_NAME']  
collection = db['titles']    

def extract_titles_and_subheadings(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        
        # Extract the main title
        title = soup.title.string if soup.title else "No Title Found"

        # Extract subheadings (h1, h2, h3, etc.)
        subheadings = []
        for i in range(1, 4):  
            headings = soup.find_all(f'h{i}')
            subheadings.extend([heading.string for heading in headings if heading.string])

        document = {
            'url': url,
            'title': title,
            'subheadings': subheadings
        }

        collection.insert_one(document)
        print(f"Saved title and subheadings for '{url}'")
    else:
        print(f"Failed to retrieve {url}")


if __name__ == "__main__":
    url = "https://medium.com/@MaryDsa/step-by-step-guide-to-build-a-web-crawler-9cd0b69cd44c"
    extract_titles_and_subheadings(url)
    
    
    # test urls dynamic links :
    # https://www.bbc.com/news
    # https://www.bbc.com/news/world
    # https://medium.com/@Ivan-Smith-308/how-to-write-wig-business-plan-example-guide-4d8e0070843f
    # https://medium.com/@MaryDsa/step-by-step-guide-to-build-a-web-crawler-9cd0b69cd44c
   #  