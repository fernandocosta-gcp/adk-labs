from google.adk.agents import Agent, SequentialAgent

MODEL = 'gemini-3.5-flash'

planejador = Agent(
    name='planejador',
    model=MODEL,
    instruction='Crie um outline com 3 tópicos sobre o tema do usuário. Responda só com o outline.',
    output_key='outline',
)

redator = Agent(
    name='redator',
    model=MODEL,
    instruction='Escreva um texto curto seguindo este outline: {outline}',
    output_key='rascunho',
)

revisor = Agent(
    name='revisor',
    model=MODEL,
    instruction='Revise e melhore este texto, mantendo-o curto: {rascunho}',
    output_key='texto_final',
)

root_agent = SequentialAgent(
    name='pipeline_conteudo',
    sub_agents=[planejador, redator, revisor],
)