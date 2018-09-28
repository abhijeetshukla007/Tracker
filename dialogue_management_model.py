from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import rasa_core
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.channels.facebook import FacebookInput
from rasa_core.run import serve_application


logger = logging.getLogger(__name__)


def train_dialogue(
    domain_file="domain.yml",
    model_path="./models/dialogue",
    training_data_file="./data/stories.md",
):

    agent = Agent(domain_file, policies=[MemoizationPolicy(), KerasPolicy()])
    data = agent.load_data(training_data_file)
    agent.train(data, epochs=250, batch_size=50, validation_split=0.2)

    agent.persist(model_path)
    return agent


input_channel = FacebookInput(
    fb_verify="1SLUOxZACyK14424df-rasa-bot",
    # you need tell facebook this token, to confirm your URL
    fb_secret="49e74c993d6045abf5b43c03c39ba677",  # your app secret
    fb_access_token="EAAEdmlTd4jYBAKh1sT6diElbm4s59Hynqi6bZAou9sa4UA4IUghGZBtF2X5PxDhHv1zFZCEcirs5vXaKvcidTfvEb1FyWwW40lufwnB6bQkjRuPziXFZAR5NlByJ306HUSEhzHE1BxBhtUf0NxTY5KjnL6jIQMUpyh22lgCiVU5SIH0sDnrp"
    # token for the page you subscribed to
)

def run_tracker_bot(serve_forever=True):
    interpreter = RasaNLUInterpreter("./models/tracker/default/trackermodel")
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    agent = Agent.load(
        "./models/dialogue", interpreter=interpreter, action_endpoint=action_endpoint
    )
    rasa_core.run.serve_application(agent, "cmdline",5005,"credentials.yml")
    return agent


if __name__ == "__main__":
    # train_dialogue()
    run_tracker_bot()

