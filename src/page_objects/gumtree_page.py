
# Page Object for Gumtree page


from selenium.webdriver.common.by import By
from src.page_objects.base_page import BasePage

class GumtreePage(BasePage):
    # Locators - These may need to be adjusted based on actual Gumtree page structure
    RESULTS_COUNT = (By.CSS_SELECTOR, "h1.results-count")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "div.listing-maincontent")
    COOKIE_ACCEPT_BUTTON = (By.CSS_SELECTOR, "button#onetrust-accept-btn-handler")
    
    def __init__(self, driver):
        # Initialize Gumtree page object
        
        super().__init__(driver)
    
    def navigate_to_gumtree_page(self, url):
        # Navigate to a specific Gumtree page

        self.navigate_to(url)
        self.wait_for_page_load()
        
        # Handle cookie consent if it appears
        try:
            if self.is_displayed(self.COOKIE_ACCEPT_BUTTON):
                self.click(self.COOKIE_ACCEPT_BUTTON)
        except:
            # Cookie consent might not appear, so we can ignore errors
            pass
    
    def get_results_count(self):
        """
        Get the number of results displayed on the page
        
        Returns:
            Integer count of results, or 0 if not found
        """
        try:
            results_text = self.get_text(self.RESULTS_COUNT)
            # Extract the number from text like "123 ads"
            return int(''.join(filter(str.isdigit, results_text)))
        except:
            # If unable to get results count, return 0
            return 0
    
    def has_search_results(self):
        """
        Check if the page has any search results
        
        Returns:
            True if results are found, False otherwise
        """
        return len(self.find_elements(self.SEARCH_RESULTS)) > 0
    
    def is_title_displayed(self):
        """
        Check if the page title is properly displayed
        
        Returns:
            True if title exists and is not empty, False otherwise
        """
        return bool(self.get_title())