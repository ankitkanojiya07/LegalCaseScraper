# Legal Case Scraper

## Overview
The Legal Case Scraper is a Python-based tool designed to scrape and model legal case information from a specified website. It efficiently extracts key details from search results and detailed case pages, providing structured data output using Pydantic models.

## Features
- **Search Results Scraping**: Extracts case number, date of decision, petitioner name, respondent name, and case type from the first page of search results.
- **Detailed Case Scraping**: Gathers comprehensive case details including registration number, filing date, parties involved, advocates, judges, hearing history, applicable acts, and orders.
- **Data Modeling**: Uses Pydantic models to ensure data is structured, validated, and easily usable.

## Requirements
- Python 3.7+
- `requests`
- `beautifulsoup4`
- `pydantic`

## Installation
1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/legal-case-scraper.git
    cd legal-case-scraper
    ```

2. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Scraping Search Results
To scrape the first page of search results, update the `search_url` variable with the actual URL of the search results page and run the scraper.

```python
from scraper import scrape_search_results

search_url = 'https://example.com/search-results'
search_results = scrape_search_results(search_url)

for result in search_results:
    print(result.json())
