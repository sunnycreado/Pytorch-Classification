import torch
from torch import nn
from src.utils.other_utils import OtherUtils
from src.utils.config_parser import ConfigReader


otherutils = OtherUtils()
config = ConfigReader()
HYPER_PARAMETERS = config.get_value('HyperParameters')


class NeuralNetwork():

    def create_model(self,is_binary):

        if not is_binary:

            class MultiClass(nn.Module):

                def __init__(self) -> None:
                    super().__init__()
                    self.layers = nn.Sequential(
                        nn.Linear(in_features=2,out_features=16),
                        nn.ReLU(),
                        # nn.Dropout(p=0.2),
                        nn.Linear(in_features=16,out_features=16),
                        nn.ReLU(),
                        # nn.Dropout(p=0.2),
                        nn.Linear(in_features=16,out_features=otherutils.get_classes()),

                    )
                
                def forward(self,x):
                    return self.layers(x)
                
            torch.cuda.manual_seed(HYPER_PARAMETERS['RandomState'])
            torch.manual_seed(HYPER_PARAMETERS['RandomState'])
            model = MultiClass().to(device=otherutils.get_device())
            return model
        
        else:

            class BinaryClass(nn.Module):

                def __init__(self,) -> None:
                    super().__init__()
                    self.layers = nn.Sequential(
                        nn.Linear(in_features=2 , out_features=16),
                        nn.Linear(in_features=16 , out_features=32),
                        nn.ReLU(),
                        nn.Linear(in_features=32 , out_features=64),
                        nn.ReLU(),
                        nn.Linear(in_features=64 , out_features=16),
                        nn.ReLU(),
                        nn.Linear(in_features=16 , out_features=4),
                        nn.Linear(in_features=4 , out_features=1)
                    )

                def forward(self,x):
                    return self.layers(x)
            

            torch.cuda.manual_seed(HYPER_PARAMETERS['RandomState'])
            torch.manual_seed(HYPER_PARAMETERS['RandomState'])
            model = BinaryClass().to(device=otherutils.get_device())
            return model
                
            

    
    
    def get_model(self,is_binary):

        return self.create_model(is_binary)
