from google.adk.agents import Agent
from google.adk.tools import google_search

MODEL = 'gemini-3.5-flash'

root_agent = Agent(
    name='assistente_web',
    model=MODEL,
    description='Responde perguntas com informações atuais de itens no Meercado Livre.',
    instruction=(
        'Você responde perguntas usando pesquisa na web e dados expostos do mercado livre. '
        'Use a ferramenta de busca sempre que a pergunta envolver itens de produtos,'
        'preços, ou qualquer coisa envolvendo detalhes de itens de produto no Mercado Livre. '
        'Cite dados dos itens solicitados e quando não encontrar a informação. Nunca invente e nunca traga de outro local qu enão seja o Mercado Livre.'
    ),
    tools=[google_search],
)