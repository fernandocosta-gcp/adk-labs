from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import google_search

MODEL = 'gemini-3.5-flash'

pesquisador = Agent(
    name='pesquisador_web',
    model=MODEL,
    instruction=(
        'Pesquise na web sobre o tema do usuário. Liste de 4 a 5 achados objetivos, '
        'cada um com o nome do site de origem e a data quando houver. '
        'Não escreva conclusões, apenas os achados.'
    ),
    tools=[google_search],
    output_key='achados',
)

redator = Agent(
    name='redator',
    model=MODEL,
    instruction=(
        'Escreva um resumo de um parágrafo com base apenas nestes achados: {achados}. '
        'Mantenha as fontes entre parênteses e indique incertezas ou divergências.'
    ),
)

root_agent = SequentialAgent(
    name='pesquisa_web_pipeline',
    sub_agents=[pesquisador, redator],
)