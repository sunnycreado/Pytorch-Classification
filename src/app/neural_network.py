import torch
from torch import nn
from src.utils.other_utils import OtherUtils


otherutils = OtherUtils()


class NeuralNetwork():

    def create_model(self):

        class Model(nn.Module):

            def __init__(self) -> None:
                super().__init__()
                self.layers = nn.Sequential(
                    nn.Linear(in_features=otherutils.get_classes(),out_features=8),
                    nn.ReLU(),
                    nn.Linear(in_features=8,out_features=16),
                    nn.ReLU(),
                    nn.Linear(in_features=16,out_features=8),
                    nn.ReLU(),
                    nn.Linear(in_features=8,out_features=1)
                )
            
            def forward(self,x):
                return self.layers(x)
        
        model = Model().to(device=otherutils.get_device())
        return model
    


    
    def get_model(self):

        return self.create_model()
