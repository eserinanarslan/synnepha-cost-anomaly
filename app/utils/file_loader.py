import pandas as pd


class CsvLoader:

    @staticmethod
    def load_csv(file_path):

        return pd.read_csv(file_path)