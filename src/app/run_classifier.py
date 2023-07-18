

from src.app.data_transformer import TransformData
from src.utils.other_utils import OtherUtils
from src.app.neural_network import NeuralNetwork



transform = TransformData()
otherutils = OtherUtils()
nn=NeuralNetwork()


class RunClassifier():

    def run(self):
        is_binary = otherutils.check_classification_type()
        X,y = transform.acquire_transformed_data()        
        model = nn.get_model()
        
        pass


if __name__ == '__main__':
    pass
    

    