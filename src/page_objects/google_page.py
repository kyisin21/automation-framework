
# Page Object for Google Search


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.page_objects.base_page import BasePage
from src.config.config import Config

class GooglePage(BasePage):
    # Locators
    SEARCH_BOX = (By.NAME, "q")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "div.g")
    SEARCH_RESULT_LINKS = (By.CSS_SELECTOR, "div.g a")
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//button[contains(text(), 'Accept all')]")
    
    def __init__(self, driver):
        # Initialize Google page object
        
        super().__init__(driver)
    
    def navigate_to_google(self):
        # Navigate to Google homepage and handle cookie consent if present

        self.navigate_to(Config.GOOGLE_URL)
        
        # Handle cookie consent if it appears
        try:
            if self.is_displayed(self.COOKIE_ACCEPT_BUTTON):
                self.click(self.COOKIE_ACCEPT_BUTTON)
        except:
    
            pass
    
    def search(self, query):
        # Perform a search on Google
        
        self.input_text(self.SEARCH_BOX, query)
        self.find_element(self.SEARCH_BOX).send_keys(Keys.RETURN)
        self.wait_for_page_load()
    
    def get_all_search_results(self):
        """
        Get all search results from the current page
        
        Returns:
            List of search result WebElements
        """
        return self.find_elements(self.SEARCH_RESULTS)
    
    def get_all_search_result_links(self):
        """
        Get all search result links
        
        Returns:
            List of (url, text) tuples
        """
        links = self.find_elements(self.SEARCH_RESULT_LINKS)
        return [(link.get_attribute('href'), link.text) for link in links if link.get_attribute('href')]
    
    def filter_gumtree_links(self, links):
        """
        Filter Gumtree links from a list of links
                  
        Returns:
            List of Gumtree (url, text) tuples
        """
        return [(url, text) for url, text in links if url and 'gumtree' in url.lower()]