from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import rasa_core
from rasa_core.agent import Agent
from rasa_core.actions import Action
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies import MemoizationPolicy
from rasa_core.policies import KerasPolicy
from rasa_core.utils import EndpointConfig
from rasa_core.run import serve_application
from rasa_core.channels.channel import RestInput

import logging


def train_tracker_dialogue(
	domain_file="domain.yml",
	model_path="./models/dialogue",
	training_data_file="./data/stories.md",
):
	agent = Agent(domain_file, policies=[MemoizationPolicy(), KerasPolicy()])
	data = agent.load_data(training_data_file)
	agent.train(data, epochs=300, batch_size=50, validation_split=0.2)
	agent.persist(model_path)
	return agent

def run_tracker_bot(serve_forever=True):
	input_channel=RestInput()
	interpreter = RasaNLUInterpreter('./models/tracker/trackermodel')
	action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
	agent = Agent.load('./models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)
	rasa_core.run.serve_application(agent,port=5002,credentials_file="credentials.yml",cors="*")
		
	return agent

	# train_tracker_dialogue()
run_tracker_bot()

