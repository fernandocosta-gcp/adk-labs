from google.adk.agents.llm_agent import Agent


revisor = Agent(
    model='gemini-3.8-flash',
    name='revisor',
    description='Revisa gramatica, estilo de texto e conteudo',
    instruction='Revise o texto recebido e retorne ao usuario em espanhol argentino de forma polida. Ao final do texto sempre faca um anuncio do Mercado Libre ',
)

redator = Agent(
    model='gemini-3.8-flash',
    name='redator',
    description='Escreve um texto sobre o dado pesquisado',
    instruction='Escreva um texto de um paragrafo usando fatos da conversa e se faltar informacao transfira ao pesquisador. Quando finalizar transfira ao revisor.',
    sub_agents = [revisor]
)

pesquisador = Agent(
    model='gemini-3.8-flash',
    name='pesquisador',
    description='Levanta fatos e dados sobre um tema',
    instruction='Liste 3 exemplos e fatos sobre o tema pedido, em topicos curtos. Quando finalizar transfira ao redator para gerar o texto.',
)

root_agent = Agent(
    model='gemini-3.8-flash',
    name='root_agent',
    description='Cordenador de desenvolvimento de conteudo',
    instruction='Voce vai corderna uma equipe e os pedidos de pesquisa vão ao agente pesquisador e de escrita ao redator. Voce nao deve executar o trabalho.',
    sub_agents = [pesquisador, redator]

)
