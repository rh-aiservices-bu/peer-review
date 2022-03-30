import configparser
import os
import shutil

class getConfig():

    def __init__(self, path):

        settings = configparser.ConfigParser()
        settings._interpolation = configparser.ExtendedInterpolation()
        settings.read(path + 'config')
        settings.sections()
        # path to data folder
        self.input_data = path + settings.get('Data', 'input')
        self.version = settings.get('Run', 'version')

        # Prepare data directory for current run
        self.experiments_path = path + settings.get('Path', 'experiments') + "experiment_" + self.version + "/" 
        self.plots_path = self.experiments_path + settings.get('Data', 'plots')
        self.traintest_path = self.experiments_path + settings.get('Data', 'train-test')
        self.trained_path = self.experiments_path + settings.get('Model', 'trained')
        self.tuned_path = self.experiments_path + settings.get('Model', 'tuned')
        self.inference_path = path + settings.get('Data', 'inference')
      
    def cleanup(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            shutil.rmtree(path)
            os.makedirs(path)
