from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import google_search

MODEL = 'gemini-3.5-flash'

pesquisador = Agent(
    name='pesquisador_web',
    model=MODEL,
    instruction=(
        'Pesquise o item informado no Mercado Livre. Liste de 4 a 5 produtos encontrados, '
        'cada um com o nome, detalhes, e preço quando houver. '
        'Não escreva conclusões, apenas retorne itens e o máximo de detalhes.'
    ),
    tools=[google_search],
    output_key='produtos',
)

redator = Agent(
    name='redator',
    model=MODEL,
    instruction=(
        'Escreva um compilado de um parágrafo com base apenas nestes produtos encontrados: {produtos}. '
        'Mantenha as fontes entre parênteses e indique incertezas ou divergências.'
    ),
)

root_agent = SequentialAgent(
    name='pesquisa_web_pipeline',
    sub_agents=[pesquisador, redator],
)