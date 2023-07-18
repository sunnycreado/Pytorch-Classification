import torch

class ModelFunction():

    def get_loss_fn(self,is_binary,y_logits,y_true):

        if is_binary:
            loss_fn = torch.nn.BCEWithLogitsLoss(y_logits,y_true)
            return loss_fn
        else:
            loss_fn = torch.nn.CrossEntropyLoss(y_logits,y_true)
            return loss_fn
    
    def get_accuracy_fn(self,y_pred,y_true):
        correct = torch.eq(y_true,y_pred).sum().item()
        acc = (correct/len(y_true))*100
        return acc

