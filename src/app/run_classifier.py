

from src.app.data_transformer import TransformData
from src.utils.other_utils import OtherUtils
from src.app.neural_network import NeuralNetwork
from src.app.trainer import Trainer
from src.utils.plot_utilities import PlotGraphs





transform = TransformData()
otherutils = OtherUtils()
nn=NeuralNetwork()
train = Trainer()
plot_graphs =PlotGraphs()


class RunClassifier():

    def run(self):
        is_binary = otherutils.check_classification_type()
        X,y = transform.acquire_transformed_data(is_binary)        
        data = transform.split_data(X,y)
        model = nn.get_model(is_binary)
        train.train_model(model,data[0],data[2])
        train.test_model(model,data[1],data[3])
        plot_graphs.plot_decision_boundary(model=model,X=data[1],y=data[3])
        
        
        pass


if __name__ == '__main__':
    pass
    

    