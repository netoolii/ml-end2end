from clients.base_ollama import OllamaBase


class TinyLlama(OllamaBase):
    def __init__(self, **kwargs):
        super().__init__(model="tinyllama", **kwargs)

    def request(self, content):
        return super().request(content)
