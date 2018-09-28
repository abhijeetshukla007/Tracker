from rasa_core.channels.facebook import FacebookInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
    # load your trained agent
    
interpreter = RasaNLUInterpreter('./models/tracker/default/trackermodel')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)

input_channel = FacebookInput(
            fb_verify="1SLUOxZACyK14424dfgd2444242asdsdl29eHb2lmxqSGnadid1",
            # you need tell facebook this token, to confirm your URL
            fb_secret="49e74c993d6045abf5b43c03c39ba677",  # your app secret
            fb_access_token="EAAEdmlTd4jYBAKh1sT6diElbm4s59Hynqi6bZAou9sa4UA4IUghGZBtF2X5PxDhHv1zFZCEcirs5vXaKvcidTfvEb1FyWwW40lufwnB6bQkjRuPziXFZAR5NlByJ306HUSEhzHE1BxBhtUf0NxTY5KjnL6jIQMUpyh22lgCiVU5SIH0sDnrp"
            # token for the page you subscribed to
    )

    # set serve_forever=False if you want to keep the server running
s = agent.handle_channels([input_channel], 5006, serve_forever=True)