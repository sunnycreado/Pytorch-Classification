import sys
import os
from src.utils.config_parser import ConfigReader
from src.utils.other_utils import OtherUtils
import torch

config = ConfigReader()
otherutils = OtherUtils()
Data = config.get_value('Data')

class TransformData():


    
    def split_data(self,df):
        """
            Split the data in X and y as data vector and output classes 

        """
        X,y = df.iloc[:,:2].to_numpy(dtype=float),df.iloc[:,2].to_numpy(dtype=float)
        return X,y
    
    
    
    def shift_to_device(self,X,y,device):
        X = torch.from_numpy(X).type(torch.float).to(device)
        y = torch.from_numpy(y).type(torch.float).to(device)
        return X,y

        
    


    def acquire_transformed_data(self):
        df = otherutils.get_df()
        X,y = self.split_data(df)
        device = otherutils.get_device()
        X,y = self.shift_to_device(X,y,device)
        return X,y










