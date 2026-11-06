from google.adk.agents import Agent
from google.adk.tools.google_search_tool import GoogleSearchTool
from google.adk.tools.tool_context import ToolContext

MODEL = 'gemini-3.5-flash'


def salvar_nota(titulo: str, conteudo: str, tool_context: ToolContext) -> dict:
    """Salva uma nota de pesquisa no estado da sessão.

    Args:
        titulo: título curto da nota.
        conteudo: texto da nota, com a fonte.
    """
    notas = tool_context.state.get('notas', [])
    notas.append({'titulo': titulo, 'conteudo': conteudo})
    tool_context.state['notas'] = notas
    return {'status': 'ok', 'total_notas': len(notas)}


busca = GoogleSearchTool(bypass_multi_tools_limit=True)

root_agent = Agent(
    name='pesquisador_com_notas',
    model=MODEL,
    instruction=(
        'Você é um pesquisador. Para CADA pergunta do usuário, siga estes passos, nesta ordem: '
        '1) pesquise na web com a ferramenta de busca; '
        '2) chame a ferramenta salvar_nota com um título curto e um resumo que inclua a fonte; '
        '3) só depois escreva a resposta final ao usuário. '
        'Nunca escreva a resposta final sem antes chamar salvar_nota.'
    ),
    tools=[busca, salvar_nota],
)