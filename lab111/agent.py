from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext

MODEL = 'gemini-3.5-flash'


def salvar_perfil(nome: str, tom: str, tool_context: ToolContext) -> dict:
    """Salva o nome e o tom de conversa preferido do usuário.

    Args:
        nome: como o usuário quer ser chamado.
        tom: formal, informal ou divertido.
    """
    tool_context.state['user:nome'] = nome
    tool_context.state['user:tom'] = tom
    return {'status': 'ok', 'nome': nome, 'tom': tom}


root_agent = Agent(
    name='assistente_pessoal',
    model=MODEL,
    description='Assistente que lembra do usuário entre conversas.',
    instruction=(
        'Nome do usuário: {user:nome?}. Tom preferido: {user:tom?}. '
        'Se o nome ou o tom estiverem vazios, pergunte ao usuário e depois chame salvar_perfil. '
        'Se já estiverem preenchidos, não pergunte de novo: chame o usuário pelo nome '
        'e responda sempre no tom preferido.'
    ),
    tools=[salvar_perfil],
)