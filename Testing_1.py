import pytest
import requests_mock
from TEST_Bot import enhanced_crawler
# from TEST_Bot.enhanced_crawler import EnhancedWebCrawler  # Ensure correct import

@pytest.fixture
def crawler():
    """Fixture to initialize the web crawler with a test URL."""
    return enhanced_crawler.EnhancedWebCrawler("https://medium.com/@Ivan-Smith-308/how-to-use-chatgpt-to-write-a-business-plan-example-b58dac868207", max_pages=5)

def test_crawl_medium_articles(crawler):
    """Test crawling two Medium articles."""
    article1_html = """
    <html>
        <head><title>Using ChatGPT for Business Plans</title></head>
        <body>
            <h1>How to Use ChatGPT to Write a Business Plan</h1>
            <h2>Introduction</h2>
            <h3>AI and Business Planning</h3>
            <a href="https://medium.com/@Ivan-Smith-308/page2">Next Page</a>
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
            <a href="https://medium.com/@Ivan-Smith-308/page3">Next Page</a>
        </body>
    </html>
    """

    with requests_mock.Mocker() as m:
        # Mock both Medium URLs
        m.get("https://medium.com/@Ivan-Smith-308/how-to-use-chatgpt-to-write-a-business-plan-example-b58dac868207", text=article1_html)
        m.get("https://medium.com/@Ivan-Smith-308/page2", text=article1_html)

        m.get("https://medium.com/@Ivan-Smith-308/how-to-write-wig-business-plan-example-guide-4d8e0070843f", text=article2_html)
        m.get("https://medium.com/@Ivan-Smith-308/page3", text=article2_html)

        
        crawler.crawl_page("https://medium.com/@Ivan-Smith-308/how-to-use-chatgpt-to-write-a-business-plan-example-b58dac868207")
        crawler.crawl_page("https://medium.com/@Ivan-Smith-308/how-to-write-wig-business-plan-example-guide-4d8e0070843f")

        
        assert ("Title", "Using ChatGPT for Business Plans") in crawler.headings
        assert ("h1", "How to Use ChatGPT to Write a Business Plan") in crawler.headings
        assert ("h2", "Introduction") in crawler.headings
        assert ("h3", "AI and Business Planning") in crawler.headings
        assert "https://medium.com/@Ivan-Smith-308/page2" in crawler.visited_urls

       
        assert ("Title", "Wig Business Plan Guide") in crawler.headings
        assert ("h1", "How to Write a Wig Business Plan") in crawler.headings
        assert ("h2", "Step 1") in crawler.headings
        assert ("h3", "Introduction") in crawler.headings
        assert "https://medium.com/@Ivan-Smith-308/page3" in crawler.visited_urls
