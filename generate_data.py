from src.utils.config_parser import ConfigReader
from src.datagenerator.data_generator import GenerateData

#default libraries



#Instantiation
config = ConfigReader()
generate_data = GenerateData()


#Global Parameters
DATA = config.get_value('Data')


if __name__ == "__main__":
    generate_data.start_generator(DATA['noise'])






