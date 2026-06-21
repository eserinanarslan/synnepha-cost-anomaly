from app.utils.file_loader import CsvLoader


class AnomalyService:

    def __init__(self, csv_path):

        self.csv_path = csv_path

    def get_all_anomalies(self):

        df = CsvLoader.load_csv(self.csv_path)

        return df.to_dict(orient="records")

    def get_anomaly_by_rank(self, rank):

        df = CsvLoader.load_csv(self.csv_path)

        result = df[df["anomaly_rank"] == rank]

        return result.to_dict(orient="records")