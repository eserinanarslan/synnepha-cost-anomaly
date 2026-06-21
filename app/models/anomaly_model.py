from pydantic import BaseModel


class AnomalyResponse(BaseModel):

    anomaly_rank: int
    date: str
    total_cost_usd: float
    detection_rate: float