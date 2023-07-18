import torch
import pandas as pd 
import torch
import os 


from src.utils.config_parser import ConfigReader



config = ConfigReader()
Data = config.get_value('Data')

class OtherUtils():

    def get_df(self):
        data_path = os.path.join(Data['base_data_path']+Data['filename'])
        df = pd.read_excel(data_path)
        return df

    def get_classes(self):
        df=self.get_df()
        classes =len(df['Color Class'].unique())
        return classes


    def check_classification_type(self):
        classes= self.get_classes()
        is_binary = False if classes>2 else True
        return is_binary
    
    def get_device(self):
        return 'cuda' if torch.cuda.is_available() else 'cpu'
