from pydantic import BaseModel
from typing import List

class SearchResultData(BaseModel):
    case_number: str
    date_of_decision: str
    petitioner_name: str
    respondent_name: str
    case_type: str
