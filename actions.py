from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

import requests
from requests.auth import HTTPDigestAuth
import json
import datetime
from rasa_core_sdk.forms import FormAction, EntityFormField


class ActionWeather(Action):
    def name(self):
        return "action_weather"

    def run(self, dispatcher, tracker, domain):
        from apixu.client import ApixuClient

        api_key = "ed0b641d57bb4629a5c140954181509"
        client = ApixuClient(api_key)

        loc = tracker.get_slot("geo-city")
        current = client.getCurrentWeather(q=loc)
        city = current["location"]["name"]
        condition = current["current"]["condition"]["text"]
        temperature_c = current["current"]["temp_c"]
        humidity = current["current"]["humidity"]
        wind_mph = current["current"]["wind_mph"]

        response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(
            condition, city, temperature_c, humidity, wind_mph
        )

        dispatcher.utter_message(response)
        return [SlotSet("geo-city", loc)]


class ActionCreateTodoList(Action):
    def name(self):
        return "action_create_todo_list"

    def run(self, dispatcher, tracker, domain):

        listname = tracker.get_slot("todo-list-name")

        url = "http://tracker-app-tracker-api.7e14.starter-us-west-2.openshiftapps.com/api/v1/createTodoList"
        response = requests.get(url, params={"listName": listname})

        if response.status_code != 200:
            print("Errorr", format(response.status_code))
        else:
            print("Success")
        jsonResponse = response.json()
        print(jsonResponse["message"])
        dispatcher.utter_message(jsonResponse["message"])
        return []


class ActionAddTaskToList(Action):
    def name(self):
        return "action_add_task_to_list"

    def run(self, dispatcher, tracker, domain):

        listname = tracker.get_slot("todo-list-name")
        taskName = tracker.get_slot("task-name")
        url = "http://tracker-app-tracker-api.7e14.starter-us-west-2.openshiftapps.com/api/v1/addTaskToList"
        now = datetime.datetime.now()

        payload = {
            "name": listname,
            "taskList": [{"taskName": taskName, "date": str(now)}],
        }
        response = requests.post(url, data=None, json=payload)

        if response.status_code != 200:
            print("Error", format(response.status_code))
        else:
            print("Success")
        jsonResponse = response.json()
        print(jsonResponse["message"])
        dispatcher.utter_message(jsonResponse["message"])
        return []


class ActionRetrieveTodoList(Action):
    def name(self):
        return "action_retrieve_todo_list"

    def run(self, dispatcher, tracker, domain):

        listname = tracker.get_slot("todo-list-name")
        url = "http://tracker-app-tracker-api.7e14.starter-us-west-2.openshiftapps.com/api/v1/retrieveTodoList"

        response = requests.get(url, params={"listName": listname})

        if response.status_code != 200:
            print("Error", format(response.status_code))
        else:
            print("Success")
        jsonResponse = response.json()
        print(jsonResponse["message"])
        dispatcher.utter_message(jsonResponse["message"])
        return []
