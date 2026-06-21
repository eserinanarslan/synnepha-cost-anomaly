from fastapi import APIRouter

from app.config.settings import Settings
from app.services.anomaly_service import AnomalyService
from app.services.forecast_service import ForecastService


router = APIRouter()

settings = Settings()

anomaly_service = AnomalyService(
    settings.anomaly_file
)

forecast_service = ForecastService(
    settings.forecast_file
)


@router.get("/health")
def health():

    return {"status": "healthy"}


@router.get("/anomalies")
def get_anomalies():

    return anomaly_service.get_all_anomalies()


@router.get("/anomalies/{rank}")
def get_anomaly(rank: int):

    return anomaly_service.get_anomaly_by_rank(rank)


@router.get("/forecast")
def get_forecast():

    return forecast_service.get_forecast()