import pytest
import requests_mock
from bs4 import BeautifulSoup
from TEST_Bot import enhanced_crawler
from TEST_Bot.enhanced_crawler import EnhancedWebCrawler  # Ensure correct import

@pytest.fixture
def crawler(): # type: ignore
    """Fixture to initialize the web crawler with a test URL."""
    return enhanced_crawler.EnhancedWebCrawler("https://medium.com/@Ivan-Smith-308/how-to-write-wig-business-plan-example-guide-4d8e0070843f", max_pages=5) # type: ignore


# test case function 2
def test_crawl_page_success(crawler):
    """Test if `crawl_page` successfully fetches and extracts content."""
    mock_html = """
    <html>
        <head><title>Test Page</title></head>
        <body>
            <h1>Main Heading</h1>
            <h2>Subheading 1</h2>
            <h3>Subheading 2</h3>
            <a href="https://medium.com/@Ivan-Smith-308/how-to-write-wig-business-plan-example-guide-4d8e0070843f">Next Page</a>
        </body>
    </html>
    """
    with requests_mock.Mocker() as m:
        m.get("https://medium.com/@Ivan-Smith-308/how-to-write-wig-business-plan-example-guide-4d8e0070843f", text=mock_html)
        
        crawler.crawl_page("https://medium.com/@Ivan-Smith-308/how-to-write-wig-business-plan-example-guide-4d8e0070843f")

        # Validate extracted headings
        assert ("Title", "Test Page") in crawler.headings
        assert ("h1", "Main Heading") in crawler.headings
        assert ("h2", "Subheading 1") in crawler.headings
        assert ("h3", "Subheading 2") in crawler.headings

        # Ensure the next page is added to visited URLs
        assert "https://medium.com/@Ivan-Smith-308/how-to-write-wig-business-plan-example-guide-4d8e0070843f" in crawler.visited_urls





#test case function 3

# import pytest
# from TEST_Bot.enhanced_crawler import EnhancedWebCrawler  # Ensure correct import

def crawler2():  # noqa: F811
    """Fixture to initialize the web crawler with a test URL."""
    return EnhancedWebCrawler("https://medium.com/@Ivan-Smith-308/how-to-use-chatgpt-to-write-a-business-plan-example-b58dac868207", max_pages=5)

def test_crawl_medium_articles(crawler):
    """Test crawling two Medium articles."""
    article1_html = """
    <html>
        <head><title>Using ChatGPT for Business Plans</title></head>
        <body>
            <h1>How to Use ChatGPT to Write a Business Plan</h1>
            <h2>Introduction</h2>
            <h3>AI and Business Planning</h3>
        </body>
    </html>
    """

    article2_html = """
    <html>
        <head><title>Wig Business Plan Guide</title></head>
        <body>
            <h1>How to Write a Wig Business Plan</h1>
            <h2>Step 1</h2>
            <h3>Introduction</h3>
        </body>
    </html>
    """

    with requests_mock.Mocker() as m:
       
        m.get("https://medium.com/@Ivan-Smith-308/how-to-use-chatgpt-to-write-a-business-plan-example-b58dac868207", text=article1_html)
        m.get("https://medium.com/@Ivan-Smith-308/how-to-write-wig-business-plan-example-guide-4d8e0070843f", text=article2_html)

        # Start crawling both URLs
        crawler.crawl_page("https://medium.com/@Ivan-Smith-308/how-to-use-chatgpt-to-write-a-business-plan-example-b58dac868207")
        crawler.crawl_page("https://medium.com/@Ivan-Smith-308/how-to-write-wig-business-plan-example-guide-4d8e0070843f")

        # Validate Article 1 extraction
        assert ("Title", "Using ChatGPT for Business Plans") in crawler.headings
        assert ("h1", "How to Use ChatGPT to Write a Business Plan") in crawler.headings
        assert ("h2", "Introduction") in crawler.headings
        assert ("h3", "AI and Business Planning") in crawler.headings

        # Validate Article 2 extraction
        assert ("Title", "Wig Business Plan Guide") in crawler.headings
        assert ("h1", "How to Write a Wig Business Plan") in crawler.headings
        assert ("h2", "Step 1") in crawler.headings
        assert ("h3", "Introduction") in crawler.headings


#Test case function 3

def test_extract_content(crawler):
    """Test heading extraction from an HTML page."""
    html = """
    <html>
        <head><title>Sample Page</title></head>
        <body>
            <h1>Header One</h1>
            <h2>Header Two</h2>
            <h3>Header Three</h3>
        </body>
    </html>
    """
    soup = BeautifulSoup(html, "html.parser")
    crawler.extract_content(soup)

    assert ("Title", "Sample Page") in crawler.headings
    assert ("h1", "Header One") in crawler.headings
    assert ("h2", "Header Two") in crawler.headings
    assert ("h3", "Header Three") in crawler.headings








#Test case function 4


def test_max_pages_limit():
    """Test if `max_pages` constraint works."""
    crawler = EnhancedWebCrawler("https://example.com", max_pages=2)

    mock_html = """
    <html>
        <body>
            <a href="https://example.com/page1">Page 1</a>
            <a href="https://example.com/page2">Page 2</a>
            <a href="https://example.com/page3">Page 3</a>
        </body>
    </html>
    """
    with requests_mock.Mocker() as m:
        m.get("https://example.com", text=mock_html)
        m.get("https://example.com/page1", text=mock_html)
        m.get("https://example.com/page2", text=mock_html)
        m.get("https://example.com/page3", text=mock_html)

        crawler.crawl_page("https://example.com")

        # Ensure we only visit up to `max_pages`
        assert len(crawler.visited_urls) == 2  # The start page + 1 other page
