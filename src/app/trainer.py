from src.app.model_functions import ModelFunction
from src.utils.config_parser import ConfigReader
from src.utils.other_utils import OtherUtils
import torch


model_function = ModelFunction()
config = ConfigReader()
other_utils= OtherUtils()
HYPER_PARAMETERS = config.get_value('HyperParameters')



class Trainer():


    def get_functions(self,is_binary,model):

        loss_fn = model_function.get_loss_fn(is_binary)
        accuracy_fn = model_function.get_accuracy_fn()
        optimizer = model_function.get_optimizer(model)

        return loss_fn,accuracy_fn,optimizer


    def train_model(self,model,data):

        X_train,X_test,y_train,y_test = data

        is_binary = other_utils.check_classification_type()

        loss_fn,accuracy_fn,optimizer = self.get_functions(is_binary,model)

        if not is_binary:

            torch.manual_seed(HYPER_PARAMETERS['RandomState'])
            torch.cuda.manual_seed(HYPER_PARAMETERS['RandomState'])

            for epoch in range(HYPER_PARAMETERS['epochs']):

                model.train()

                train_logits = model(X_train)
                train_pred = torch.softmax(train_logits,dim=1).argmax(dim=1)

                train_loss = loss_fn(train_logits,y_train)
                train_acc = accuracy_fn(y_train,train_pred)

                optimizer.zero_grad()

                train_loss.backward()

                optimizer.step()


                model.eval()


                with torch.inference_mode():
                    test_logits = model(X_test)
                    test_pred = torch.softmax(test_logits,dim=1).argmax(dim=1)

                    test_loss = loss_fn(test_logits,y_test)
                    test_acc = accuracy_fn(y_test,test_pred)



                if epoch%100 == 0 :
                    print(f'epoch : {epoch},Training Loss: {train_loss},Testing Loss: {test_loss},Training Accuracy: {train_acc}, Testing Accuracy: {test_acc}')

        return model


                


    # def test_model(self,model,X_test,y_test):

    #     is_binary = other_utils.check_classification_type()

    #     loss_fn,accuracy_fn,optimizer = self.get_functions(is_binary,model)

    #     if not is_binary:


    #         model.eval()

    #         with torch.inference_mode():
    #             test_logits = model(X_test)
    #             test_pred = torch.softmax(test_logits,dim=1).argmax(dim=1)

    #             test_loss = loss_fn(test_logits,y_test)
    #             test_acc = accuracy_fn(y_test,test_pred)


    #             print(f'Training Loss: {test_loss},Training Accuracy: {test_acc}')
