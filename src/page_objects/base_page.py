
# Base Page Object that contains common methods for all page objects


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from src.config.config import Config

class BasePage:
    def __init__(self, driver):
        
        # Initialize the base page with WebDriver
   
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.DEFAULT_TIMEOUT)
    
    def navigate_to(self, url):
        # Navigate to a specific URL
        
        self.driver.get(url)
    
    def find_element(self, locator):
        """
        Find an element using a locator
         
        Returns:
            WebElement if found
            
        Raises:
            Exception: If element not found
        """
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Element not found with locator: {locator}")
    
    def find_elements(self, locator):
        """
        Find multiple elements using a locator
        
        Returns:
            List of WebElements if found
            
        Raises:
            Exception: If elements not found
        """
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            return []  # Return empty list instead of raising exception
    
    def click(self, locator):
        """
        Click on an element
            
        Raises:
            Exception: If element not clickable
        """
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            raise Exception(f"Element not clickable with locator: {locator}")
    
    def input_text(self, locator, text):
        """
        Input text in an element
        
            
        Raises:
            Exception: If failed to input text
        """
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            raise Exception(f"Failed to input text: {e}")
    
    def get_text(self, locator):
        """
        Get text from an element
                   
        Returns:
            Text of the element
            
        Raises:
            Exception: If failed to get text
        """
        try:
            element = self.find_element(locator)
            return element.text
        except Exception as e:
            raise Exception(f"Failed to get text: {e}")
    
    def is_displayed(self, locator):
        """
        Check if an element is displayed
            
        Returns:
            True if displayed, False otherwise
        """
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False
    
    def get_title(self):
        """
        Get the current page title
        
        Returns:
            Page title as string
        """
        return self.driver.title
    
    def wait_for_page_load(self):
        # Wait for page to completely load
    
        self.driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)