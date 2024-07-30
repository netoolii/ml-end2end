FROM ollama/ollama:0.2.8


ENV MODEL_NAME=tinyllama
ENV OLLAMA_KEEP_ALIVE=24h
ENV OLLAMA_HOST=0.0.0.0

EXPOSE 11434

VOLUME [ "ollama:/root/.ollama" ]

RUN ollama serve & sleep 5 ; ollama pull tinyllama ; \
        echo "kill 'ollama serve' process" ; \
        ps -ef | grep 'ollama serve' | grep -v grep | awk '{print $2}' | xargs -r kill -9