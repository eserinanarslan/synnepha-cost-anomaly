import yaml


class Settings:

    def __init__(self, config_path="config.yaml"):

        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

    @property
    def anomaly_file(self):
        return self.config["files"]["anomaly_file"]

    @property
    def forecast_file(self):
        return self.config["files"]["forecast_file"]

    @property
    def host(self):
        return self.config["server"]["host"]

    @property
    def port(self):
        return self.config["server"]["port"]