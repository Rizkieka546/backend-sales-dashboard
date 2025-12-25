from fastapi import APIRouter
from typing import List
from app.services.analytics_service import AnalyticsService
from app.models.metrics import SummaryResponse, TimeSeriesItem, CategoryItem

router = APIRouter()
service = AnalyticsService()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.get("/metrics/summary", response_model=SummaryResponse)
def summary():
    return service.summary()

@router.get("/metrics/timeseries", response_model=List[TimeSeriesItem])
def timeseries():
    return service.timeseries()

@router.get("/metrics/category", response_model=List[CategoryItem])
def category():
    return service.category()
