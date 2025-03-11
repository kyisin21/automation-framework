# Test cases for Google search functionality

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from src.page_objects.google_page import GooglePage
from src.page_objects.gumtree_page import GumtreePage
from src.utils.csv_reader import CSVReader
from src.config.config import Config

class TestGoogleSearch:
    @pytest.fixture(scope="function")
    def setup(self):
        
        # Set up WebDriver before tests and teardown after
        
        print("\n----- Setting up browser -----")
        options = Options()
        
        if Config.HEADLESS:
            options.add_argument("--headless")
            
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--window-size=1920,1080")
        
        # Set up the driver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        
        yield driver
        
        # Teardown
        print("\n----- Closing browser -----")
        driver.quit()
    
    def test_google_search_gumtree_cars(self, setup):
        """
        Test Scenario:
        1. Open Google and search for "Cars in London" (from CSV)
        2. Count Gumtree links in search results
        3. Navigate to each Gumtree link and verify title and results
        """
        driver = setup
        google_page = GooglePage(driver)
        gumtree_page = GumtreePage(driver)
        
        # Step 1: Read test data from CSV and perform search
        search_query = CSVReader.get_search_query(Config.TEST_DATA_PATH)
        print(f"\nPerforming Google search for: '{search_query}'")
        
        google_page.navigate_to_google()
        google_page.search(search_query)
        
        # Step 2: Get all search results and filter Gumtree links
        all_links = google_page.get_all_search_result_links()
        gumtree_links = google_page.filter_gumtree_links(all_links)
        
        # Print the count of Gumtree links found
        gumtree_count = len(gumtree_links)
        print(f"Found {gumtree_count} Gumtree links in the search results")
        
        # If no Gumtree links found, the test should fail
        assert gumtree_count > 0, "No Gumtree links found in search results"
        
        # Step 3: Navigate to each Gumtree link and validate
        for i, (url, link_text) in enumerate(gumtree_links, 1):
            print(f"\nNavigating to Gumtree link {i}/{gumtree_count}: {url}")
            
            gumtree_page.navigate_to_gumtree_page(url)
            
            # Verify title is displayed
            assert gumtree_page.is_title_displayed(), f"Page title not displayed for {url}"
            print(f"Page title verification: PASSED")
            
            # Verify there are search results (either by count or presence of results)
            results_count = gumtree_page.get_results_count()
            if results_count > 0:
                print(f"Results count: {results_count} (PASSED)")
            else:
                # If count couldn't be retrieved, check if results are present
                assert gumtree_page.has_search_results(), f"No search results found for {url}"
                print(f"Results present but count not available (PASSED)")
            
            # Navigate back to Google for the next iteration if needed
            if i < gumtree_count:
                driver.back()