from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig
from rasa_core.channels.console import get_cmd_input
from rasa_core.channels.facebook import FacebookInput

nlu_interpreter = RasaNLUInterpreter('./models/tracker/trackermodel/')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)

facebook_channel = FacebookInput(
    fb_verify="1SLUOxZACyK14424df-rasa-bot",
    # you need tell facebook this token, to confirm your URL
    fb_secret="49e74c993d6045abf5b43c03c39ba677",  # your app secret
    fb_access_token="EAAEdmlTd4jYBAFVmoVL4JHjZAhOl1m3lQlZCPMZAZB2QtQuOdNQifsA1omt8dzD69wLtk12YY011hxt7sTB3Ih4Aq3aN28s3a2gvQWtgGWHOQkZC3AVBhp3N9YYGkbHIeUE7zvNaQXlO93KLJOaYdpisuek6zT8OSDQYiw17yZAbdcZCfgLkDJu"
    # token for the page you subscribed to
)

slack_channel = SlackInput('xoxb-436359242450-436376353474-jA0IztB0WU2VIhjngI6YM645')

agent.handle_channels([slack_channel,facebook_channel], 5004, serve_forever=True)