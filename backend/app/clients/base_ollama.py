import requests
import json
from flask import current_app
from helpers.env_helper import get_ollama_host, get_ollama_port
from helpers.commom import get_user_chat, get_assistant_chat


class OllamaBase:
    def __init__(self, model, stream=False, context=[]):
        self.url = f"http://{get_ollama_host()}:{get_ollama_port()}"
        self.route = "/api/chat"
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.model = model
        self.stream = stream
        self.data = {"model": self.model,
                     "stream": self.stream,
                     "messages": context}

    def check_is_running(self):
        response = requests.get(self.url)
        current_app.logger.info(str(response.status_code) + " " +
                                str(response.text), exc_info=True)
        if response.status_code == 200:
            return True
        return False

    def request(self, content):
        if self.check_is_running():
            if (len(self.data['messages']) == 0):
                self.data['messages'].append(get_assistant_chat(
                    """I'm an AI assistant that helps people find information.
                    Let me introduce my self, my name is Sophia"""))
            self.data['messages'].append(get_user_chat(content))
            response = requests.post(self.url+self.route,
                                     headers=self.headers,
                                     data=json.dumps(self.data))

            if response.status_code == 200:
                response_text = response.text
                data = json.loads(response_text)["message"]["content"]
                return data
            else:
                current_app.logger.critical(str(response.status_code) + " " +
                                            str(response.text), exc_info=True)
            return "-----MODEL NOT WORKING------"
        return "-----MODEL NOT RUNNING------"
