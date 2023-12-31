import torch
from src.utils.config_parser import ConfigReader




config = ConfigReader()

HYPER_PARAMETERS = config.get_value('HyperParameters')


class ModelFunction():

    def get_loss_fn(self,is_binary):

        if is_binary:
            loss_fn = torch.nn.BCEWithLogitsLoss()
            return loss_fn
        else:
            loss_fn = torch.nn.CrossEntropyLoss()
            return loss_fn
    
    def get_accuracy_fn(self):

        def accuracy_fn(y_true,y_pred):
            correct = torch.eq(y_true,y_pred).sum().item()
            acc = (correct/len(y_true))*100
            return acc

        return accuracy_fn
    
    def get_optimizer(self,model):
        return torch.optim.SGD(model.parameters(),lr=HYPER_PARAMETERS['learningrate'])
    
    def get_pred_from_logits(self,is_binary,logits):
        if is_binary:
            return torch.round(torch.sigmoid(logits))
        else: 
            return torch.softmax(logits,dim=1).argmax(dim=1)
        
    def get_logits(self,is_binary,model,data):
        if is_binary:
            return model(data).squeeze()
        else:
            return model(data)


        

