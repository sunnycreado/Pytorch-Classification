import json


CONFIG_PATH = r'config/config.json'



class ConfigReader():

    def __init__(self,path=CONFIG_PATH) -> None:
        self.config_file_path = path
        self.config_data = self._load_config()

    def _load_config(self):
        with open(self.config_file_path, 'r') as f:
            config_data = json.load(f)
        return config_data
    
    def get_value(self, key):
        if key in self.config_data:
            return self.config_data[key]
        else:
            return None
        
if __name__ == "__main__":
    config = ConfigReader()
    Data = config.get_value('Data')