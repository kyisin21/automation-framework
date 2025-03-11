
# Configuration file for the automation framework


class Config:
    # Browser settings
    BROWSER = "chrome"
    HEADLESS = True
    
    # Timeouts (in seconds)
    DEFAULT_TIMEOUT = 10
    PAGE_LOAD_TIMEOUT = 30
    
    # URLs
    GOOGLE_URL = "https://www.google.com"
    JSON_PLACEHOLDER_API = "https://jsonplaceholder.typicode.com"
    
    # File paths
    TEST_DATA_PATH = "data/search_data.csv"