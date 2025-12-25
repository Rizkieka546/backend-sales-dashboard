from pydantic import BaseModel
from typing import List

class SummaryResponse(BaseModel):
    total_records: int
    total_amount: float
    average_amount: float
    growth_percentage: float

class TimeSeriesItem(BaseModel):
    date: str
    total_amount: float

class CategoryItem(BaseModel):
    category: str
    total_amount: float
