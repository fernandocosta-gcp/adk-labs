from google.adk.agents import Agent, ParallelAgent, SequentialAgent

MODEL = 'gemini-3.5-flash'

analista_tecnico = Agent(
    name='analista_tecnico',
    model=MODEL,
    instruction='Liste 3 pontos técnicos relevantes sobre o tema do usuário.',
    output_key='analise_tecnica',
)

analista_mercado = Agent(
    name='analista_mercado',
    model=MODEL,
    instruction='Liste 3 pontos de mercado (tendências, concorrentes, demanda) sobre o tema do usuário.',
    output_key='analise_mercado',
)

analista_riscos = Agent(
    name='analista_riscos',
    model=MODEL,
    instruction='Liste 3 riscos (técnicos, legais ou éticos) sobre o tema do usuário.',
    output_key='analise_riscos',
)

analises = ParallelAgent(
    name='analises_paralelas',
    sub_agents=[analista_tecnico, analista_mercado, analista_riscos],
)

sintetizador = Agent(
    name='sintetizador',
    model=MODEL,
    instruction=(
        'Monte um relatório executivo curto combinando: '
        'Técnico: {analise_tecnica} | Mercado: {analise_mercado} | Riscos: {analise_riscos}'
    ),
)

root_agent = SequentialAgent(
    name='relatorio_paralelo',
    sub_agents=[analises, sintetizador],
)