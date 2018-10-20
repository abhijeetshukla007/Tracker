from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from collections import defaultdict
from datetime import datetime
import json
import logging
from uuid import uuid4
from flask import Blueprint, jsonify, request, Flask, Response, make_response
from flask_cors import CORS
from rasa_core import utils
from rasa_core.channels import UserMessage
from rasa_core.channels.channel import InputChannel, OutputChannel,QueueOutputChannel,CollectingOutputChannel
from rasa_core.events import SlotSet

logger = logging.getLogger()

class RestInput(InputChannel):
    """A custom http input channel.

    This implementation is the basis for a custom implementation of a chat
    frontend. You can customize this to send messages to Rasa Core and
    retrieve responses from the agent."""

    @classmethod
    def name(cls):
        return "rest"

    @staticmethod
    def on_message_wrapper(on_new_message, text, queue, sender_id):
        collector = QueueOutputChannel(queue)

        message = UserMessage(text, collector, sender_id,
                              input_channel=RestInput.name())
        on_new_message(message)

        queue.put("DONE")

    def _extract_sender(self, req):
        return req.json.get("sender", None)

    # noinspection PyMethodMayBeStatic
    def _extract_message(self, req):
        return req.json.get("message", None)

    def stream_response(self, on_new_message, text, sender_id):
        from multiprocessing import Queue

        q = Queue()

        t = Thread(target=self.on_message_wrapper,
                   args=(on_new_message, text, q, sender_id))
        t.start()
        while True:
            response = q.get()
            if response == "DONE":
                break
            else:
                yield json.dumps(response) + "\n"

    def blueprint(self, on_new_message):
        custom_webhook = Blueprint(
                'custom_webhook_{}'.format(type(self).__name__),
                inspect.getmodule(self).__name__)

        @custom_webhook.route("/", methods=['GET'])
        def health():
            return jsonify({"status": "ok"})

        @custom_webhook.route("/webhook", methods=['POST'])
        def receive():
            sender_id = self._extract_sender(request)
            text = self._extract_message(request)
            should_use_stream = utils.bool_arg("stream", default=False)

            if should_use_stream:
                return Response(
                        self.stream_response(on_new_message, text, sender_id),
                        content_type='text/event-stream')
            else:
                collector = CollectingOutputChannel()
                on_new_message(UserMessage(text, collector, sender_id,
                                           input_channel=self.name()))
                return jsonify(collector.messages)

        return custom_webhook