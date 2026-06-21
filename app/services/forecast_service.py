from app.utils.file_loader import CsvLoader


class ForecastService:

    def __init__(self, csv_path):

        self.csv_path = csv_path

    def get_forecast(self):

        df = CsvLoader.load_csv(self.csv_path)

        return df.to_dict(orient="records")