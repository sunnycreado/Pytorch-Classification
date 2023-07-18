import sys
import os
from src.utils.config_parser import ConfigReader
from src.utils.other_utils import OtherUtils
import torch
from sklearn.model_selection import train_test_split

config = ConfigReader()
otherutils = OtherUtils()
Data = config.get_value('Data')
HYPER_PARAMETERS = config.get_value('HyperParameters')

class TransformData():


    
    def seperate_data(self,df):
        """
            Split the data in X and y as data vector and output classes 

        """
        X,y = df.iloc[:,:2].to_numpy(dtype=float),df.iloc[:,2].to_numpy(dtype=float)
        return X,y
    
    
    
    def shift_to_device(self,X,y,device,is_binary):

        if not is_binary:
            X = torch.from_numpy(X).type(torch.float).to(device)
            y = torch.from_numpy(y).type(torch.LongTensor).to(device)
            return X,y

    def split_data(self,X,y):
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=Data['test_size'],random_state=HYPER_PARAMETERS['RandomState'])
        return [X_train,X_test,y_train,y_test]

    


    def acquire_transformed_data(self,is_binary):
        df = otherutils.get_df()
        device = otherutils.get_device()
        X,y = self.seperate_data(df)
        X,y = self.shift_to_device(X,y,device,is_binary)
        return X,y
    

    












