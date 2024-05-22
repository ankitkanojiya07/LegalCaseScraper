import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel
from typing import List

# Define the Pydantic models
class SearchResultData(BaseModel):
    case_number: str
    date_of_decision: str
    petitioner_name: str
    respondent_name: str
    case_type: str

class CaseDetails(BaseModel):
    registration_number: str
    filing_date: str
    parties_involved: List[str]
    advocates: List[str]
    judges: List[str]
    hearing_history: List[dict]
    applicable_acts: List[str]
    orders: List[dict]

# Function to scrape the first page of search results
def scrape_search_results(url: str) -> List[SearchResultData]:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    search_results = []
    for case in soup.select('.case-selector'):  # Adjust selector based on actual HTML structure
        case_number = case.select_one('.case-number').text.strip()
        date_of_decision = case.select_one('.date-of-decision').text.strip()
        petitioner_name = case.select_one('.petitioner-name').text.strip()
        respondent_name = case.select_one('.respondent-name').text.strip()
        case_type = case.select_one('.case-type').text.strip()
        
        search_result = SearchResultData(
            case_number=case_number,
            date_of_decision=date_of_decision,
            petitioner_name=petitioner_name,
            respondent_name=respondent_name,
            case_type=case_type
        )
        search_results.append(search_result)
    
    return search_results

# Function to scrape detailed case information
def scrape_case_details(case_number: str) -> CaseDetails:
    case_url = f"https://example.com/case-details/{case_number}"  # Adjust URL as needed
    response = requests.get(case_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    registration_number = soup.select_one('.registration-number').text.strip()
    filing_date = soup.select_one('.filing-date').text.strip()
    parties_involved = [party.text.strip() for party in soup.select('.parties-involved')]
    advocates = [adv.text.strip() for adv in soup.select('.advocates')]
    judges = [judge.text.strip() for judge in soup.select('.judges')]
    hearing_history = [
        {
            'date': hearing.select_one('.hearing-date').text.strip(),
            'purpose': hearing.select_one('.hearing-purpose').text.strip()
        } for hearing in soup.select('.hearing-history')
    ]
    applicable_acts = [act.text.strip() for act in soup.select('.applicable-acts')]
    orders = [
        {
            'type': order.select_one('.order-type').text.strip(),
            'date': order.select_one('.order-date').text.strip(),
            'description': order.select_one('.order-description').text.strip()
        } for order in soup.select('.orders')
    ]
    
    case_details = CaseDetails(
        registration_number=registration_number,
        filing_date=filing_date,
        parties_involved=parties_involved,
        advocates=advocates,
        judges=judges,
        hearing_history=hearing_history,
        applicable_acts=applicable_acts,
        orders=orders
    )
    
    return case_details

# Sample usage
search_url = 'https://example.com/search-results'
search_results = scrape_search_results(search_url)

for result in search_results:
    case_details = scrape_case_details(result.case_number)
    print(case_details.json())
