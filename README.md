# Web Crawler Project

## Overview
The **Web Crawler** is a project designed to systematically browse and extract data from websites. This tool is useful for data collection, indexing, and analysis. The crawler efficiently retrieves web pages, follows links, and processes relevant information while adhering to site policies.

## Features
- **Multi-threaded Crawling**: Supports concurrent requests for faster data retrieval.
- **Customizable URL Filtering**: Specify allowed domains and exclude unwanted links.
- **Data Extraction**: Extract useful information such as text, images, and links.
- **Robots.txt Compliance**: Respects web crawling policies.
- **User-Agent Customization**: Mimics different browsers to avoid detection.
- **Data Storage**: Saves extracted data in JSON, CSV, or database formats.

## Technologies Used
- **Programming Language**: Python
- **Frameworks/Libraries**:
  - BeautifulSoup (for parsing HTML)
  - Requests (for HTTP requests)
  - Scrapy (for advanced crawling)
  - pytest (for white box testing)
  - SQLite / MongoDB (for storing crawled data)

## Installation
### Prerequisites
Ensure you have Python 3.x installed on your system.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/web-crawler.git
   cd web-crawler
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the crawler:
   ```bash
   python main.py --url "https://example.com" --depth 2
   ```

## Usage
- Modify  `enchanced_crawler.py` customize settings such as:
  - **Max depth of crawling**
  - **Allowed/Disallowed domains**
  - **Data storage options**
- Run the crawler with different parameters as needed.
- Analyze and visualize the collected data.

## Contributing
Contributions are welcome! Feel free to submit issues and pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any inquiries, reach out via email at **Praneethsai520@gmail.com** or create an issue in the repository.

