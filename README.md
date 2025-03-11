A comprehensive automation framework for UI and API testing using Python, Selenium with Page Object Model, and Pytest.

# Overview

This framework provides a structured approach to:
- Web UI Automation (Selenium WebDriver)
- API Testing (Requests library)
- Data-driven Testing (CSV data sources)

# Features

- Page Object Model design pattern for UI tests
- Clean separation of test data, test logic, and page interactions
- API client for RESTful service testing
- CSV-based test data management
- HTML reporting
- Easy to extend and maintain

# Project Structure

```
automation-framework/
│
├── data/                     # Test data in CSV format
│   └── search_data.csv       # CSV file containing search queries
|
├── docs/                     # Explaining the automation approach
│   └── automation_pipeline.md 
|
├── src/                      
│   ├── config/               # Configuration files
│   │   └── config.py        
│   │
│   ├── page_objects/         # Page Object Models
│   │   ├── base_page.py      # Base page with common methods
│   │   ├── google_page.py    # Google search page objects
│   │   └── gumtree_page.py   # Gumtree page objects
│   │
│   ├── utils/                
│       ├── api_client.py     # API client for REST API calls
│       └── csv_reader.py     # Utility to read CSV data
│
├── tests/                    # Test cases
│   ├── api/                  # API Tests
│   │   └── test_json_placeholder.py
│   │
│   └── ui/                   # UI Tests
│       └── test_google_search.py
│
├── conftest.py               # Pytest configurations
├── README.md                 # General documentation
└── requirements.txt          # Dependencies for the project
```


# Setup Instructions

# Prerequisites

- Python 3.9 or higher
- Chrome browser installed
- Internet connection

# Installation

1. Clone the repository:
   ```
   git clone https://github.com/kyisin21/automation-framework.git
   cd automation-framework
   ```

2. Create and activate a virtual environment:
   ```
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

# Running Tests

# UI Tests

To run the Google search UI tests:

```
pytest tests/ui/test_google_search.py -v
```

# API Tests

To run the JSONPlaceholder API tests:

```
pytest tests/api/test_json_placeholder.py -v
```

# Run All Tests

To run all tests:

```
pytest
```

# Generate HTML Report

Reports are automatically generated in the `reports` directory with timestamp.

To view a report, open the generated HTML file in any web browser.

# Customization

# Modifying Test Data

- Edit the CSV files in the `data` directory to change test inputs.
- For the Google search test, modify `data/search_data.csv` to change the search query.


# CI/CD Integration

This framework can be easily integrated with CI/CD pipelines like Jenkins, GitHub Actions, or GitLab CI. See `docs/automation_pipeline.md` for details.

# Troubleshooting

Common issues:

1. WebDriver not found:
   ```
   pip install --upgrade webdriver-manager
   ```

2. Test data not found:
   - Ensure your working directory is the project root when running tests

3. Browser compatibility:
   - The framework is configured for Chrome by default
   - For other browsers, modify the driver setup in tests