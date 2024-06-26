# Workshop ml-end2end: Desenvolvendo um ChatGPT com Docker-Compose
## Descrição
Este repositório contém o código-fonte e a documentação para o Workshop ml-end2end, onde criaremos um ChatGPT utilizando modelos de linguagem (LLMs) disponibilizados publicamente. Nosso sistema será composto por quatro módulos principais: Backend, Banco de Dados, Frontend e LLM.

## Metodologia
O workshop seguirá a seguinte metodologia:

1. Explicação dos conceitos:
    - Python como backend.
    - Utilização do framework Flask.
    - Conexão com APIs externas.
    - Conexão com banco de dados MariaDB.
    - Docker e Docker-Compose.
    - Arquitetura de software.
    - Frontend.
    - Modelos de linguagem (LLMs).
2. Organização em passos:
    - Cada etapa será dividida em “passos”.
    - Se você perder algo ou ficar para trás, poderá usar o comando `git clone --depth 1 --branch <tag_name> https://github.com/netoolii/ml-end2end` para baixar a versão correspondente e acompanhar a aula.
## Módulos do Projeto
1. Backend (API REST em Python com Flask e Gunicorn)
    - Controle de acesso dos usuários.
    - Adição de comandos específicos para a saída do modelo.
    - Salvar o prompt do usuário e a resposta do modelo LLM no banco de dados.
    - Retornar a resposta do modelo para o módulo Frontend.
    - Exibir a lista de prompts anteriores.
2. Banco de Dados (MariaDB)
    - Três tabelas: users, conversation e posts.
    - Armazenamento das conversas entre usuário e modelo.
3.  Frontend (HTML, CSS e JavaScript)
    - Funcionalidades:
        - Login.
        - Envio de comandos prompts para o módulo Backend.
        - Exibição de prompts e respostas para o usuário.
        - Lista de prompts anteriores.
4. Modelo de Linguagem (LLM)
    - Recebe o prompt e retorna a resposta para o módulo Backend.

## Detalhamento do Módulo Backend
1. Login
    - Verificação das credenciais fornecidas pelo usuário.
2. Criação de um Novo “Post”
    - Conversação entre usuário e modelo.
3. Consulta ao Banco de Dados MariaDB
    - Exibição da lista de posts do usuário corrente.
4. Processamento de Texto do Prompt
    - Requisição ao módulo LLM.
    - Salvar o prompt e a resposta do modelo.
    - Processamento do resultado e formatação da resposta API.

## Detalhamento do Banco de dados

1. Tabela `users`
    - id: integer
    - username: varchar
    - password: varchar
    - created_at: timestamp
2. Tabela `conversation`
    - id: integer
    - status: enum ['online', 'deleted']
    - user_id: `users.id`
    - created_at: timestamp
3. Tabela `posts`
    - id: integer
    - prompt: text
    - body: text
    - conversation_id: `conversation.id`
    - created_at: timestamp
