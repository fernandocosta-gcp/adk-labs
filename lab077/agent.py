from google.adk import Agent, Workflow
from google.adk.events import RequestInput

MODEL = 'gemini-3.5-flash'

redator = Agent(
    name='redator',
    model=MODEL,
    instruction='Escreva um comunicado curto, com 3 frases, sobre o tema do usuário.',
)


async def pedir_aprovacao(node_input: str):
    """Nó humano: pausa o fluxo e pede a decisão de uma pessoa."""
    yield RequestInput(
        message=f'Rascunho: {node_input} | Digite sim para publicar ou não para descartar.'
    )


def publicar(node_input: str) -> str:
    """Recebe a resposta humana como entrada e decide o destino."""
    if node_input.strip().lower() in ('sim', 's', 'yes'):
        return 'Publicado com sucesso.'
    return 'Descartado pelo revisor humano.'


root_agent = Workflow(
    name='aprovacao_hitl',
    edges=[('START', redator, pedir_aprovacao, publicar)],
)