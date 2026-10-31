from google.adk.agents import Agent, LoopAgent, ParallelAgent, SequentialAgent
from google.adk.tools.tool_context import ToolContext

MODEL = 'gemini-3.5-flash'


def aprovar(tool_context: ToolContext) -> dict:
    """Chame quando o texto estiver aprovado."""
    tool_context.actions.escalate = True
    return {'status': 'aprovado'}


# 1) Coleta em paralelo
coletor_fatos = Agent(
    name='coletor_fatos',
    model=MODEL,
    instruction='Liste 4 fatos objetivos sobre o tema do usuário.',
    output_key='fatos',
)
coletor_exemplos = Agent(
    name='coletor_exemplos',
    model=MODEL,
    instruction='Liste 3 exemplos práticos ou casos reais sobre o tema do usuário.',
    output_key='exemplos',
)
coleta = ParallelAgent(
    name='coleta_paralela',
    sub_agents=[coletor_fatos, coletor_exemplos],
)

# 2) Rascunho
redator = Agent(
    name='redator',
    model=MODEL,
    instruction='Escreva um texto curto usando estes fatos: {fatos} e estes exemplos: {exemplos}',
    output_key='texto',
)

# 3) Refinamento em loop
critico = Agent(
    name='critico',
    model=MODEL,
    instruction=(
        'Avalie o texto: {texto}. Se estiver claro, correto e bem estruturado, '
        'chame a ferramenta aprovar. Senão, liste até 3 melhorias.'
    ),
    tools=[aprovar],
    output_key='critica',
)
refinador = Agent(
    name='refinador',
    model=MODEL,
    instruction=(
        'Reescreva o texto {texto} aplicando a crítica: {critica}. '
        'Se a crítica indicar aprovação, repita o texto sem alterações.'
    ),
    output_key='texto',
)
refinamento = LoopAgent(
    name='refinamento',
    sub_agents=[critico, refinador],
    max_iterations=2,
)

root_agent = SequentialAgent(
    name='pipeline_hibrido',
    sub_agents=[coleta, redator, refinamento],
)