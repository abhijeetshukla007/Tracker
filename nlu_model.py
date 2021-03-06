from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

def train_nlu(data, configs, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.load(configs))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir,project_name='tracker',fixed_model_name='trackermodel')
	
def run_nlu():
	interpreter = Interpreter.load('./models/tracker/trackermodel/')
	print(interpreter.parse("Hi"))
	
if __name__ == '__main__':
	train_nlu('./data/training_data.json', 'config.yml', './models')
	run_nlu()