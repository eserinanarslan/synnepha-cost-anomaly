from pydantic import BaseModel


class ForecastResponse(BaseModel):

    date: str
    forecast_cost_usd: float