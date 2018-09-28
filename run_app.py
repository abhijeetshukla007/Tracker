from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig
from rasa_core.channels.console import get_cmd_input

nlu_interpreter = RasaNLUInterpreter('./models/tracker/default/trackermodel')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)

input_channel = SlackInput('xoxb-436359242450-436376353474-jA0IztB0WU2VIhjngI6YM645')

agent.handle_channels(get_cmd_input, 5004, serve_forever=True)